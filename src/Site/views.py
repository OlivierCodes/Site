
from django.http import HttpResponse
from django.shortcuts import render
from datetime import datetime

def index(request):
    date = datetime.today()
    return render(request,
                  "Site/index.html",
                  context={"date":date})


