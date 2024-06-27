from django.shortcuts import render
from datetime import datetime
from django.http import HttpResponse
def current_datetime(request):
    now =datetime.now ()
    html = f"<html><body><h1>Current Date and Time:</h1><p>{now}</p></body></html>"
    return HttpResponse(html)
