# Generated by Django 4.0.2 on 2022-06-28 16:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BiodataModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=100)),
                ('contact', models.CharField(default='', max_length=100)),
                ('email', models.EmailField(default='', max_length=100)),
                ('place_of_birth', models.CharField(default='', max_length=100)),
                ('sub_place', models.CharField(default='', max_length=100)),
                ('dob', models.DateField(blank=True, default='2020-01-01', null=True)),
                ('timeofBirth', models.DateField(blank=True, default='2020-01-01', null=True)),
                ('caste', models.CharField(default='', max_length=100)),
                ('sub_caste', models.CharField(default='', max_length=100)),
                ('gotra', models.CharField(default='', max_length=100)),
                ('manglik', models.CharField(default='', max_length=100)),
                ('rashi', models.CharField(default='', max_length=100)),
                ('nakshatra', models.CharField(default='', max_length=100)),
                ('height', models.CharField(default='', max_length=100)),
                ('religion', models.CharField(default='', max_length=100)),
                ('education', models.CharField(default='', max_length=100)),
                ('employee', models.CharField(default='', max_length=100)),
                ('income', models.CharField(default='', max_length=100)),
                ('college_name', models.CharField(default='', max_length=100)),
                ('org_name', models.CharField(default='', max_length=100)),
                ('fname', models.CharField(default='', max_length=100)),
                ('mname', models.CharField(default='', max_length=100)),
                ('foccupation', models.CharField(default='', max_length=100)),
                ('moccupation', models.CharField(default='', max_length=100)),
                ('brothers', models.CharField(default='', max_length=100)),
                ('sisters', models.CharField(default='', max_length=100)),
                ('mbrothers', models.CharField(default='', max_length=100)),
                ('msisters', models.CharField(default='', max_length=100)),
                ('address', models.CharField(default='', max_length=100)),
            ],
        ),
    ]
