# Generated by Django 4.2.3 on 2023-07-20 21:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("blogs", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="blog",
            name="comments",
        ),
        migrations.AddField(
            model_name="comment",
            name="blog",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="comments",
                to="blogs.blog",
            ),
        ),
    ]