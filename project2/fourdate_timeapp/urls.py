from django.urls import path
from fourdate_timeapp import views
urlpatterns = [
path('datetimeoffsets/', views.datetime_with_offsets, name= 'datetime_with_offsets '),
]