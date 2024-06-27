from django.contrib import admin
from django.urls import path, include 
# Import include
urlpatterns = [
path('admin/', admin.site.urls),
path('fourdate_timeapp', include('fourdate_timeapp.urls')), 
# Include your app's URLs
]
