from django.contrib import admin
from .models import Category


class CategoryAdmin(admin.ModelAdmin):
    # prepopulatedfld for auto filling slug with pdt name
    prepopulated_fields = {'slug': ('category_name',)}
    # listdisplay for what properties  to be listed in product listings
    list_display = ('category_name', 'slug')


admin.site.register(Category, CategoryAdmin)  # registering model to the admin
