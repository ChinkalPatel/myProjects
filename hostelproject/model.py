# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Admin(models.Model):
    adminid = models.AutoField(primary_key=True)
    fname = models.CharField(max_length=45, blank=True, null=True)
    lname = models.CharField(max_length=45, blank=True, null=True)
    mname = models.CharField(max_length=45, blank=True, null=True)
    email = models.CharField(max_length=45, blank=True, null=True)
    gender = models.CharField(max_length=7, blank=True, null=True)
    city = models.CharField(max_length=45, blank=True, null=True)
    address = models.CharField(max_length=45, blank=True, null=True)
    profile = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'admin'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=80)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class Canteen(models.Model):
    itemid = models.IntegerField(primary_key=True)
    itemname = models.CharField(max_length=45, blank=True, null=True)
    itemprice = models.IntegerField(blank=True, null=True)
    image = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'canteen'


class Complain(models.Model):
    complain_id = models.AutoField(db_column='complain_Id', primary_key=True)  # Field name made lowercase.
    reason = models.CharField(max_length=45, blank=True, null=True)
    date = models.DateField(blank=True, null=True)
    status = models.CharField(max_length=5, blank=True, null=True)
    student_studentid = models.CharField(db_column='student_studentId', max_length=20, blank=True, null=True)  # Field name made lowercase.
    proof = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'complain'


class Course(models.Model):
    course_id = models.CharField(db_column='course_Id', primary_key=True, max_length=20)  # Field name made lowercase.
    course_name = models.CharField(db_column='course_Name', max_length=20, blank=True, null=True)  # Field name made lowercase.
    course_branch = models.CharField(db_column='course_Branch', max_length=20, blank=True, null=True)  # Field name made lowercase.
    course_duration = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'course'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Electricitybill(models.Model):
    electricitybill_id = models.AutoField(db_column='electricitybill_Id', primary_key=True)  # Field name made lowercase.
    units = models.IntegerField(blank=True, null=True)
    unit_price = models.IntegerField(db_column='unit_Price', blank=True, null=True)  # Field name made lowercase.
    payment_status = models.CharField(db_column='payment_Status', max_length=10, blank=True, null=True)  # Field name made lowercase.
    month = models.CharField(max_length=10, blank=True, null=True)
    date_paid = models.DateField(db_column='date_Paid', blank=True, null=True)  # Field name made lowercase.
    studentid = models.IntegerField(blank=True, null=True)
    totalprice = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'electricitybill'


class Employee(models.Model):
    employeeid = models.AutoField(db_column='employeeId', primary_key=True)  # Field name made lowercase.
    employee_name = models.CharField(db_column='employee_Name', max_length=15, blank=True, null=True)  # Field name made lowercase.
    dob = models.DateField(db_column='DOB', blank=True, null=True)  # Field name made lowercase.
    contact_no = models.DecimalField(db_column='contact_NO', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    aadhar_no = models.DecimalField(db_column='aadhar_No', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    salary = models.FloatField(blank=True, null=True)
    job_assigned = models.CharField(db_column='job_Assigned', max_length=20, blank=True, null=True)  # Field name made lowercase.
    join_date = models.DateField(db_column='join_Date', blank=True, null=True)  # Field name made lowercase.
    gender = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'employee'


class Gatepass(models.Model):
    gatepassid = models.AutoField(db_column='gatepassId', primary_key=True)  # Field name made lowercase.
    studentid = models.CharField(db_column='studentId', max_length=10, blank=True, null=True)  # Field name made lowercase.
    place = models.CharField(max_length=20, blank=True, null=True)
    sdate = models.DateField(blank=True, null=True)
    ddate = models.DateField(blank=True, null=True)
    cheak = models.CharField(max_length=10, blank=True, null=True)
    status = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'gatepass'


class IngredientsDetails(models.Model):
    ingredient_id = models.IntegerField(db_column='ingredient_Id', primary_key=True)  # Field name made lowercase.
    ingredients_name = models.CharField(db_column='ingredients_Name', max_length=15, blank=True, null=True)  # Field name made lowercase.
    ingredients_type = models.CharField(db_column='ingredients_Type', max_length=45, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ingredients_details'


class MessIngredients(models.Model):
    quantity = models.FloatField(blank=True, null=True)
    price = models.FloatField(blank=True, null=True)
    purchace_date = models.DateField(db_column='purchace_Date', blank=True, null=True)  # Field name made lowercase.
    payment_status = models.CharField(db_column='payment_Status', max_length=3, blank=True, null=True)  # Field name made lowercase.
    ingredients_details_ingredient = models.ForeignKey(IngredientsDetails, models.DO_NOTHING, db_column='Ingredients_details_ingredient_Id', primary_key=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'mess_ingredients'


class Pyament(models.Model):
    transection_id = models.CharField(db_column='transection_Id', primary_key=True, max_length=20)  # Field name made lowercase.
    phase = models.IntegerField(db_column='Phase', blank=True, null=True)  # Field name made lowercase.
    pyment_date = models.DateField(db_column='pyment_Date', blank=True, null=True)  # Field name made lowercase.
    payment_status = models.CharField(db_column='payment_Status', max_length=3, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'pyament'


class Room(models.Model):
    room_id = models.CharField(db_column='room_Id', primary_key=True, max_length=20)  # Field name made lowercase.
    room_type = models.CharField(db_column='room_Type', max_length=20, blank=True, null=True)  # Field name made lowercase.
    capacity = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'room'


class Student(models.Model):
    studentid = models.AutoField(primary_key=True)
    password = models.CharField(max_length=10, blank=True, null=True)
    student_fname = models.CharField(db_column='student_Fname', max_length=45, blank=True, null=True)  # Field name made lowercase.
    student_mname = models.CharField(db_column='student_Mname', max_length=45, blank=True, null=True)  # Field name made lowercase.
    student_lname = models.CharField(db_column='student_Lname', max_length=45, blank=True, null=True)  # Field name made lowercase.
    dob = models.DateField(db_column='DOB', blank=True, null=True)  # Field name made lowercase.
    address = models.CharField(max_length=100, blank=True, null=True)
    email = models.CharField(max_length=30, blank=True, null=True)
    contactno = models.IntegerField(blank=True, null=True)
    registration_date = models.DateField(db_column='registration date', blank=True, null=True)  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = 'student'


class WeekMenu(models.Model):
    day = models.CharField(primary_key=True, max_length=10)
    breakfast = models.CharField(max_length=20, blank=True, null=True)
    lunch = models.CharField(max_length=45, blank=True, null=True)
    dinner = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'week_menu'
