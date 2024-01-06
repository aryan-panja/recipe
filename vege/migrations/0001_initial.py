# Generated by Django 5.0 on 2024-01-06 12:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('recipe_name', models.CharField(max_length=200)),
                ('recipe_description', models.TextField()),
                ('recipe_image', models.ImageField(upload_to='images/')),
            ],
        ),
    ]
