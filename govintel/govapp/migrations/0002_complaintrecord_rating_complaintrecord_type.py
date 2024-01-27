# Generated by Django 5.0.1 on 2024-01-27 13:50

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("govapp", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="complaintrecord",
            name="rating",
            field=models.CharField(
                choices=[
                    ("ChildrensRights", "Children's Rights"),
                    ("WomensRights", "Women's Rights"),
                    ("Disability", "Disability"),
                    ("Violence", "Violence"),
                    ("Divorce", "Divorce"),
                ],
                default=1,
                max_length=20,
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="complaintrecord",
            name="type",
            field=models.CharField(
                choices=[
                    ("ChildrensRights", "Children's Rights"),
                    ("WomensRights", "Women's Rights"),
                    ("Disability", "Disability"),
                    ("Violence", "Violence"),
                    ("Divorce", "Divorce"),
                ],
                default="Not Serious",
                max_length=20,
            ),
            preserve_default=False,
        ),
    ]
