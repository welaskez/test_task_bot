#!/bin/sh

if [ "$SERVICE_TYPE" = "bot" ]; then
    alembic upgrade head
    python __main__.py
elif [ "$SERVICE_TYPE" = "admin_panel" ]; then
    python run_admin_panel.py
fi