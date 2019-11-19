from django.contrib import admin

# Register your models here.
from .models import BlogPost
# Need to register my BlogPost so it shows up in the admin
admin.site.register(BlogPost)
