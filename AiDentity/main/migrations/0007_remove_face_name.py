# Generated by Django 4.2.7 on 2023-11-30 22:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_remove_face_target'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='face',
            name='name',
        ),
    ]
