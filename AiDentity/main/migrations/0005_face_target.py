# Generated by Django 4.2.7 on 2023-11-29 12:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_face_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='face',
            name='target',
            field=models.IntegerField(default=1),
        ),
    ]
