# Generated by Django 5.0.6 on 2024-05-10 10:05

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0013_poll_expiration_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='poll',
            name='expiration_date',
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='John Doe (Default)', max_length=200, null=True)),
                ('title', models.CharField(default='This is the default, title change it in profile.', max_length=200, null=True)),
                ('desc', models.CharField(default='Hey, there this is a default text description about you that you can change on after clicking on "Edit"', max_length=200, null=True)),
                ('profile_img', models.ImageField(blank=True, default='images/default.jpg', null=True, upload_to='images')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
