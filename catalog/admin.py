from django.contrib import admin
from . import models
@admin.register(models.Gener)
class generadmin(admin.ModelAdmin):
    list_display=['name']



@admin.register(models.Bookinstance)
class bookinstanceadmin(admin.ModelAdmin):
    list_filter=('due_back','status','borrower')
    fieldsets=(('book:',{'fields':('book','id')}),
               ('availablity:',{'fields':('due_back','status','borrower')})

    )
    

class bookinstanceininline(admin.TabularInline):

    model=models.Bookinstance


@admin.register(models.Book)
class bookadmin(admin.ModelAdmin):
     inlines=[bookinstanceininline]
     list_display=['title','author','display_gener']


@admin.register(models.Author)
class authoradmin(admin.ModelAdmin):

    list_display=['name','last_name','date_of_birth','date_of_death']
    fields=['name','last_name',('date_of_birth','date_of_death')]





