# Generated by Django 4.1 on 2024-01-01 21:31

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("mainapp", "0012_remove_teammembers_contact_alter_contact_contact"),
    ]

    operations = [
        migrations.AlterField(
            model_name="contact",
            name="contact",
            field=models.IntegerField(),
        ),
    ]