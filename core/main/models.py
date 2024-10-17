from django.db import models

# Create your models here.

class slider(models.Model):

    name = models.CharField('Hndik name',max_length=250)
    name1 = models.CharField('Hndik name',max_length=250)
    img = models.ImageField('Hndik image',upload_to='hndik/')
    text = models.TextField('Hndik text')
    
    def str(self) -> str:
        return self.name

class product(models.Model):

    img = models.ImageField('Product image',upload_to='product/')
    prod_name = models.CharField('Prod name',max_length=250)
    new = models.BooleanField('Active')
    price = models.BigIntegerField('Prod price')

    def __str__(self) -> str:
        return self.prod_name
    
class about(models.Model):

    img = models.ImageField('Aboout image',upload_to='about/')
    name = models.CharField('About name',max_length=250)
    text = models.TextField('About text')
    but_name = models.CharField('Button name',max_length=250)

    def __str__(self) -> str:
        return self.name

class offer(models.Model):

    img = models.ImageField('Offer image',upload_to='offer/')
    name = models.CharField('Upto',max_length=250)

    def __str__(self) -> str:
        return self.name
    
class offer_s(models.Model):

    img = models.ImageField('Offer image',upload_to='offer/')
    name = models.CharField('Upto',max_length=250)

    def __str__(self) -> str:
        return self.name
    
class blog(models.Model):

    img = models.ImageField('Blog image',upload_to='blog/')
    name = models.CharField('Mounth',max_length=250)
    name1 = models.CharField('Date',max_length=250,default='SOME STRING')
    title = models.CharField('Blog title',max_length=250)
    text = models.TextField('Blog text')
    
    def __str__(self) -> str:
        return self.name
    
class client(models.Model):

    img = models.ImageField('Client image',upload_to='client/')
    name = models.CharField('Client name',max_length=250)
    text = models.TextField('Client text')

    def __str__(self) -> str:
        return self.name