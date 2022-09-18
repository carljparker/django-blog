from django.contrib import admin
from blogging.models import Post, Category

#
# Admin registrations
#


class CategoriesInline(admin.TabularInline):
    model = Category.posts.through


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    fields = ("name", "description")


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    inlines = [CategoriesInline]
