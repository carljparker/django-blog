from django.contrib import admin
from blogging.models import Post, Category

# Admin registrations
admin.site.register(Post)

@admin.register(Category)
class CategoryAdmin( admin.ModelAdmin ):
    fields  = ( 'name', 'description' )

