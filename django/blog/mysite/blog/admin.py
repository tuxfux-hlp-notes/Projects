from django.contrib import admin
from models import BlogPost

# Register your models here.

#admin.site.register(BlogPost)

class BlogPostAdmin(admin.ModelAdmin):
  list_display = ('title','timestamp')

admin.site.register(BlogPost, BlogPostAdmin)
