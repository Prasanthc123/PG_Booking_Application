from django.db import models

# Create your models here.
class Pgs(models.Model):
    pg_name=models.CharField(max_length=100)
    pg_address=models.CharField(max_length=500)
    pg_pic=models.ImageField(default='ntr.jpg')
    pg_cost=models.IntegerField()

    def __str__(self):
        return self.pg_name

class Booking(models.Model):
    pg_name=models.OneToOneField(Pgs,on_delete=models.CASCADE)
    customer=models.CharField(max_length=100)
    age=models.IntegerField()
    option_menu=(('Male','Male'),('Female','Female'))
    gender = models.CharField(max_length=200, choices=option_menu)
    option_menu1=(('Student','Student'),('Job','Job'))
    profession=models.CharField(max_length=300,choices=option_menu1)
    phone_number=models.CharField(max_length=20)
    address=models.TextField()
    district=models.CharField(max_length=50)
    state=models.CharField(max_length=100)
    Adhar_card=models.FileField()
    Photo=models.ImageField()

class Payment(models.Model):
    amount=models.IntegerField()
    