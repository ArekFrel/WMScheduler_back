import sys
import threading
from django.apps import AppConfig
run_once_lock = threading.Lock()
has_run = False


class PlannerConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'Planner'

    def ready(self):
        if not 'runserver' in sys.argv:
            return
        global has_run
        with run_once_lock:
            if not has_run:
                from .utils import refresh_data
                refresh_data()
                has_run = True

if __name__ == '__main__':
    pass