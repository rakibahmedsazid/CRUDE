# Generated by Django 4.2.5 on 2023-10-04 19:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employes',
            name='img',
            field=models.ImageField(upload_to='images'),
        ),
    ]
