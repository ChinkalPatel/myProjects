# Generated by Django 2.0.2 on 2019-01-28 18:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AuthGroup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=80, unique=True)),
            ],
            options={
                'db_table': 'auth_group',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthGroupPermissions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'db_table': 'auth_group_permissions',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthPermission',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('codename', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'auth_permission',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128)),
                ('last_login', models.DateTimeField(blank=True, null=True)),
                ('is_superuser', models.IntegerField()),
                ('username', models.CharField(max_length=150, unique=True)),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=150)),
                ('email', models.CharField(max_length=254)),
                ('is_staff', models.IntegerField()),
                ('is_active', models.IntegerField()),
                ('date_joined', models.DateTimeField()),
            ],
            options={
                'db_table': 'auth_user',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUserGroups',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'db_table': 'auth_user_groups',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUserUserPermissions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'db_table': 'auth_user_user_permissions',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Complain',
            fields=[
                ('complain_id', models.CharField(db_column='complain_Id', max_length=20, primary_key=True, serialize=False)),
                ('reason', models.CharField(blank=True, max_length=45, null=True)),
                ('date', models.DateField(blank=True, null=True)),
                ('status', models.CharField(blank=True, max_length=5, null=True)),
                ('student_studentid', models.CharField(blank=True, max_length=20, null=True)),
            ],
            options={
                'db_table': 'complain',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('course_id', models.CharField(db_column='course_Id', max_length=20, primary_key=True, serialize=False)),
                ('course_name', models.CharField(blank=True, db_column='course_Name', max_length=20, null=True)),
                ('course_branch', models.CharField(blank=True, db_column='course_Branch', max_length=20, null=True)),
                ('course_duration', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'course',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoAdminLog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('action_time', models.DateTimeField()),
                ('object_id', models.TextField(blank=True, null=True)),
                ('object_repr', models.CharField(max_length=200)),
                ('action_flag', models.PositiveSmallIntegerField()),
                ('change_message', models.TextField()),
            ],
            options={
                'db_table': 'django_admin_log',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoContentType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('app_label', models.CharField(max_length=100)),
                ('model', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'django_content_type',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoMigrations',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('app', models.CharField(max_length=255)),
                ('name', models.CharField(max_length=255)),
                ('applied', models.DateTimeField()),
            ],
            options={
                'db_table': 'django_migrations',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoSession',
            fields=[
                ('session_key', models.CharField(max_length=40, primary_key=True, serialize=False)),
                ('session_data', models.TextField()),
                ('expire_date', models.DateTimeField()),
            ],
            options={
                'db_table': 'django_session',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Electricitybill',
            fields=[
                ('electricitybill_id', models.CharField(db_column='electricitybill_Id', max_length=20, primary_key=True, serialize=False)),
                ('units', models.IntegerField(blank=True, null=True)),
                ('unit_price', models.IntegerField(blank=True, db_column='unit_Price', null=True)),
                ('payment_status', models.CharField(blank=True, db_column='payment_Status', max_length=5, null=True)),
                ('month', models.CharField(blank=True, max_length=10, null=True)),
                ('date_paid', models.DateField(blank=True, db_column='date_Paid', null=True)),
            ],
            options={
                'db_table': 'electricitybill',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('employeeid', models.IntegerField(db_column='employeeId', primary_key=True, serialize=False)),
                ('employee_name', models.CharField(blank=True, db_column='employee_Name', max_length=15, null=True)),
                ('dob', models.DateField(blank=True, db_column='DOB', null=True)),
                ('contact_no', models.IntegerField(blank=True, db_column='contact_NO', null=True)),
                ('aadhar_no', models.IntegerField(blank=True, db_column='aadhar_No', null=True)),
                ('job_assigned', models.CharField(blank=True, db_column='job_Assigned', max_length=20, null=True)),
                ('join_date', models.DateField(blank=True, db_column='join_Date', null=True)),
                ('gender', models.CharField(blank=True, max_length=10, null=True)),
            ],
            options={
                'db_table': 'employee',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='IngredientsDetails',
            fields=[
                ('ingredient_id', models.IntegerField(db_column='ingredient_Id', primary_key=True, serialize=False)),
                ('ingredients_name', models.CharField(blank=True, db_column='ingredients_Name', max_length=15, null=True)),
                ('ingredients_type', models.CharField(blank=True, db_column='ingredients_Type', max_length=45, null=True)),
            ],
            options={
                'db_table': 'ingredients_details',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Pyament',
            fields=[
                ('transection_id', models.CharField(db_column='transection_Id', max_length=20, primary_key=True, serialize=False)),
                ('phase', models.IntegerField(blank=True, db_column='Phase', null=True)),
                ('pyment_date', models.DateField(blank=True, db_column='pyment_Date', null=True)),
                ('payment_status', models.CharField(blank=True, db_column='payment_Status', max_length=3, null=True)),
            ],
            options={
                'db_table': 'pyament',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('room_id', models.CharField(db_column='room_Id', max_length=20, primary_key=True, serialize=False)),
                ('room_type', models.CharField(blank=True, db_column='room_Type', max_length=20, null=True)),
                ('capacity', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'room',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('studentid', models.CharField(db_column='studentId', max_length=10, primary_key=True, serialize=False)),
                ('password', models.CharField(blank=True, db_column='password', max_length=8, null=True)),
                ('student_fname', models.CharField(blank=True, db_column='student_Fname', max_length=15, null=True)),
                ('student_mname', models.CharField(blank=True, db_column='student_Mname', max_length=15, null=True)),
                ('student_lname', models.CharField(blank=True, db_column='student_Lname', max_length=15, null=True)),
                ('dob', models.DateField(blank=True, db_column='DOB', null=True)),
                ('address_houseno', models.IntegerField(blank=True, db_column='address_Houseno', null=True)),
                ('address_street', models.CharField(blank=True, db_column='address_Street', max_length=15, null=True)),
                ('address_city', models.CharField(blank=True, db_column='address_City', max_length=15, null=True)),
                ('address_district', models.CharField(blank=True, db_column='address_District', max_length=15, null=True)),
                ('address_state', models.CharField(blank=True, db_column='address_State', max_length=15, null=True)),
                ('contact_no', models.IntegerField(blank=True, db_column='contact_No', null=True)),
                ('emailid', models.CharField(blank=True, db_column='emailId', max_length=20, null=True)),
                ('blood_group', models.CharField(blank=True, db_column='blood_Group', max_length=5, null=True)),
                ('college_id', models.CharField(blank=True, db_column='college_Id', max_length=20, null=True)),
            ],
            options={
                'db_table': 'student',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='WeekMenu',
            fields=[
                ('date', models.IntegerField(primary_key=True, serialize=False)),
                ('breakfast', models.CharField(blank=True, max_length=20, null=True)),
                ('lunch', models.CharField(blank=True, max_length=45, null=True)),
                ('dinner', models.CharField(blank=True, max_length=45, null=True)),
            ],
            options={
                'db_table': 'week_menu',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='MessIngredients',
            fields=[
                ('quantity', models.FloatField(blank=True, null=True)),
                ('price', models.FloatField(blank=True, null=True)),
                ('purchace_date', models.DateField(blank=True, db_column='purchace_Date', null=True)),
                ('payment_status', models.CharField(blank=True, db_column='payment_Status', max_length=3, null=True)),
                ('ingredients_details_ingredient', models.ForeignKey(db_column='Ingredients_details_ingredient_Id', on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='student.IngredientsDetails')),
            ],
            options={
                'db_table': 'mess_ingredients',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Salary',
            fields=[
                ('month', models.CharField(blank=True, max_length=10, null=True)),
                ('payment_status', models.CharField(blank=True, db_column='payment_Status', max_length=5, null=True)),
                ('salary', models.IntegerField(blank=True, null=True)),
                ('employee_employeeid', models.OneToOneField(db_column='employee_employeeId', on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='student.Employee')),
            ],
            options={
                'db_table': 'salary',
                'managed': False,
            },
        ),
    ]
