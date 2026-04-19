from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.schedulers.base import STATE_RUNNING
from datetime import datetime,timedelta,timezone
from app.models.job import Job
from app import db,cache

scheduler=BackgroundScheduler()
def mark_stale_jobs():
    deadline=datetime.now(timezone.utc())-timedelta(days=7)

    stale_jobs=Job.query.filter_by(Job.status=="applied",Job.created_at<deadline).all()
    for job in stale_jobs:
        job.notes = (job.notes or "") + " [STALE]"

    db.session.commit()

def clear_cache():
    cache.clear()

def start_scheduler():
    if scheduler.start!=STATE_RUNNING:
        scheduler.add_job(mark_stale_jobs,'interval',days=1)
        scheduler.add_job(clear_cache,'interval',weeks=1)
        scheduler.start()
