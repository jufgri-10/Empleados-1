# Generated by Django 3.0.6 on 2020-07-16 21:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('persona', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='empleado',
            name='avatar',
            field=models.ImageField(blank=True, default='static/media/avatar2.png', null=True, upload_to='empleados'),
        ),
    ]
