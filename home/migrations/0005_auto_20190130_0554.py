# Generated by Django 2.1.5 on 2019-01-30 05:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_auto_20190130_0033'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='audio',
            new_name='files',
        ),
    ]