from django.contrib import admin

# Register your models here.
# reference: https://docs.djangoproject.com/en/1.11/ref/contrib/admin/
from .models import Product,Category
from .forms import ProductAdminForm

class ProductAdmin(admin.ModelAdmin):
	form = ProductAdminForm

	# sets values for how the admin suit lists your products
	list_display = ('name','price','old_price','created_at','updated_at',)
	list_display_links = ('name',)
	list_per_page = 50
	ordering = ['-created_at']
	search_fields = ['name','description','meta_keywords','meta_description']
	exclude = ('created_at','updated_at',)

	# sets up slug to generated the product name
	prepopulated_fields = {'slug':('name',)}

admin.site.register(Product,ProductAdmin)

class CategoryAdmin(admin.ModelAdmin):
	# sets up values for how admin site lists categories
	list_display = ('name','created_at','updated_at',)
	list_display_links = ('name',)
	list_per_page = 20
	ordering = ['name']
	search_fields = ['name','description','meta_keywords','meta_description']
	exclude = ('created_at','updated_at',)

	# sets up slug to be generated from category name
	prepopulated_fields = {'slug':('name',)}

admin.site.register(Category, CategoryAdmin)