# Generated by Django 4.0.3 on 2022-03-18 06:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalogue', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='phone',
            old_name='Phone',
            new_name='phone',
        ),
    ]
