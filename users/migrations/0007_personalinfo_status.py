# Generated by Django 2.0.7 on 2018-08-09 05:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_auto_20180802_0243'),
    ]

    operations = [
        migrations.AddField(
            model_name='personalinfo',
            name='status',
            field=models.CharField(blank=True, max_length=125, null=True, verbose_name='status'),
        ),
    ]
