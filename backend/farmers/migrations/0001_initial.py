# Generated by Django 4.2.3 on 2023-07-15 09:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Farmer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(default='', max_length=50)),
                ('last_name', models.CharField(default='', max_length=50)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('phone', models.IntegerField(default=None, unique=True)),
                ('location', models.CharField(max_length=50)),
            ],
        ),
    ]
