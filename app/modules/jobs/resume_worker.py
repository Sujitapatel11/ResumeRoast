from app.core.celery_app import celery_app
import logging

logger = logging.getLogger(__name__)


@celery_app.task(name="jobs.resume.analyze_resume")
def analyze_resume(job_id: str):
    """
    Background task to analyze a resume.
    """

    logger.info(f"Started resume analysis for Job ID: {job_id}")

    # TODO:
    # 1. Load job from database
    # 2. Download resume
    # 3. Extract text
    # 4. Call AI service
    # 5. Save analysis
    # 6. Mark job completed

    logger.info(f"Finished resume analysis for Job ID: {job_id}")

    return {
        "job_id": job_id,
        "status": "SUCCESS"
    }