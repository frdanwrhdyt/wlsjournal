from django.contrib import admin
from .models import User

class UserAdminView(admin.ModelAdmin):
    list_display = ('id','username', )

admin.site.register(User, UserAdminView)