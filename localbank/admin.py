from django.contrib import admin

from .models import Bankitem
# Register your models here.

# admin.site.register(Bankitem)

# Define the admin class
class BankitemAdmin(admin.ModelAdmin):
    list_display = ('bankItemName', 'bankItemPrice', 'belongsto')
 # bankItemName = models.CharField(max_length=200)
 #    itemAquiredOn = models.DateTimeField(auto_now_add=False)
 #    bankitemDescription = models.TextField(max_length=1000, help_text='Enter a brief description of the book')
 #    bankItemPrice 

# Register the admin class with the associated model
admin.site.register(Bankitem, BankitemAdmin)
