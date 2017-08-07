# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models her
class Slider(models.Model):
    title = models.CharField('標題', max_length=50)
    content = models.CharField('內容', max_length=100)

    def __str__(self):
        return self.title

    def __save__(self,*args, **kwargs):
        if self.title:
            self.title_stripped = strip_tags(self.title)

        if self.content:
            self.content_stripped = strip_tags(self.content)

        super(Slider, self).save(*args, **kwargs)

    class Meta:
        db_table = 'slider'
        verbose_name = '首頁滑塊'
        verbose_name_plural = '首頁滑塊'

class About(models.Model):
    title = models.CharField('標題', max_length=50)
    content = models.TextField('內容')

    def __str__(self):
        return self.title

    def __save__(self,*args, **kwargs):
        if self.title:
            self.title_stripped = strip_tags(self.title)

        if self.content:
            self.content_stripped = strip_tags(self.content)

        super(About, self).save(*args, **kwargs)

    class Meta:
        db_table = 'about'
        verbose_name = '關於聖森'
        verbose_name_plural = '關於聖森'

class Management_Philosophy(models.Model):
    title = models.CharField('標題', max_length=50)
    content = models.TextField('內容')

    def __str__(self):
        return self.title

    def __save__(self,*args, **kwargs):
        if self.title:
            self.title_stripped = strip_tags(self.title)

        if self.content:
            self.content_stripped = strip_tags(self.content)

        super(Management_Philosophy, self).save(*args, **kwargs)

    class Meta:
        db_table = 'management_philosophy'
        verbose_name = '經營理念'
        verbose_name_plural = '經營理念'

class Partner(models.Model):
    logo = models.ImageField('圖示', upload_to='./', default = './no-profile-pic-img.gif')
    title = models.CharField('標題', max_length=50)
    url = models.URLField('網址', max_length=200)

    def __str__(self):
        return self.title

    def __save__(self,*args, **kwargs):
        if self.logo:
            self.logo_stripped = strip_tags(self.logo)

        if self.title:
            self.title_stripped = strip_tags(self.title)

        if self.url:
            self.url_stripped = strip_tags(self.url)

        super(Partner, self).save(*args, **kwargs)

    class Meta:
        db_table = 'partner'
        verbose_name = '合作伙伴'
        verbose_name_plural = '合作伙伴'

class Contact(models.Model):
    name = models.CharField('姓名', max_length=20)
    email = models.EmailField('信箱', max_length=200)
    url = models.URLField('網址', max_length=200, null=True, blank=True)
    message = models.TextField('訊息')

    def __str__(self):
        return self.name

    def __save__(self,*args, **kwargs):
        if self.name:
            self.name_stripped = strip_tags(self.name)

        if self.email:
            self.email_stripped = strip_tags(self.email)

        if self.url:
            self.url_stripped = strip_tags(self.url)

        if self.message:
            self.message_stripped = strip_tags(self.message)

        super(Partner, self).save(*args, **kwargs)

    class Meta:
        db_table = 'contact'
        verbose_name = '聯絡我們'
        verbose_name_plural = '聯絡我們'

class Company(models.Model):
    name = models.CharField('公司名', max_length=20)
    zipcode = models.IntegerField('郵遞區號', default=0)
    address = models.CharField('地址', max_length=200)

    def __str__(self):
        return self.name

    def __save__(self,*args, **kwargs):
        if self.name:
            self.name_stripped = strip_tags(self.name)

        if self.address:
            self.address_stripped = strip_tags(self.address)

        super(Company, self).save(*args, **kwargs)

    class Meta:
        db_table = 'company'
        verbose_name = '公司資訊'
        verbose_name_plural = '公司資訊'
