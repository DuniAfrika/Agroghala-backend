# Generated by Django 4.2.3 on 2023-07-22 11:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("services", "0004_alter_ghala_image"),
    ]

    operations = [
        migrations.AlterField(
            model_name="ghala",
            name="image",
            field=models.ImageField(default="default.jpg", upload_to="images/"),
        ),
    ]
