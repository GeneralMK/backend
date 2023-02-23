from django.db import models
from django.conf import settings
from django.forms import ValidationError
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

    def validate_file_extension(value):
        if not value.name.endswith('.pdf'):
            raise ValidationError(u'File Not Supported!')
    identity_doc=models.FileField(upload_to="uploaded_files", validators=[validate_file_extension], null=True)
    residency=models.FileField(upload_to="uploaded_files", validators=[validate_file_extension], null=True)
    def __str__(self):
        return self.names

class booking(models.Model):
    schedule_name=models.CharField(max_length=250)
    user=models.ForeignKey(patients, on_delete=models.CASCADE)
    check_in=models.DateField()
    check_out= models.DateField()

    def __str__(self):
        return f'{self.user} has booked from {self.check_in} to {self.check_out}'
    def __str__(self):
        return self.schedule_name
