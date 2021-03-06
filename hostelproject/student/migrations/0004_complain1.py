# Generated by Django 2.1.7 on 2019-02-27 04:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0003_canteen'),
    ]

    operations = [
        migrations.CreateModel(
            name='Complain1',
            fields=[
                ('complain_id', models.CharField(db_column='complain_Id', max_length=20, primary_key=True, serialize=False)),
                ('reason', models.CharField(blank=True, max_length=45, null=True)),
                ('date', models.DateField(blank=True, null=True)),
                ('status', models.CharField(blank=True, max_length=5, null=True)),
                ('student_studentid', models.CharField(blank=True, max_length=20, null=True)),
                ('proof', models.ImageField(null=True, upload_to='photo')),
            ],
            options={
                'db_table': 'complain1',
                'managed': False,
            },
        ),
    ]
