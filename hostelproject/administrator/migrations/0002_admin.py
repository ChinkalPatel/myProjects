# Generated by Django 2.1.7 on 2019-03-06 22:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('administrator', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Admin',
            fields=[
                ('adminid', models.AutoField(primary_key=True, serialize=False)),
                ('fname', models.CharField(blank=True, max_length=45, null=True)),
                ('lname', models.CharField(blank=True, max_length=45, null=True)),
                ('mname', models.CharField(blank=True, max_length=45, null=True)),
                ('email', models.CharField(blank=True, max_length=45, null=True)),
                ('gender', models.CharField(blank=True, max_length=7, null=True)),
                ('city', models.CharField(blank=True, max_length=45, null=True)),
                ('address', models.CharField(blank=True, max_length=45, null=True)),
                ('profile', models.CharField(blank=True, max_length=200, null=True)),
            ],
            options={
                'db_table': 'admin',
                'managed': False,
            },
        ),
    ]
