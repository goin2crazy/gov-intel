# Generated by Django 5.0.1 on 2024-01-28 00:02

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("govapp", "0003_peopleadult_user_alter_complaintrecord_rating_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="complaintrecord",
            name="datetime",
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]