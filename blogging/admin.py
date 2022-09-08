from django.contrib import admin
from blogging.models import Post, Category

#
# Admin registrations
#

class CategoriesInline(admin.TabularInline):
    model = Category.posts.through

class CategoryAdmin(admin.ModelAdmin):
    model = Category
    fields = ("name", "description")

class PostAdmin(admin.ModelAdmin):
    model = Post
    inlines = [CategoriesInline]

admin.site.register(Category, CategoryAdmin)
admin.site.register(Post, PostAdmin)
