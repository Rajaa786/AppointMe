# Generated by Django 4.0.3 on 2022-04-17 07:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testApp', '0003_alter_myuser_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myuser',
            name='username',
            field=models.CharField(default='Guest', max_length=50),
            preserve_default=False,
        ),
    ]