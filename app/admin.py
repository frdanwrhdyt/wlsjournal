from django.contrib import admin
from app.models import *

# class BusinessTypeAdmin(admin.ModelAdmin):
#     list_display = ('id', 'name')

class UserBusinessAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'user_id', 'created_at', 'updated_at')

class PurchaseProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'qty', 'price', 'user_business_id', 'created_at', 'updated_at')

class SellingProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'hpp', 'price', 'user_business_id', 'created_at', 'updated_at',)

class CustomerAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'user_business_id', 'created_at', 'updated_at',)

class PaymentTypeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'user_business_id', 'created_at', 'updated_at',)

class InvoiceAdmin(admin.ModelAdmin):
    list_display = ('id', 'invoice_num', 'copy_num', 'status', 'customer_id', 'payment_type_id', 'created_at', 'updated_at',)

class OrderAdmin(admin.ModelAdmin):
    list_display = ('id','invoice_num_id', 'selling_product_id', 'amount', 'created_at', 'updated_at')

admin.site.register(UserBusiness, UserBusinessAdmin)
admin.site.register(PurchaseProduct, PurchaseProductAdmin)
admin.site.register(SellingProduct, SellingProductAdmin)
admin.site.register(Customer, CustomerAdmin)
admin.site.register(PaymentType, PaymentTypeAdmin)
admin.site.register(Invoice, InvoiceAdmin)
admin.site.register(Order, OrderAdmin)