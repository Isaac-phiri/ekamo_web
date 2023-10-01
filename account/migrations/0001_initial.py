# Generated by Django 4.2.5 on 2023-10-01 17:51

import account.managers
from django.db import migrations, models
import django.db.models.deletion
import django_countries.fields
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='AgentType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('commission', models.CharField(blank=True, max_length=150, null=True)),
                ('salary', models.CharField(blank=True, max_length=150, null=True)),
                ('title', models.CharField(max_length=150)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='AgentProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=150)),
                ('last_name', models.CharField(max_length=150)),
                ('floatLimit', models.DecimalField(decimal_places=2, max_digits=100)),
                ('code', models.CharField(max_length=150)),
                ('phonenumber', models.CharField(max_length=150)),
                ('idtype', models.CharField(blank=True, choices=[('NRC', 'NRC'), ('Passport', 'Passport'), ('Drivers Lincense', 'Drivers Lincense')], max_length=300, verbose_name='id type')),
                ('idNo', models.CharField(blank=True, max_length=300, verbose_name='ID Type')),
                ('id_front', models.ImageField(blank=True, null=True, upload_to='id_front/')),
                ('id_back', models.ImageField(blank=True, null=True, upload_to='id_back/')),
                ('dob', models.DateField(auto_now=True)),
                ('province', models.CharField(blank=True, max_length=50, null=True, verbose_name='province')),
                ('district', models.CharField(blank=True, max_length=50, null=True, verbose_name='district')),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('agent_type', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='account.agenttype')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('idtype', models.CharField(blank=True, choices=[('NRC', 'NRC'), ('Passport', 'Passport'), ('Drivers Lincense', 'Drivers Lincense')], max_length=300, verbose_name='id type')),
                ('idNo', models.CharField(blank=True, max_length=300, verbose_name='ID Type')),
                ('id_front', models.ImageField(blank=True, null=True, upload_to='id_front/')),
                ('id_back', models.ImageField(blank=True, null=True, upload_to='id_back/')),
                ('code', models.CharField(max_length=150)),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='email address')),
                ('first_name', models.CharField(blank=True, max_length=30, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=30, verbose_name='last name')),
                ('phone', phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, region=None)),
                ('dob', models.DateField(auto_now=True)),
                ('province', models.CharField(blank=True, max_length=50, verbose_name='province')),
                ('district', models.CharField(blank=True, max_length=50, verbose_name='district')),
                ('country', django_countries.fields.CountryField(blank=True, max_length=2)),
                ('is_staff', models.BooleanField(default=False, verbose_name='staff')),
                ('date_joined', models.DateTimeField(auto_now_add=True, verbose_name='date joined')),
                ('is_active', models.BooleanField(default=True, verbose_name='active')),
                ('is_verified', models.BooleanField(default=False, verbose_name='verified')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
            },
            managers=[
                ('objects', account.managers.UserManager()),
            ],
        ),
    ]
