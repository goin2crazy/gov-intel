from django.db import models

class LivinPlace(models.Model):
    location = models.CharField(max_length=255)
    status = models.CharField(max_length=50, choices=[('New', 'New'), ('Middle', 'Middle'), ('Old', 'Old')])

class PeopleAdult(models.Model):
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

class ComplaintRecord(models.Model):
    text = models.TextField()
    location = models.CharField(max_length=255)
    adult = models.ForeignKey(PeopleAdult, on_delete=models.CASCADE)
    datetime = models.DateTimeField()

    def __str__(self):
        return f"Complaint at {self.location} on {self.datetime}"