# Generated by Django 4.0.3 on 2022-04-07 01:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0002_rename_user_appuser'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='appuser',
            table='User',
        ),
        migrations.CreateModel(
            name='Note',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('resume', models.TextField(max_length=200)),
                ('body', models.TextField(max_length=400)),
                ('publish_date', models.DateTimeField()),
                ('image', models.ImageField(upload_to='')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='notes.appuser')),
            ],
        ),
    ]
