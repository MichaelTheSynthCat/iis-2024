from django.apps import AppConfig
from animal_shelter.settings import SEED_DEMO_DATA


class ShelterConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "shelter"

    def ready(self):
        if SEED_DEMO_DATA:
            from .seeds import seed_demo_data

            seed_demo_data()
