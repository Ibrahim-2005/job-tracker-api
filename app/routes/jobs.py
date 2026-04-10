from flask import Blueprint, jsonify, request
from flask_jwt_extended import jwt_required, get_jwt_identity
from app.models.job import Job
from app import db

jobs_bp = Blueprint('jobs', __name__)

@jobs_bp.route('/jobs',methods=['POST'])
@jwt_required()
def create_job():
    user_id = get_jwt_identity()
    data=request.get_json()
    job=Job(
        user_id=user_id,
        company=data['company'],
        role=data['role']
    )
    db.session.add(job)
    db.session.commit()
    job_count = Job.query.filter_by(user_id=user_id).count()
    return jsonify({"msg":f"Job {(job_count)} created",}),201


@jobs_bp.route('/jobs', methods=['GET'])
@jwt_required()
def get_jobs():
    user_id=get_jwt_identity()
    jobs=Job.query.filter_by(user_id=user_id).all()

    return jsonify([
        {
            "id":j.id,
            "company":j.company,
            "role":j.role,
            "status":j.status

        }for j in jobs
    ])