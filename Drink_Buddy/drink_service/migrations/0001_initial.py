# Generated by Django 4.2.2 on 2023-07-05 12:11

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Drink",
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
                ("name", models.CharField(max_length=100)),
                ("ingredients", models.TextField()),
                ("recipe", models.TextField()),
                ("timeofyear", models.CharField(max_length=100)),
                ("timetodrink", models.CharField(max_length=100)),
                ("socialsituation", models.CharField(max_length=100)),
                ("mood", models.CharField(max_length=100)),
                ("iscoffee", models.BooleanField(default=False)),
                ("istea", models.BooleanField(default=False)),
                ("isalcoholic", models.BooleanField(default=False)),
                ("isnonalcoholic", models.BooleanField(default=False)),
                (
                    "imagefile",
                    models.ImageField(
                        blank=True, null=True, upload_to="images/recipes"
                    ),
                ),
                ("temperatureoflocation", models.CharField(max_length=100)),
                ("timeofday", models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name="Drinks",
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
                ("description", models.CharField(max_length=250)),
                ("image", models.ImageField(upload_to="Drink/images/")),
                ("url", models.URLField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name="UserLocation",
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
                ("location", models.CharField(max_length=100)),
            ],
        ),
    ]
