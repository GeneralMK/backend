from django.db import models

# Create your models here.
class doctor(models.Model):
    practice_name= models.CharField(max_length=100, null=False)
    practice_number= models.BigIntegerField(max_length=250, null=False)
    doc_name=models.CharField(max_length=255, unique=False)
    practice_phone_number=models.CharField(max_length=100, null=False)
    address_details= models.TextField()
    banking_details=models.TextField()
    practice_email= models.EmailField()

    def __str__(self):
        return self.doc_name
