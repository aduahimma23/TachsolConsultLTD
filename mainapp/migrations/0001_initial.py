# Generated by Django 5.0.1 on 2024-02-14 09:00

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="About",
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
                (
                    "title",
                    models.CharField(
                        default="About Tachsol Consultancy LTD", max_length=150
                    ),
                ),
                ("content", models.TextField()),
                (
                    "image",
                    models.ImageField(blank=True, null=True, upload_to="about_images/"),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
            ],
        ),
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
                ("image", models.ImageField(upload_to="clients_image/")),
                (
                    "name",
                    models.CharField(default="@Tachsol Consult LTD", max_length=500),
                ),
                ("location", models.CharField(default="Accra", max_length=50)),
                ("description", models.CharField(default="Tachsol", max_length=100)),
                (
                    "contact",
                    models.CharField(
                        default="+233208157526",
                        help_text="Enter in the format: +1234567890",
                        max_length=15,
                    ),
                ),
                (
                    "website_link",
                    models.URLField(blank=True, default="http://tachsol.com"),
                ),
                (
                    "email",
                    models.EmailField(default="info@tachsol.com", max_length=254),
                ),
                ("sector_of_work", models.CharField(default="Banking", max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name="Mission",
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
                ("created_at", models.DateField(auto_now_add=True)),
                ("content", models.TextField(max_length=2000)),
            ],
        ),
        migrations.CreateModel(
            name="Portfolio",
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
                (
                    "title",
                    models.CharField(
                        choices=[("Mr.", "Mr"), ("Ms.", "Ms"), ("Mrs.", "Mrs")],
                        max_length=5,
                    ),
                ),
                ("name", models.CharField(default="Tachsol", max_length=50)),
                (
                    "email",
                    models.EmailField(default="tachsol.km@gmail.com", max_length=254),
                ),
                ("image", models.ImageField(blank=True, upload_to="portfolio_images/")),
                (
                    "content",
                    models.TextField(default="Tachsol Consult", max_length=1500),
                ),
                (
                    "phone_number",
                    models.CharField(
                        default="+1234567890",
                        help_text="Enter in the format: +1234567890",
                        max_length=15,
                    ),
                ),
                (
                    "work_experience",
                    models.TextField(default="legal practitioner", max_length=1000),
                ),
                (
                    "educational_background",
                    models.TextField(
                        default="Write something about your educational background",
                        max_length=500,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Project",
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
                ("title", models.CharField(max_length=100)),
                ("description", models.TextField()),
                ("start_date", models.DateField()),
                ("end_date", models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name="ScopeOfOperation",
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
                (
                    "name",
                    models.CharField(
                        default="Human Resource Development, Training, and Facilitation",
                        max_length=100,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="TeamMembers",
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
                ("name", models.CharField(default="Tachsol", max_length=100)),
                ("position", models.CharField(default="Founder", max_length=50)),
                (
                    "email",
                    models.EmailField(default="info@tachsol.com", max_length=254),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Testimonial",
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
                (
                    "title",
                    models.CharField(
                        choices=[("Mr.", "Mr"), ("Ms.", "Ms"), ("Mrs.", "Mrs")],
                        max_length=5,
                    ),
                ),
                (
                    "author",
                    models.CharField(default="Mr. Martin Offei", max_length=100),
                ),
                (
                    "content",
                    models.TextField(
                        default="Write the testimonial here", max_length=1500
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Title",
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
                (
                    "gender",
                    models.CharField(
                        choices=[("Mr.", "Mr"), ("Ms.", "Ms"), ("Mrs.", "Mrs")],
                        default="Mr",
                        max_length=20,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="EmploymentRecord",
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
                ("year", models.DateField()),
                ("position", models.CharField(blank=True, default="", max_length=50)),
                (
                    "duties",
                    models.TextField(default="Overall management", max_length=500),
                ),
                (
                    "portfolio",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="mainapp.portfolio",
                    ),
                ),
            ],
        ),
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
                (
                    "activity",
                    models.CharField(
                        default="Training Needs Assessment", max_length=255
                    ),
                ),
                (
                    "description",
                    models.TextField(
                        blank=True,
                        default="Short note about the activity",
                        max_length=255,
                    ),
                ),
                (
                    "scope",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="services",
                        to="mainapp.scopeofoperation",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="HomePage",
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
                ("welcome_message", models.TextField()),
                ("projects", models.ManyToManyField(to="mainapp.project")),
                ("services", models.ManyToManyField(to="mainapp.services")),
                ("testimonials", models.ManyToManyField(to="mainapp.testimonial")),
            ],
        ),
    ]
