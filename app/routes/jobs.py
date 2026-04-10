from flask import Blueprint, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity

jobs_bp = Blueprint('jobs', __name__)

@jobs_bp.route('/jobs', methods=['GET'])
@jwt_required()
def get_jobs():
    user_id = int(get_jwt_identity())
    return jsonify({
        "msg": "Access granted",
        "user_id": user_id
    })