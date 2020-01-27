from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


# Create your models here.

# Items to hold sharing contents in the lobby
class BulletItem(models.Model):
    poster = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    book_title = models.CharField(max_length=200)
    description = models.CharField(max_length=1000)
    likes = models.IntegerField(default=0)

    def get_book_url(self):
        """Returns the url to the detail page of the book"""
        # return reverse('book-detail', args=[str(self.id)])
    def __str__(self):
        return self.book_title + '--' + self.poster.username


# Each user comment toward a certain share
class BulletComment(models.Model):
    bullet_item = models.ForeignKey(BulletItem, on_delete=models.CASCADE)
    content = models.CharField(max_length=1000, help_text='Post a comment on the share')
    commenter = models.ForeignKey(User, on_delete=models.DO_NOTHING)


class BookCollections(models.Model):
    book_title = models.CharField(max_length=200, default='')
    isbn = models.CharField(max_length=20, default='')
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    onPage = models.IntegerField(default=0)
    totalPage = models.IntegerField(default=1)
    percentage = models.IntegerField(default=0)


# class CollectionComments(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     collection = models.ForeignKey(BookCollections, on_delete=models.CASCADE)
#     content = models.TextField(help_text='Post a comment')


# class ReadingStatus(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     collection = models.ForeignKey(BookCollections, on_delete=models.CASCADE)
#
