# Generated by Django 2.0.7 on 2018-08-02 02:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_remove_personalinfo_dob'),
    ]

    operations = [
        migrations.AddField(
            model_name='personalinfo',
            name='dob',
            field=models.DateField(blank=True, null=True, verbose_name='Date of birth'),
        ),
    ]
