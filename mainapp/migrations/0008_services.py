# Generated by Django 4.1 on 2023-10-30 17:55

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("mainapp", "0007_teammembers"),
    ]

    operations = [
        migrations.CreateModel(
            name="Services",
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
                ("updated_by", models.CharField(default="Mr. Offei", max_length=50)),
                (
                    "content",
                    models.TextField(default="Enter the text here", max_length=10000),
                ),
            ],
        ),
    ]
