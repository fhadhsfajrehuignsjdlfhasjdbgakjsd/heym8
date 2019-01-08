# Generated by Django 2.0.6 on 2018-07-02 14:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='NewsComplaint',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('theme', models.CharField(choices=[('ext_drugs_prop', 'Explicit extremism/drugs propaganda'), ('suic_call', 'Suicide call'), ('discredit', 'Discredit users because of their nationality, gender and religion'), ('adult_cont', 'Spreading adult content')], max_length=15)),
            ],
            options={
                'verbose_name': 'NewsComplaint',
                'verbose_name_plural': 'NewsComplaints',
            },
        ),
        migrations.CreateModel(
            name='NewsComplaintSet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nOfExtDugsPropComplaints', models.IntegerField()),
                ('nOfSuicCallComplaints', models.IntegerField()),
                ('nOfDiscreditComplaints', models.IntegerField()),
                ('nOfAdultContentComplaints', models.IntegerField()),
            ],
            options={
                'verbose_name': 'newsComplaintSet',
                'verbose_name_plural': 'newsComplaintSets',
            },
        ),
        migrations.CreateModel(
            name='ThoughtComplaint',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('theme', models.CharField(choices=[('ext_drugs_prop', 'Explicit extremism/drugs propaganda'), ('suic_call', 'Suicide call'), ('discredit', 'Discredit users because of their nationality, gender and religion'), ('adult_cont', 'Spreading adult content')], max_length=15)),
            ],
            options={
                'verbose_name': 'ThoughtComplaint',
                'verbose_name_plural': 'ThoughtComplaints',
            },
        ),
        migrations.CreateModel(
            name='ThoughtComplaintSet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nOfExtDrugsPropComplaints', models.IntegerField()),
                ('nOfSuicCallComplaints', models.IntegerField()),
                ('nOfDiscreditComplaints', models.IntegerField()),
                ('nOfAdultContentComplaints', models.IntegerField()),
            ],
            options={
                'verbose_name': 'thoughtComplaintSet',
                'verbose_name_plural': 'thoughtComplaintSets',
            },
        ),
    ]
