from django.contrib import admin
from .models import MyUser, Subscription


class MyUserAdmin(admin.ModelAdmin):
    search_fields = ['first_name', 'last_name', 'email']


admin.site.register(MyUser, MyUserAdmin)
admin.site.register(Subscription)
