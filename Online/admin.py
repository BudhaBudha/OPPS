from django.contrib import admin
from django.apps import apps
from .models import *

post_models = apps.get_app_config('Online').get_models()
for model in post_models:
    admin.site.register(model)

#Register your models here.
