# Generated by Django 4.1 on 2024-01-01 21:29

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("mainapp", "0010_rename_update_the_about_page_about_about_content_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="contact",
            name="contact",
            field=models.IntegerField(blank=True, default=233207758838, max_length=15),
        ),
        migrations.AlterField(
            model_name="teammembers",
            name="contact",
            field=models.IntegerField(default=233207758838, max_length=15),
        ),
    ]