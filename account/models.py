from django.shortcuts import render
from django.db import models

class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
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
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


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
    id = models.BigAutoField(primary_key=True)
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


class ItemDb(models.Model):
    item_number = models.IntegerField(db_column='Item_number', primary_key=True)  # Field name made lowercase.
    number_category = models.IntegerField(db_column='Number_category')  # Field name made lowercase.
    item_name = models.CharField(db_column='Item_name', max_length=45)  # Field name made lowercase.
    item_content = models.CharField(db_column='Item_content', max_length=45)  # Field name made lowercase.
    item_precautions = models.CharField(db_column='Item_precautions', max_length=45)  # Field name made lowercase.
    item_image = models.CharField(db_column='Item_image', max_length=45)  # Field name made lowercase.
    item_location = models.CharField(db_column='Item_location', max_length=45)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'item_db'


class ReviewDb(models.Model):
    review_number = models.IntegerField(db_column='Review_number', primary_key=True)  # Field name made lowercase.
    review_score = models.FloatField(db_column='Review_score')  # Field name made lowercase.
    review_content = models.CharField(db_column='Review_content', max_length=45)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'review_db'


class UserDb(models.Model):
    user_number = models.IntegerField(db_column='User_number', primary_key=True)  # Field name made lowercase.
    user_id = models.IntegerField(db_column='User_id')  # Field name made lowercase.
    user_password = models.IntegerField(db_column='User_password')  # Field name made lowercase.
    user_name = models.CharField(db_column='User_name', max_length=45)  # Field name made lowercase.
    user_phonenumber = models.CharField(db_column='User_phonenumber', max_length=45)  # Field name made lowercase.
    user_birth = models.DateField(db_column='User_birth')  # Field name made lowercase.
    user_joindate = models.DateField(db_column='User_joindate')  # Field name made lowercase.
    user_rate = models.FloatField(db_column='User_rate')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'user_db'
        unique_together = (('user_number', 'user_id'),)

