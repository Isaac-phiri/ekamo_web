from __future__ import unicode_literals
from django.db import models
from django.core.mail import send_mail
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.base_user import AbstractBaseUser
from django.urls import reverse
from django_countries.fields import CountryField
from phonenumber_field.modelfields import PhoneNumberField

from .managers import UserManager

class AgentType(models.Model): #get
    commission = models.CharField(max_length = 150, blank=True,null=True)
    salary = models.CharField(max_length = 150, blank=True,null=True)
    title = models.CharField(max_length = 150)
    timestamp = models.DateTimeField(auto_now_add=True)
    updated  = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.title} - {self.commission}'

class AgentProfile(models.Model):  #get  #post
    ID_TYPE = (
          ('NRC', 'NRC'),
          ('Passport', 'Passport'),
          ('Drivers Lincense', 'Drivers Lincense'),
    )
    first_name = models.CharField(max_length = 150)
    last_name = models.CharField(max_length = 150)
    floatLimit  = models.DecimalField(max_digits=100, decimal_places=2)
    code = models.CharField(max_length = 150)
    phonenumber = models.CharField(max_length = 150)
    agent_type = models.ForeignKey(AgentType, on_delete=models.CASCADE, default=None, blank=True,null=True)
    idtype = models.CharField(choices= ID_TYPE,verbose_name='id type', max_length=300, blank=True)
    idNo = models.CharField(verbose_name='ID Type', max_length=300,blank=True )
    id_front = models.ImageField(upload_to='id_front/', null=True, blank=True)
    id_back = models.ImageField(upload_to='id_back/', null=True, blank=True)
    dob = models.DateField(auto_now=True, blank=True)
    province = models.CharField(verbose_name='province', max_length=50, blank=True,null=True)
    district = models.CharField(verbose_name='district', max_length=50, blank=True,null=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    updated  = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.first_name}'
    

class User(AbstractBaseUser, PermissionsMixin):  #get 
    ID_TYPE = (
          ('NRC', 'NRC'),
          ('Passport', 'Passport'),
          ('Drivers Lincense', 'Drivers Lincense'),
    )
    ROLE = (
          ('CRM', 'CRM'),
          ('Manager', 'Manager'),
          ('Agent Manager', 'Agent Manager'),
    )
    idtype = models.CharField(choices= ID_TYPE,verbose_name='id type', max_length=300, blank=True)
    idNo = models.CharField(verbose_name='ID Type', max_length=300,blank=True )
    id_front = models.ImageField(upload_to='id_front/', null=True, blank=True)
    id_back = models.ImageField(upload_to='id_back/', null=True, blank=True)
    code = models.CharField(max_length = 150)
    email = models.EmailField(verbose_name='email address', unique=True)
    first_name = models.CharField(
        verbose_name='first name', max_length=30, blank=True)
    last_name = models.CharField(verbose_name='last name', max_length=30, blank=True)
    phone = PhoneNumberField(blank=True)
    dob = models.DateField(auto_now=True, blank=True)
    province = models.CharField(verbose_name='province', max_length=50, blank=True)
    district = models.CharField(verbose_name='district', max_length=50, blank=True)
    country = CountryField(blank_label='(select country)', blank=True)
    is_staff = models.BooleanField(verbose_name='staff', default=False)
    date_joined = models.DateTimeField(verbose_name='date joined', auto_now_add=True)
    is_active = models.BooleanField(verbose_name='active', default=True)
    is_verified = models.BooleanField(verbose_name='verified', default=False)
  
    # agents_to_manage = models.ManyToManyField(AgentProfile, verbose_name="Agents To Manage", null=True, blank=True)
    # 
    objects = UserManager()
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = 'user'
        verbose_name_plural = 'users'
        
    def get_status(self):
        if self.is_active:
            return 'Active'
        return 'Not Active'

    def get_full_name(self):
        '''
        Returns the first_name plus the last_name, with a space in between.
        '''
        full_name = '%s %s' % (self.first_name, self.last_name)
        return full_name.strip()

    def get_short_name(self):
        '''
        Returns the short name for the user.
        '''
        return self.first_name

    def email_user(self, subject, message, from_email=None, **kwargs):
        '''
        Sends an email to this User.
        '''
        print(subject, message, from_email,)
        # send_mail(subject, message, from_email, [self.email], **kwargs)
    
    # def get_absolute_url(self):
    #     return reverse('account:profile', args=[self.pk])

    # def get_edit_url(self):
    #     return reverse('account:profile-edit', args=[self.pk])
    
    # def get_soil_url(self):
    #     return reverse('account:soil',args=[self.pk])
    


 