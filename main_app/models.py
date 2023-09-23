from django.db import models
from django.urls import reverse

DIFFICULTIES = (
    ("E", "Easy"),
    ("M", "Moderate"),
    ("H", "Hard")
)

# Create your models here.
class National_park(models.Model):
    name = models.CharField(max_length=100)
    province = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    description = models.TextField(max_length=250)

    # Changing this instance method does not impact the database
    # Therefore, no makemigrations is necessary
    def __str__(self):
        return f"{self.name} ({self.id})"
    
    def get_absolute_url(self):
        return reverse("national_parks_detail", kwargs={"national_park_id": self.id})
    
class Trail(models.Model):
    name = models.CharField(max_length=100)
    difficulty = models.CharField(
        max_length=1,
        choices=DIFFICULTIES,
        default=DIFFICULTIES[1][0]
    )
    distance = models.FloatField("Trail Distance")
    national_park = models.ForeignKey(
        National_park,
        on_delete=models.CASCADE
    )
    def __str__(self):
        return f"{self.name} | {self.distance} km | difficulty: {self.get_difficulty_display()}"