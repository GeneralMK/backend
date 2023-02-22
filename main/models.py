from django.db import models

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

class schedules(models.Manager):
    schedule_name=models.CharField(max_length=250)
    user=models.ForeignKey(patients, on_delete=models.CASCADE)
    start_date=models.DateTimeField()
    end_date= models.DateTimeField()

    def __str__(self):
        return self.schedule_name