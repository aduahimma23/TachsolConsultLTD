# Generated by Django 4.1 on 2023-10-20 19:27

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("accounts", "0001_initial"),
    ]

    operations = [
        migrations.DeleteModel(
            name="StaffUser",
        ),
    ]