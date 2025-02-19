#!/bin/sh

alembic upgrade head
python __main__.py