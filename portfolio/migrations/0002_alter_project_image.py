# Generated by Django 4.2.2 on 2023-06-29 14:45

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("portfolio", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="project",
            name="image",
            field=models.ImageField(upload_to="portfolio/images/"),
        ),
    ]