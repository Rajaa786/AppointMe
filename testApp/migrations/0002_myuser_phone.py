# Generated by Django 4.0.3 on 2022-04-10 15:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='myuser',
            name='phone',
            field=models.CharField(default=0, max_length=12, unique=True, verbose_name='Phone No'),
        ),
    ]
