# Generated by Django 4.1 on 2023-10-26 17:19

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("mainapp", "0003_portfolio"),
    ]

    operations = [
        migrations.CreateModel(
            name="Clients",
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
                ("Client_image", models.ImageField(upload_to="")),
                ("Client_name", models.CharField(default="", max_length=500)),
                ("year_joined", models.DateField()),
            ],
        ),
    ]
