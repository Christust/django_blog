from django.apps import AppConfig


class BlogConfig(AppConfig):
    # Cambiamos name colocando antes del nombre 'aplicaciones.' para que podamos hacer migraciones y las tome en cuenta.
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'aplicaciones.blog'
