# Generated by Django 4.1.7 on 2023-02-23 13:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='tatto_artist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('registered_business_name', models.CharField(max_length=250)),
                ('trading_business_name', models.CharField(max_length=250)),
                ('business_registration_model', models.CharField(choices=[('Informal', 'Informal'), ('Solo Proprietor', 'Solo Proprietor'), ('Close Corperation', 'Close Corperation'), ('(Pty) Ltd', '(Pty) Ltd')], max_length=255)),
                ('name_of_owner', models.CharField(max_length=100)),
                ('id_no', models.CharField(max_length=13)),
                ('address_details', models.TextField()),
                ('phone_number', models.CharField(max_length=11)),
                ('practice_email', models.EmailField(max_length=254)),
                ('nature_of_your_business', models.CharField(choices=[(' Permanent Cosmetic Clinic', ' Permanent Cosmetic Clinic'), ('Training Course Provider', 'Training Course Provider'), ('Tattoo Studio', 'Tattoo Studio'), ('Plastic Surgery Practice', 'Plastic Surgery Practice'), ('Retreat Organiser', 'Retreat Organiser')], max_length=255)),
            ],
        ),
    ]
