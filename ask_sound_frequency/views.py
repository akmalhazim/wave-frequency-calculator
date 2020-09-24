from django.http import HttpResponse
from django.shortcuts import render

def index(request):
  frequency = None
  velocity = None
  wavelength = None
  if validate(request):
    # frequency = (float(request.POST['velocity'])) / float(request.POST['wavelength'])
    frequency = calculate_frequency(float(request.POST['velocity']), float(request.POST['wavelength']))
    velocity = request.POST['velocity']
    wavelength = request.POST['wavelength']
  else:
    frequency = None

  return render(request, "index.html", {'frequency': frequency, "velocity": velocity, "wavelength": wavelength})

def validate(request):
  return request.method == 'POST' and request.POST['wavelength'] != 0

def calculate_frequency(velocity, wavelength):
  return velocity / wavelength