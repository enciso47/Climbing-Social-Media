from django.contrib import admin
from .models import *

admin.site.register(UserProfile)
admin.site.register(GymProfile)
admin.site.register(Comment)
admin.site.register(Post)
