# Generated by Django 4.1 on 2024-01-01 21:34

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("mainapp", "0014_alter_contact_contact"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="contact",
            name="contact",
        ),
    ]