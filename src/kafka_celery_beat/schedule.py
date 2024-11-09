from celery import Celery

from kafka_celery_beat.core import celeryconfig
from kafka_celery_beat.core.config import settings

celery = Celery(settings.APP_NAME)
# Set beat celery configuration
celery.config_from_object(celeryconfig)
# Execute task every 30 seconds
celery.conf.beat_schedule = {
    "task1": {
        "task": "kafka.read_messages",
        "schedule": 30.0,
    }
}
