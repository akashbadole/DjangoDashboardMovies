# Generated by Django 4.0.4 on 2022-08-27 09:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Movies', '0002_alter_movies_booking'),
    ]

    operations = [
        migrations.RenameField(
            model_name='movies',
            old_name='Booking',
            new_name='ReleaseDate',
        ),
    ]
