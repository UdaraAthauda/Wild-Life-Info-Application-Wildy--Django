from django.contrib import admin
from .models import *
from blogs.models import BlogPost

admin.site.register(Region)

class VenomTypeAdmin(admin.ModelAdmin):
    list_display = ('name', 'venom_type_translation')

admin.site.register(VenomType, VenomTypeAdmin)

admin.site.register(Snake)

# blog post inlines 
class BlogPostInline(admin.StackedInline):
    model = BlogPost
    extra = 0

# extendet Snake model
class SnakeAdmin(admin.ModelAdmin):
    model = Snake
    inlines = [BlogPostInline]

admin.site.unregister(Snake)

admin.site.register(Snake, SnakeAdmin)