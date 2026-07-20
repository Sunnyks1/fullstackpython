from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser


class CustomerUserAdmin(UserAdmin):
    model=CustomUser
    list_display=['username','email','is_staff','is_active']
    fieldsets=UserAdmin.fieldsets +(
        ('Extra Info',{'fields':('bio',)}),
    )
admin.site.register(CustomUser,CustomerUserAdmin)
# Register your models here.