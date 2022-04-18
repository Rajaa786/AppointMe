# Generated by Django 4.0.3 on 2022-04-18 15:59

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('testApp', '0007_alter_userprofile_role'),
    ]

    operations = [
        migrations.CreateModel(
            name='AppointmentMade',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('appointment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='testApp.appointments')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]