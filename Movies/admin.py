from django.contrib import admin

# Register your models here.
from .models import Movies, MovieAvailable

admin.site.register(Movies)
admin.site.register(MovieAvailable)
admin.site.site_header = 'BookMyShow - Akash Badole'
