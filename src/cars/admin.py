from django.contrib import admin
from cars.models import Cars



class CarsAdmin(admin.ModelAdmin):
    list_display                = ('cars_id','brand','model','year','condition','date_uploaded','seller')
    search_fields               = ('brand','model')
    readonly_fields             = ('date_uploaded',)

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()


admin.site.register(Cars,CarsAdmin)



