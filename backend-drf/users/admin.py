from django.contrib import admin
#from .models import User # insteed using this we can use.....
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin


# Register your models here.
User = get_user_model()

# For creating password non editable
class UserAdmin(BaseUserAdmin):
    list_display = ['email', 'first_name', 'last_name', 'is_active']
    fieldsets = () # Here this field modify the Password section as read only. So no one can edit the password


admin.site.register(User, UserAdmin) # But here also you need to pass UserAdmin......