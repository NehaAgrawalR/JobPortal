from django.contrib import admin

# Register your models here.
from .models import *

#admin.site.register(User)

admin.site.register(SeekerUser)
admin.site.register(Provider)
admin.site.register(Job)