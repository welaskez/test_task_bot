from datetime import timedelta

from celery import Celery

import core.celery.jobs  # type: ignore # noqa
from core.config import settings

celery_app = Celery(
    settings.celery.app_name,
    broker=settings.redis.get_url(),
    backend=settings.redis.get_url(),
)

celery_app.autodiscover_tasks()

celery_app.conf.beat_schedule = {
    "scheduled_mailing": {
        "task": "core.celery.jobs.start_mailing",
        "schedule": timedelta(seconds=10),
    },
}
celery_app.conf.broker_connection_retry_on_startup = True
