from django.contrib import admin
from .models import BulletItem, BulletComment
from .models import BookCollections


# Register your models here.
@admin.register(BulletItem)
class BulletItemAdmin(admin.ModelAdmin):
    list_display = ('book_title', 'poster', 'description', 'likes')


@admin.register(BulletComment)
class BulletCommentAdmin(admin.ModelAdmin):
    list_display = ('bullet_item', 'content', 'commenter')


@admin.register(BookCollections)
class BookCollectionsAdmin(admin.ModelAdmin):
    list_display = ('book_title', 'isbn', 'user')
