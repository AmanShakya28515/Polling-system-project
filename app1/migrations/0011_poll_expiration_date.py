# Generated by Django 5.0.2 on 2024-04-02 07:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0010_remove_poll_expiration_datetime'),
    ]

    operations = [
        migrations.AddField(
            model_name='poll',
            name='expiration_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
