# Generated by Django 4.2.5 on 2023-12-26 19:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0003_delete_purpose'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='gender',
            field=models.CharField(choices=[('Male', 'Male'), ('Female', 'Female')], max_length=10),
        ),
    ]
