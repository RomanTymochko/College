# Generated by Django 2.2.6 on 2019-11-01 15:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0002_galleryimage_gallery'),
    ]

    operations = [
        migrations.AlterField(
            model_name='galleryimage',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='gallery/'),
        ),
    ]