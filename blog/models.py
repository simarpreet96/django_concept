from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext_lazy as _
from django.utils import timezone
from ckeditor.fields import RichTextField
# from django.contrib.auth import settings


class User(AbstractUser):
    id = models.AutoField(primary_key=True)
    email = models.EmailField(unique=True, null=True)
    username = models.CharField(max_length=30, unique=False)
    is_staff = models.BooleanField(_('staff status'), default=True)
    is_active = models.BooleanField(_('active'), default=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.email


class Post(models.Model):
    objects = None
    STATUS_CHOICES = [
        ('d', 'Draft'),
        ('p', 'Published'),
        ('w', 'Withdrawn'),
    ]
    id = models.AutoField(primary_key=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = RichTextField(blank=True)
    created_date = models.DateTimeField(default=timezone.now)
    # published_date = models.DateTimeField(blank=True, null=True)
    # image = models.ImageField(upload_to='images/',default='')
    status = models.CharField(max_length=1, choices=STATUS_CHOICES, default='')

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title


class Category(models.Model):
    objects = None
    id = models.AutoField(primary_key=True)
    categoryname = models.CharField(max_length=120)
    slug = models.SlugField(max_length=40)

    def __str__(self):
        return self.categoryname


class Store(models.Model):
    objects = None
    id = models.AutoField(primary_key=True)
    storename = models.CharField(max_length=120)
    storeaddress = models.CharField(max_length=200)

    def __str__(self):
        return self.storename


class Product(models.Model):
    objects = None
    id = models.AutoField(primary_key=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    # image = models.ImageField(upload_to='media/')
    price = models.IntegerField()
    description = models.TextField(max_length=500)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    store = models.ForeignKey(Store, on_delete=models.CASCADE)
    published=models.BooleanField(default=False)

    def __str__(self):
        return self.name


class Productimage (models.Model):
    objects = None
    id = models.AutoField(primary_key=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="product_images")
    image = models.ImageField(upload_to='media/', blank=True)

    def __str__(self):
        return f'{self.product.name} image'


class Cart(models.Model):
    objects = None
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    item = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    created = models.DateTimeField(auto_now_add=True)
    price = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.quantity} of {self.item.name}'

    def get_total(self):
        return self.item.price * self.quantity
        floattotal = float("{0:.2f}".format(total))
        return floattotal


class Order(models.Model):
    objects = None
    orderitems = models.ManyToManyField(Cart)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    ordered = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username

    def get_totals(self):
        total = 0
        for order_item in self.orderitems.all():
            total += order_item.get_total()
        return total

    def get_percentage(self):
        total = 0
        p = 0
        for order_item in self.orderitems.all():
            total += order_item.get_total()
            p = total * 0.08
            floattotal = float("{0:.2f}".format(p))
        return floattotal

    def all_total(self):
        total = 0
        p = 0
        for order_item in self.orderitems.all():
            total += order_item.get_total()
            p = total * 0.08 + total
            floattotal = float("{0:.2f}".format(p))
        return floattotal


class Wish(models.Model):
    item = models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)

    def __str__(self):
        return self.item.name

    def get_wish_total(self):
        return self.item.price * self.quantity
        floattotal = float("{0:.2f}".format(total))
        return floattotal


class BillingAddress(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    zipcode = models.CharField(max_length=50)
    city = models.CharField(max_length=30)
    landmark = models.CharField(max_length=20)

    def __str__(self):
        return f'{self.user.email} billing address'


# only one object will be created for this model as save method is override
class Origin(models.Model):
    objects = None
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)

    def save(self, *args, **kwargs):
        if self.__class__.objects.count():
            self.pk = self.__class__.objects.first().pk
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name
