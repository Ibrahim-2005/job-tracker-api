from flask import Blueprint,request,jsonify
from app import db
from app.models.user import User
from werkzeug.security import generate_password_hash,check_password_hash
from flask_jwt_extended import create_access_token


auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/register', methods=['POST'])
def register():
    data = request.get_json()

    if not data or not data.get('email') or not data.get('password'):
        return jsonify({"warning": "Missing fields"}), 400

    if User.query.filter_by(email=data['email']).first():
        return jsonify({"error": "Email already exists"}), 400

    hashed_pw = generate_password_hash(data['password'])

    user = User(
        email=data['email'],
        password_hash=hashed_pw
    )

    db.session.add(user)
    db.session.commit()

    return jsonify({"msg": "User created"}), 201


@auth_bp.route('/login',methods=['POST'])
def login():
    data=request.get_json()
    if not data or not data.get('email') or not data.get('password'):
        return jsonify({"warning": "Missing fields"}), 400
    user=User.query.filter_by(email=data['email']).first()

    if not user:
        return jsonify({"error": "User not found"}), 401
    elif not check_password_hash(user.password_hash,data['password']):
        return jsonify({"error":"Invalid password"}),401
    
    token=create_access_token(identity=str(user.id))

    return jsonify({"access_token": token})