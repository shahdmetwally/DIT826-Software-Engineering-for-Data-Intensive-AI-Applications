# Generated by Django 4.2.7 on 2023-11-29 13:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_face_target'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='face',
            name='target',
        ),
    ]