# Generated by Django 4.0.7 on 2023-01-04 14:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('departments', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Departament',
            new_name='Department',
        ),
    ]