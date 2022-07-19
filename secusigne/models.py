from itertools import product
from django.db import models
# Create your models here.
class Banner(models.Model):
    img = models.CharField(max_length=100)
    alt_text = models.CharField(max_length=200)

class Category(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='categories_images', blank=True)

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"

class Brand(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='brand_images', blank=True)

    def __str__(self):
        return self.title

class Color(models.Model):
    title = models.CharField(max_length=100)
    color_code = models.CharField(max_length=100)

    def __str__(self):
        return self.title

class Size(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title

class Product(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='products_images')
    slug = models.SlugField(max_length=200)
    detail = models.TextField()
    specs = models.TextField()
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    color = models.ForeignKey(Color, on_delete=models.CASCADE)
    size = models.ForeignKey(Size, on_delete=models.CASCADE)
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.title

class ProductAttribute(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    color = models.ForeignKey(Color, on_delete=models.CASCADE)
    size = models.ForeignKey(Size, on_delete=models.CASCADE)
    price = models.PositiveBigIntegerField()

    def __str__(self):
        return self.product.title