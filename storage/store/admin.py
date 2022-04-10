from django.contrib import admin

from .models import *

admin.site.register(Keeper)
admin.site.register(Category)
admin.site.register(Tool)
admin.site.register(Operation)
