# Generated by Django 4.0.3 on 2022-04-03 03:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='User',
            new_name='AppUser',
        ),
    ]