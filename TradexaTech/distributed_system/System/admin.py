from django.contrib import admin

from .models import User,Product,Order

admin.site.register([User,Product,Order])