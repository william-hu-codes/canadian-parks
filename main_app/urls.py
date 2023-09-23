from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("about/", views.about, name="about"),
    path("national-parks/", views.national_parks_index, name="national_parks_index"),
    path("national-parks/<int:national_park_id>/", views.national_parks_detail, 
    name="national_parks_detail"),
    path("national_parks_create/", views.NationalParkCreate.as_view(), name="national_parks_create"),
    path("national_parks/<int:pk>/update", views.NationalParkUpdate.as_view(), name="national_parks_update"),
    path("national_parks/<int:pk>/delete", views.NationalParkDelete.as_view(), name="national_parks_delete"),
]