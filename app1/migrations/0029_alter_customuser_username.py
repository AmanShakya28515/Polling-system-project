# Generated by Django 5.0.6 on 2024-06-21 13:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0028_alter_poll_end_date_alter_poll_start_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='username',
            field=models.CharField(max_length=10, unique=True),
        ),
    ]
