from flask import Blueprint,request,jsonify
from app import db
from app.models.user import User
from werkzeug.security import generate_password_hash


auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/register', methods=['POST'])
def register():
    data = request.get_json()

    if not data or not data.get('email') or not data.get('password'):
        return jsonify({"msg": "Missing fields"}), 400

    if User.query.filter_by(email=data['email']).first():
        return jsonify({"msg": "Email already exists"}), 400

    hashed_pw = generate_password_hash(data['password'])

    user = User(
        email=data['email'],
        password_hash=hashed_pw
    )

    db.session.add(user)
    db.session.commit()

    return jsonify({"msg": "User created"}), 201