from celery import Celery

from core.config import settings

celery_app = Celery(
    settings.celery.app_name,
    broker=settings.redis.get_url(),
    backend=settings.redis.get_url(),
)
