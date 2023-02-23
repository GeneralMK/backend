from django.db import models

# Create your models here.
class tatto_artist(models.Model):
    registered_business_name= models.CharField(max_length=250, null=False)
    trading_business_name= models.CharField(max_length=250, null=False)
    TYPE=(
        ("Informal","Informal"),
        ("Solo Proprietor","Solo Proprietor"),
        ("Close Corperation","Close Corperation"),
         ("(Pty) Ltd","(Pty) Ltd")
    )
    business_registration_model=models.CharField(max_length=255, unique=False,choices=TYPE)
    name_of_owner=models.CharField(max_length=100, null=False)
    id_no=models.CharField(max_length=13, null=False)
    address_details= models.TextField()
    phone_number=models.CharField(max_length=11,null=False)
    practice_email= models.EmailField()
    TYPES=(
        (" Permanent Cosmetic Clinic"," Permanent Cosmetic Clinic"),
        ("Training Course Provider","Training Course Provider"),
        ("Tattoo Studio","Tattoo Studio"),
        ("Plastic Surgery Practice","Plastic Surgery Practice"),
        ("Retreat Organiser","Retreat Organiser")
    )
    nature_of_your_business=models.CharField(max_length=255, unique=False,choices=TYPES)