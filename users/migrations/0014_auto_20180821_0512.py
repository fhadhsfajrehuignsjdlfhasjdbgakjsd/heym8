# Generated by Django 2.0.7 on 2018-08-21 05:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0013_auto_20180818_0358'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userpicture',
            name='picture',
            field=models.ImageField(upload_to='pics'),
        ),
        migrations.AlterField(
            model_name='usersettings',
            name='whoCanSeeMyAlbums',
            field=models.CharField(default='all', max_length=6),
        ),
    ]
