from flask import Blueprint, jsonify, request
from flask_jwt_extended import jwt_required, get_jwt_identity
from app.models.job import Job
from app.models.status_history import StatusHistory
from app import db
from datetime import datetime,timezone

jobs_bp = Blueprint('jobs', __name__)

@jobs_bp.route('/jobs',methods=['POST'])
@jwt_required()
def create_job():
    user_id = int(get_jwt_identity())
    data=request.get_json()
    job=Job(
        user_id=user_id,
        company=data['company'],
        role=data['role']
    )
    db.session.add(job)
    db.session.commit()
    job_count = Job.query.filter_by(user_id=user_id).count()
    return jsonify({
        "message": "Job created successfully",
        "data": {
            "id": job.id,
            "company": job.company,
            "role": job.role,
            "status": job.status
        }
    }), 201


@jobs_bp.route('/jobs', methods=['GET'])
@jwt_required()
def get_jobs():
    user_id= int(get_jwt_identity())
    jobs=Job.query.filter_by(user_id=user_id,deleted_at=None).all()

    return jsonify([
        {
            "id":j.id,
            "company":j.company,
            "role":j.role,
            "status":j.status

        }for j in jobs
    ])

@jobs_bp.route('/jobs/<int:job_id>',methods=['PUT'])
@jwt_required()
def update_job(job_id):
    user_id= int(get_jwt_identity())
    data=request.get_json()

    job=Job.query.filter_by(id=job_id,user_id=user_id,deleted_at=None).first()
    if not job:
        return jsonify({"msg":"Job not found"}),404
    
    job.company=data.get('company',job.company)
    job.role=data.get('role',job.role)
    if 'status' in data and data['status'] != job.status:
        history = StatusHistory(
            job_id=job.id,
            from_status=job.status,
            to_status=data['status'],
            changed_at=datetime.now(timezone.utc)
        )
        db.session.add(history)
        job.status = data['status']

    db.session.commit()
    return jsonify({"msg": "Job updated"})

@jobs_bp.route('/jobs/<int:job_id>',methods=['DELETE'])
@jwt_required()
def delete_job(job_id):
    user_id= int(get_jwt_identity())
    
    job=Job.query.filter_by(id=job_id,user_id=user_id).first()

    if not job:
        return jsonify({"msg":"Job not found"}),404
    
    job.deleted_at=datetime.now(timezone.utc)
    db.session.commit()
    return jsonify({"msg":"Job Deleted"})


@jobs_bp.route('/jobs/<int:job_id>/history', methods=['GET'])
@jwt_required()
def get_history(job_id):
    user_id = int(get_jwt_identity())

    job = Job.query.filter_by(id=job_id,user_id=user_id,deleted_at=None).first()

    if not job:
        return jsonify({"error": "Job not found"}), 404

    history = StatusHistory.query.filter_by(job_id=job_id).all()

    return jsonify([
        {
            "from": h.from_status,
            "to": h.to_status,
            "time": h.changed_at
        } for h in history
    ])