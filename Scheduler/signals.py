from django.db.models.signals import post_migrate
from django.dispatch import receiver
from django.apps import apps

@receiver(post_migrate)
def create_temp_data(sender, **kwargs):
    if sender.name != 'Planner':  # upewnij się, że to Twoja aplikacja
        return
    # Import modeli tutaj, żeby uniknąć błędów importu
    MyModel = apps.get_model('Planner', 'MyModel')

    # Sprawdź, czy dane już istnieją, żeby nie dublować
    if not MyModel.objects.exists():
        MyModel.objects.create(name='Tymczasowy wpis')
