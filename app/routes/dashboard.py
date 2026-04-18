from flask import Blueprint, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from app.models.job import Job
from datetime import datetime,timezone,timedelta

dashboard_bp = Blueprint('dashboard', __name__)


@dashboard_bp.route('/dashboard', methods=['GET'])
@jwt_required()
def dashboard():
    user_id = int(get_jwt_identity())

    total_jobs = Job.query.filter_by(user_id=user_id, deleted_at=None).count()
    applied = Job.query.filter_by(user_id=user_id, status='applied', deleted_at=None).count()
    interview = Job.query.filter_by(user_id=user_id, status='interview', deleted_at=None).count()
    offer = Job.query.filter_by(user_id=user_id, status='offer', deleted_at=None).count()
    rejected = Job.query.filter_by(user_id=user_id, status='rejected', deleted_at=None).count()

    response_rate=0
    if total_jobs> 0:
        response_rate=((interview + offer)/total_jobs)*100
    return jsonify({
        "message": "Dashboard stats",
        "data": {
            "total_jobs": total_jobs,
            "applied": applied,
            "interview": interview,
            "offer": offer,
            "rejected": rejected,
            "response_rate": round(response_rate,2)
        }
    })

@dashboard_bp.route('/dashboard/stale',methods=['GET'])
@jwt_required()
def stale_jobs():
    
    user_id=int(get_jwt_identity())
    seven_days=datetime.now(timedelta.utc)-timedelta(days=7)

    jobs = Job.query.filter(
        Job.user_id == user_id,
        Job.status == 'applied',
        Job.created_at < seven_days,
        Job.deleted_at == None
    ).all()

    return jsonify({
        "message": "Stale jobs",
        "data": [
            {
                "id": j.id,
                "company": j.company,
                "role": j.role,
                "created_at": j.created_at.isoformat() if j.created_at else None
            } for j in jobs
        ]
    })