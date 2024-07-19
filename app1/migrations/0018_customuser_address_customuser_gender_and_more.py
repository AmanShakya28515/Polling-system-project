# Generated by Django 5.0.6 on 2024-05-12 04:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0017_remove_profile_image_profile_profile_picture_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='address',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='customuser',
            name='gender',
            field=models.CharField(choices=[('male', 'Male'), ('female', 'Female'), ('other', 'Other')], default='male', max_length=10),
        ),
        migrations.AddField(
            model_name='customuser',
            name='mobile_number',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
    ]