# Generated by Django 4.2.3 on 2023-07-22 21:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("services", "0005_alter_ghala_image"),
    ]

    operations = [
        migrations.AlterField(
            model_name="ghala",
            name="image",
            field=models.ImageField(default="default.jpg", upload_to="images"),
        ),
        migrations.AlterField(
            model_name="soko",
            name="image",
            field=models.ImageField(default="default.jpg", upload_to="images"),
        ),
    ]
