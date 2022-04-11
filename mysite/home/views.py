from re import TEMPLATE
from django.shortcuts import render
from django.http import HttpResponse
import datetime

TEMPLATE_DIRS = (
    'os.path.join(BASE_DIR, "templates")'
)

def index(request):
  today = datetime.datetime.now().date()
  time = datetime.datetime.now().time()
  return render (request, 'index.html', {'today':today, 'time':time})