# Generated by Django 4.1 on 2023-10-24 08:54

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("mainapp", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="IndividualAbooutPage",
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
                ("image", models.ImageField(upload_to="")),
                ("Name", models.CharField(default="", max_length=50)),
                ("position", models.CharField(max_length=50)),
                ("title", models.CharField(max_length=100)),
                ("content", models.TextField(default="", max_length=1500)),
            ],
        ),
    ]