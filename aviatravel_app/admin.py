from django.contrib import admin
from aviatravel_app.models import( 
        TravelTicket,
        Country,
        City,
        Images,
        Category
    )

class ImagesAdmin(admin.TabularInline):
    model = Images
    extra = 2

class TravelTicketAdmin(admin.ModelAdmin):
    prepopulated_fields = {
        'slug': ('title',),
    }

    inlines = [ImagesAdmin]

class CountryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}

class CityAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}

admin.site.register(TravelTicket, TravelTicketAdmin)
admin.site.register(Country, CountryAdmin)
admin.site.register(City, CityAdmin)
admin.site.register(Category, CategoryAdmin)
