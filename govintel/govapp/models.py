from django.contrib import admin
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class LivinPlace(models.Model):
    location = models.CharField(max_length=255)
    status = models.CharField(max_length=50, choices=[('New', 'New'), ('Middle', 'Middle'), ('Old', 'Old')])

    def __str__(self): 
        return f"{self.location} ({self.status})"

class PeopleAdult(models.Model):    
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    name = models.CharField(max_length=255)
    family_name = models.CharField(max_length=255)
    surname = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=20)
    passport_card_number = models.CharField(max_length=20)
    living_place = models.ForeignKey(LivinPlace, on_delete=models.CASCADE)
    birth_date = models.DateField()
    work = models.CharField(max_length=255)
    financial_status = models.CharField(max_length=50, choices=[('Rich', 'Rich'), ('Middle', 'Middle'), ('Poor', 'Poor')])
    property = models.CharField(max_length=255)
    other_information = models.TextField()

    def __str__(self): 
        return f"({self.phone_number}) {self.family_name} {self.name}"

class PeopleKid(models.Model):
    name = models.CharField(max_length=255)
    family_name = models.CharField(max_length=255)
    surname = models.CharField(max_length=255)
    birth_date = models.DateField()
    living_place = models.ForeignKey(LivinPlace, on_delete=models.CASCADE)
    property = models.CharField(max_length=255)
    school = models.CharField(max_length=255)
    parents = models.ManyToManyField(PeopleAdult)
    other_information = models.TextField()

    def __str__(self): 
        return f"{self.family_name} {self.name} ({self.birth_date.year})"

from django.core.validators import MinValueValidator, MaxValueValidator

class ComplaintRecord(models.Model):
    text = models.TextField()
    location = models.CharField(max_length=255)
    adult = models.ForeignKey(PeopleAdult, on_delete=models.CASCADE)
    datetime = models.DateTimeField(default=timezone.now)

    type = models.CharField(max_length=20)
    rating = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(3)]
    )

    def __str__(self):
        return f"Complaint at {self.location} on {self.datetime}"

admin.site.register(LivinPlace)
admin.site.register(PeopleAdult)
admin.site.register(PeopleKid)
admin.site.register(ComplaintRecord)