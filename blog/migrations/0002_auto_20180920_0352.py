# Generated by Django 2.0.5 on 2018-09-20 03:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='category',
            old_name='mame',
            new_name='name',
        ),
    ]
