from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("about/", views.about, name="about"),
    path("national-parks/", views.national_parks_index, name="national_parks_index"),
    path("national-parks/<int:national_park_id>/", views.national_parks_detail, name="national_parks_detail")
]