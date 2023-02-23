from django.db import models
from django.conf import settings
# Create your models here.
class category(models.Model):
    TYPE=(
        ("Doctor","Doctor"),
        ("Tattoo Studio", "Tattoo Studio"),
        ("Nurse","Nurse"),
        ("Care-Facility", "Care-Facility"),

    )
    category= models.CharField(max_length=200, null=True, choices=TYPE)

    
class patients(models.Model):
    names=models.CharField(max_length=100)
    email=models.EmailField(max_length=100)
    password=models.CharField(max_length=12)
    document=models.FileField(upload_to="uploads")
    
    def __str__(self):
        return self.names

class booking(models.Manager):
    schedule_name=models.CharField(max_length=250)
    user=models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    check_in=models.DurationField()
    check_out= models.DurationField()

    def __str__(self):
        return f'{self.user} has booked from {self.check_in} to {self.check_out}'
    def __str__(self):
        return self.schedule_name
          