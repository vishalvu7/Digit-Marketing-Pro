from django.contrib import admin

from django.contrib.auth.models import User

from digitalmarketingapp.models import UserDetails
# Register your models here.

admin.site.register(UserDetails)

class AdminUserDetails(admin.ModelAdmin):
    list_display = ['mobiles','defaultbalance','senderIds','user']