from flask import Blueprint,request,jsonify
from app import db
from app.models.user import User
from werkzeug.security import generate_password_hash,check_password_hash
from flask_jwt_extended import create_access_token
from app.schemas.user_schema import UserSchema

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/register', methods=['POST'])
def register():
    data = request.get_json()

    if not data:
        return jsonify({"error": "No data", "code": 400}), 400

    schema = UserSchema()
    errors = schema.validate(data)

    if errors:
        return jsonify({"error": errors, "code": 422}), 422

    if User.query.filter_by(email=data['email']).first():
        return jsonify({"error": "Email already exists","code": 400}), 400

    hashed_pw = generate_password_hash(data['password'])

    user = User(
        email=data['email'],
        password_hash=hashed_pw
    )

    db.session.add(user)
    db.session.commit()

    return jsonify({"message": "User created","data": {"email": user.email}}), 201


@auth_bp.route('/login',methods=['POST'])
def login():
    data=request.get_json()
    if not data or not data.get('email') or not data.get('password'):
        return jsonify({"error": "Missing fields","code": 400}), 400
    user=User.query.filter_by(email=data['email']).first()

    if not user or not check_password_hash(user.password_hash, data['password']):
        return jsonify({"error": "Invalid credentials","code": 401}), 401
    
    token=create_access_token(identity=str(user.id))

    return jsonify({"message": "Login successful","data": {"access_token": token}})