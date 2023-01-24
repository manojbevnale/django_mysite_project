from django.contrib import admin
from .models import Service,About,Contact
# Register your models here.
class ServicesDetail(admin.ModelAdmin):
    list_display=['title','description','image']
admin.site.register(Service,ServicesDetail)


class AboutDetail(admin.ModelAdmin):
    list_display=['title','description','image']
admin.site.register(About,AboutDetail)


class ContactForm(admin.ModelAdmin):
    list_display=['name','email','message','number']
admin.site.register(Contact,ContactForm)    