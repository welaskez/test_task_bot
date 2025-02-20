#!/bin/sh

if [ "$SERVICE_TYPE" = "bot" ]; then
    alembic upgrade head
    python __main__.py
elif [ "$SERVICE_TYPE" = "admin_panel" ]; then
    python run_admin_panel.py
elif [ "$SERVICE_TYPE" = "celery_worker" ]; then
    celery -A core.celery.app worker --loglevel=info
elif [ "$SERVICE_TYPE" = "celery_beat" ]; then
    celery -A core.celery.app beat --loglevel=info
fi