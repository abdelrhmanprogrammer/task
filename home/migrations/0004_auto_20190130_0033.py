# Generated by Django 2.1.5 on 2019-01-30 00:33

from django.db import migrations, models
import home.models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_post_audio'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='img',
            field=models.FileField(blank=True, upload_to=home.models.img_path),
        ),
    ]
