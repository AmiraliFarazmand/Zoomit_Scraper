#!/bin/ash

echo "applyiing migrations:"
python manage.py migrate report
# sleep 120
exec "$@"