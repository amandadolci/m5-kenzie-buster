# Generated by Django 4.2.4 on 2023-08-14 20:15

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("movies", "0002_movieorder_movie_order"),
    ]

    operations = [
        migrations.RenameField(
            model_name="movieorder",
            old_name="buyed_at",
            new_name="bought_at",
        ),
    ]
