# Generated by Django 2.2.6 on 2019-10-08 21:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_auto_20191009_0236'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='facebook',
            field=models.CharField(default='', max_length=150),
        ),
        migrations.AlterField(
            model_name='profile',
            name='linkedin',
            field=models.CharField(default='', max_length=150),
        ),
        migrations.AlterField(
            model_name='profile',
            name='twitter',
            field=models.CharField(default='', max_length=150),
        ),
        migrations.AlterField(
            model_name='profile',
            name='website',
            field=models.CharField(default='', max_length=150),
        ),
    ]