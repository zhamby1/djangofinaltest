from datetime import datetime
from unicodedata import category
from django.db import models
from django.utils import timezone

# Create your models here.




class Book(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.TextField()
    author = models.TextField()
    publisher = models.TextField()
    pub_date = models.DateField()
    price = models.FloatField(default=0)

    def __str__(self):
        return self.title
    
class Sales(models.Model):
    code = models.CharField(max_length=100)
    sub_total = models.FloatField(default=0)
    grand_total = models.FloatField(default=0)
    tax_amount = models.FloatField(default=0)
    tax = models.FloatField(default=0)
    tendered_amount = models.FloatField(default=0)
    amount_change = models.FloatField(default=0)
    date_added = models.DateTimeField(default=timezone.now) 

    def __str__(self):
        return self.name
    
class salesItems(models.Model):
    sale_id = models.ForeignKey(Sales,on_delete=models.CASCADE)
    book_id = models.ForeignKey(Book,on_delete=models.CASCADE)
    price = models.FloatField(default=0)
    qty = models.FloatField(default=0)
    total = models.FloatField(default=0)


#need to fix this, need to be able to pull just one item 
class Returns(models.Model):
    code = models.CharField(max_length=100)
    sub_total = models.FloatField(default=0)
    grand_total = models.FloatField(default=0)
    tax_amount = models.FloatField(default=0)
    tax = models.FloatField(default=0)
    tendered_amount = models.FloatField(default=0)
    amount_change = models.FloatField(default=0)
    date_added = models.DateTimeField(default=timezone.now) 
