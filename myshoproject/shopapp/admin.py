from django.contrib import admin
from .models import user,product,catagry,order
# Register your models here.


class adminproduct(admin.ModelAdmin):
    list_display=['product_name','price','Catagry']

class admincatagry(admin.ModelAdmin):
    list_display=['name']

admin.site.register(user)
admin.site.register(product,adminproduct)
admin.site.register(catagry,admincatagry)
admin.site.register(order)