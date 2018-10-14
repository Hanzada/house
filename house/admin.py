from django.contrib import admin
from .models import House,City
class HouseAdmin(admin.ModelAdmin):
    list_display = ['name','price']
    fieldsets = (
        ('Продавец',{'fields':('avtor','phone'

                               )}),(
            'Квартира',{'fields':('name','description','price','image','size','count_room','all_floor','current_floor','balcony'
                                  )}),(
            'Адрес',{'fields':('city','adress','urlmap'

        )})
    )
class CityAdmin(admin.ModelAdmin):
     list_display = ['name']
     prepopulated_fields = {'slug': ['name']}
admin.site.register(House,HouseAdmin)
admin.site.register(City,CityAdmin)
# Register your models here.
