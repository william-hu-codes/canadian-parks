from django.shortcuts import render

# baby step - usually a model is used to store data
national_parks = [
    {"name": "Banff National Park", "city": "Banff", "province": "Alberta"},
    {"name": "Jasper National Park", "city": "Jasper", "province": "Alberta"},
]

# Create your views here.
def home(request):
    return render(request, "home.html")

def about(request):
    return render(request, "about.html")

def national_parks_index(request):
    return render(request, "national_parks/index.html", {
        "national_parks": national_parks
    })