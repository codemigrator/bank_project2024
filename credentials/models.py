from django.db import models
from django.urls import reverse


class Register(models.Model):
    username = models.CharField(max_length=250, default=True)
    password = models.TextField()
    conform_password = models.TextField()

    def __str__(self):
        return self.username


class Districts(models.Model):
    name = models.CharField(max_length=250)


    def __str__(self):
        return self.name



class Branch(models.Model):
    district = models.ForeignKey(Districts, on_delete=models.CASCADE)
    name = models.CharField(max_length=250)

    def __str__(self):
        return self.name


class AccountType(models.Model):
    name = models.CharField(max_length=250)

    def __str__(self):
        return self.name





class FromTable(models.Model):
    name = models.CharField(max_length=50)
    date_of_birth = models.DateField(null=True,blank=True)
    age = models.PositiveIntegerField(null=True,blank=True)
    phone_number = models.CharField(max_length=20,blank=True)
    mail_id = models.EmailField(max_length=254,unique=True)
    address = models.TextField(blank=True)
    district = models.ForeignKey(Districts,on_delete=models.CASCADE)
    branch = models.ForeignKey(Branch,on_delete=models.CASCADE)
    account_type = models.ForeignKey(AccountType,on_delete=models.CASCADE)
    choices = models.ManyToManyField('CheckboxOptions', blank=True)


    def __str__(self):
        return self.name


class CheckboxOptions(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
