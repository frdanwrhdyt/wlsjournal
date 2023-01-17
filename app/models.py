from django.db import models
from users.models import User

class UserBusiness (models.Model):
    name = models.CharField(max_length=200)
    location = models.TextField()
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    tax = models.IntegerField( default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-name', ]


class PurchaseProduct (models.Model):
    name = models.CharField(max_length=200)
    qty = models.CharField(max_length=200)
    price = models.CharField(max_length=200)
    user_business_id = models.ForeignKey(UserBusiness, on_delete=models.CASCADE)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-name', ]

class SellingProduct(models.Model):
    name = models.CharField(max_length=200)
    hpp = models.CharField(max_length=200)
    price = models.CharField(max_length=200)
    user_business_id = models.ForeignKey(UserBusiness, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-name', ]

class Customer(models.Model):
    name = models.CharField(max_length=200, unique=False)
    user_business_id = models.ForeignKey(UserBusiness, on_delete=models.DO_NOTHING)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-name', ]

class PaymentType(models.Model):
    name = models.CharField(max_length=200)
    user_business_id = models.ForeignKey(UserBusiness, on_delete=models.DO_NOTHING)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.name

    
    class Meta:
        ordering = ['-name', ]

class Invoice(models.Model):
    invoice_num = models.CharField(max_length=200)
    status = models.BooleanField(default=False)
    payment_type_id = models.ForeignKey(PaymentType, on_delete=models.DO_NOTHING)
    customer_id = models.ForeignKey(Customer, on_delete=models.DO_NOTHING)
    copy_num = models.IntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.invoice_num)
    class Meta:
        ordering = ['-invoice_num',]
class Order(models.Model):
    invoice_num_id = models.ForeignKey(Invoice, on_delete=models.CASCADE)
    selling_product_id = models.ForeignKey(SellingProduct, on_delete=models.CASCADE)
    amount = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # def save(self, *args, **kwargs):
    #     super(Order, self).save(*args, **kwargs)
    
    def __str__(self):
        return str(self.invoice_num_id)

    class Meta:
        ordering = ['-invoice_num_id', ]
