from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.contrib.auth.models import AbstractUser


class Users(AbstractUser):
    about = models.TextField()
    image = models.ImageField(upload_to='users/', blank=True, null=True)
    address = models.CharField(max_length=500)


class BaseCreateModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True



class Category(BaseCreateModel):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name



class Brand(BaseCreateModel):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name



class Size(BaseCreateModel):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name



class Color(BaseCreateModel):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=25)

    def __str__(self):
        return self.name



class Tags(BaseCreateModel):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name




class Product(BaseCreateModel):
    name = models.CharField(max_length=100)
    price = models.DecimalField(decimal_places=2, max_digits=10)
    rating = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    discount = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(100)])
    text = models.TextField()
    image = models.ImageField(upload_to="images/")
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, blank=True, null=True)
    size = models.ManyToManyField(Size, blank=True, null=True)
    color = models.ManyToManyField(Color, blank=True, null=True)
    tags = models.ManyToManyField(Tags, blank=True, null=True)

    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ['-created_at']




class ProductImage(BaseCreateModel):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to="images/")

    def __str__(self):
        return self.product.name
    

class Banner(BaseCreateModel):
    name = models.CharField(max_length=25)
    title = models.CharField(max_length=50)
    about = models.TextField()
    image = models.ImageField(upload_to='banners/')
    status = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class Blog(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='blogs')
    about = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=False)

    def __str__(self):
        return self.title


class Contact(models.Model):
    name = models.CharField(max_length=25)
    email = models.EmailField()
    message = models.TextField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Fikir'
        verbose_name_plural = 'Fikirlar'


class ShoppingCart(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.ForeignKey(Users, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username



