from django.shortcuts import render
from .models import National_park

# baby step - usually a model is used to store data

# Create your views here.
def home(request):
    return render(request, "home.html")

def about(request):
    return render(request, "about.html")

def national_parks_index(request):
    national_parks = National_park.objects.all().order_by("name")
    return render(request, "national_parks/index.html", {
        "national_parks": national_parks
    })

def national_parks_detail(request, national_park_id):
    national_park = National_park.objects.get(id=national_park_id)
    return render(request, "national_parks/detail.html", {
        "national_park": national_park
    })