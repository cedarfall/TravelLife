# Generated by Django 2.2.6 on 2019-10-09 16:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20191009_2218'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='end_date',
            new_name='date',
        ),
        migrations.RemoveField(
            model_name='post',
            name='amenities',
        ),
        migrations.RemoveField(
            model_name='post',
            name='no_of_guests',
        ),
        migrations.RemoveField(
            model_name='post',
            name='start_date',
        ),
    ]
