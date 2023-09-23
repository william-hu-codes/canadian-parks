from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import National_park
from .forms import TrailForm


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
    trail_form = TrailForm()
    return render(request, "national_parks/detail.html", {
        "national_park": national_park,
        "trail_form": trail_form
    })

class NationalParkCreate(CreateView):
    model = National_park
    fields = "__all__"
    # success_url = "/national_parks"

class NationalParkUpdate(UpdateView):
    model = National_park
    fields = ["province", "city", "description"]

class NationalParkDelete(DeleteView):
    model = National_park
    success_url = "/national-parks"

def add_trail(request, national_park_id):
    form = TrailForm(request.POST)
    if form.is_valid():
        new_trail = form.save(commit=False)
        new_trail.national_park_id = national_park_id
        new_trail.save()
    return redirect("national_parks_detail", national_park_id=national_park_id)