# Generated by Django 5.0.1 on 2024-01-26 21:38

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="LivinPlace",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("location", models.CharField(max_length=255)),
                (
                    "status",
                    models.CharField(
                        choices=[("New", "New"), ("Middle", "Middle"), ("Old", "Old")],
                        max_length=50,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="PeopleAdult",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=255)),
                ("family_name", models.CharField(max_length=255)),
                ("surname", models.CharField(max_length=255)),
                ("phone_number", models.CharField(max_length=20)),
                ("passport_card_number", models.CharField(max_length=20)),
                ("birth_date", models.DateField()),
                ("work", models.CharField(max_length=255)),
                (
                    "financial_status",
                    models.CharField(
                        choices=[
                            ("Rich", "Rich"),
                            ("Middle", "Middle"),
                            ("Poor", "Poor"),
                        ],
                        max_length=50,
                    ),
                ),
                ("property", models.CharField(max_length=255)),
                ("other_information", models.TextField()),
                (
                    "living_place",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="govapp.livinplace",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="ComplaintRecord",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("text", models.TextField()),
                ("location", models.CharField(max_length=255)),
                ("datetime", models.DateTimeField()),
                (
                    "adult",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="govapp.peopleadult",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="PeopleKid",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=255)),
                ("family_name", models.CharField(max_length=255)),
                ("surname", models.CharField(max_length=255)),
                ("birth_date", models.DateField()),
                ("property", models.CharField(max_length=255)),
                ("school", models.CharField(max_length=255)),
                ("other_information", models.TextField()),
                (
                    "living_place",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="govapp.livinplace",
                    ),
                ),
                ("parents", models.ManyToManyField(to="govapp.peopleadult")),
            ],
        ),
    ]
