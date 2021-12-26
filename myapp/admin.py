from django.contrib import admin
from myapp.models import user

# Register your models here.
class userAdmin(admin.ModelAdmin):
    list_display=('name', 'JID', 'gentle', 'phone', 'gmail', 'password')
admin.site.register(user, userAdmin)