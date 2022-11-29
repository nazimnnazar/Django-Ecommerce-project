from django.db import models
from django.urls import reverse
# Create your models here.
class Categ(models.Model):
    name=models.CharField(max_length=250,unique=True)
    slug=models.SlugField(max_length=250,unique=True)

    class meta:
        ordering=['name',]
        verbose_name= 'category'
        verbose_name=plural='categories'
    def get_url(self):
        return reverse('product', args=[self.slug])
        
    def get_url(self):
        return reverse('product', args=[self.slug])

class Product(models.Model):
    name=models.CharField(max_length=250,unique=True)
    slug=models.SlugField(max_length=250,unique=True)
    img=models.ImageField(upload_to='product')
    desc=models.TextField()
    stock=models.IntegerField()
    available=models.BooleanField()
    price=models.IntegerField()
    category=models.ForeignKey(Categ,on_delete=models.CASCADE)

    def get_url(self):
        return reverse('view_details',args=[self.category.slug,self.slug])    

    def __str__(self):
        return '{}'.format(self.name) 