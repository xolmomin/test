from django.contrib import admin
from django.contrib.auth.models import Group

from app.models import New, Tag

admin.site.register(New)
admin.site.register(Tag)
admin.site.unregister(Group)
