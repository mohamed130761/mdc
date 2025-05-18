from django.db import models

class Network(models.Model):
    governorate = models.CharField(max_length=100, verbose_name='Governorate')
    area = models.CharField(max_length=100,null=True, verbose_name='Area')
    type = models.CharField(max_length=100, verbose_name='Type')
    speciality = models.CharField(max_length=255, verbose_name='Speciality')
    provider = models.CharField(max_length=255, verbose_name='Provider')
    discount = models.CharField(max_length=50, blank=True, null=True, verbose_name='Discount')
    address = models.TextField(verbose_name='Address')
    phone = models.CharField(max_length=100, verbose_name='Phone')
    website = models.URLField(blank=True, null=True, verbose_name='Website')
    email = models.EmailField(blank=True, null=True, verbose_name='Email Address')
    notes = models.TextField(blank=True, null=True, verbose_name='Notes')

    def __str__(self):
        return f"{self.provider} - {self.type} - {self.area}"


class Networkeds(models.Model):
    governorate = models.CharField(max_length=100, verbose_name='Governorate')
    area = models.CharField(max_length=100,null=True, verbose_name='Area')
    type = models.CharField(max_length=100, verbose_name='Type')
    speciality = models.CharField(max_length=255, verbose_name='Speciality')
    provider = models.CharField(max_length=255, verbose_name='Provider')
    address = models.TextField(verbose_name='Address')
    phone = models.CharField(max_length=100, verbose_name='Phone')
    website = models.URLField(blank=True, null=True, verbose_name='Website')
    email = models.EmailField(blank=True, null=True, verbose_name='Email Address')
    notes = models.TextField(blank=True, null=True, verbose_name='Notes')

    def __str__(self):
        return f"{self.provider} - {self.type} - {self.area}"

class Networkmofa(models.Model):
    governorate = models.CharField(max_length=100, verbose_name='Governorate')
    area = models.CharField(max_length=100,null=True, verbose_name='Area')
    type = models.CharField(max_length=100, verbose_name='Type')
    speciality = models.CharField(max_length=255, verbose_name='Speciality')
    provider = models.CharField(max_length=255, verbose_name='Provider')
    address = models.TextField(verbose_name='Address')
    phone = models.CharField(max_length=100, verbose_name='Phone')
    website = models.URLField(blank=True, null=True, verbose_name='Website')
    email = models.EmailField(blank=True, null=True, verbose_name='Email Address')
    notes = models.TextField(blank=True, null=True, verbose_name='Notes')

    def __str__(self):
        return f"{self.provider} - {self.type} - {self.area}"

class Networkexxon(models.Model):
    governorate = models.CharField(max_length=100, verbose_name='Governorate')
    area = models.CharField(max_length=100,null=True, verbose_name='Area')
    type = models.CharField(max_length=100, verbose_name='Type')
    speciality = models.CharField(max_length=255, verbose_name='Speciality')
    provider = models.CharField(max_length=255, verbose_name='Provider')
    address = models.TextField(verbose_name='Address')
    phone = models.CharField(max_length=100, verbose_name='Phone')
    website = models.URLField(blank=True, null=True, verbose_name='Website')
    email = models.EmailField(blank=True, null=True, verbose_name='Email Address')
    notes = models.TextField(blank=True, null=True, verbose_name='Notes')

    def __str__(self):
        return f"{self.provider} - {self.type} - {self.area}"

class Networkemfa(models.Model):
    governorate = models.CharField(max_length=100, verbose_name='Governorate')
    area = models.CharField(max_length=100,null=True, verbose_name='Area')
    type = models.CharField(max_length=100, verbose_name='Type')
    speciality = models.CharField(max_length=255, verbose_name='Speciality')
    provider = models.CharField(max_length=255, verbose_name='Provider')
    address = models.TextField(verbose_name='Address')
    phone = models.CharField(max_length=100, verbose_name='Phone')
    website = models.URLField(blank=True, null=True, verbose_name='Website')
    email = models.EmailField(blank=True, null=True, verbose_name='Email Address')
    notes = models.TextField(blank=True, null=True, verbose_name='Notes')

    def __str__(self):
        return f"{self.provider} - {self.type} - {self.area}"


class Networkhorizon(models.Model):
    governorate = models.CharField(max_length=100, verbose_name='Governorate')
    area = models.CharField(max_length=100, null=True, verbose_name='Area')
    type = models.CharField(max_length=100, verbose_name='Type')
    speciality = models.CharField(max_length=255, verbose_name='Speciality')
    provider = models.CharField(max_length=255, verbose_name='Provider')
    address = models.TextField(verbose_name='Address')
    phone = models.CharField(max_length=100, verbose_name='Phone')
    website = models.URLField(blank=True, null=True, verbose_name='Website')
    email = models.EmailField(blank=True, null=True, verbose_name='Email Address')
    notes = models.TextField(blank=True, null=True, verbose_name='Notes')

    def __str__(self):
        return f"{self.provider} - {self.type} - {self.area}"