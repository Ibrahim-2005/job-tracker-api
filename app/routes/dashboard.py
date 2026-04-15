from flask import Blueprint, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from app.models.job import Job

dashboard_bp = Blueprint('dashboard', __name__)


@dashboard_bp.route('/dashboard', methods=['GET'])
@jwt_required()
def dashboard():
    user_id = int(get_jwt_identity())

    jobs = Job.query.filter_by(user_id=user_id, deleted_at=None)

    total_jobs = jobs.count()

    applied = jobs.filter_by(status='applied').count()
    interview = jobs.filter_by(status='interview').count()
    offer = jobs.filter_by(status='offer').count()
    rejected = jobs.filter_by(status='rejected').count()

    return jsonify({
        "message": "Dashboard stats",
        "data": {
            "total_jobs": total_jobs,
            "applied": applied,
            "interview": interview,
            "offer": offer,
            "rejected": rejected
        }
    })