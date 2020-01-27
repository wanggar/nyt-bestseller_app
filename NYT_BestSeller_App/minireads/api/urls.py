from django.urls import path
from . import views

app_name = 'api'
urlpatterns = [
    path('', views.index, name='index'),
    path('non-fiction/', views.non_fiction, name='non_fiction'),
    path('culture/', views.culture, name='culture'),
    path('education/', views.education, name='education'),
    path('family/', views.family, name='family'),
    path('humor/', views.humor, name='humor'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('collection/', views.collection, name='collection'),
    path('detail/<str:book_title>/<str:isbn_13>/', views.detail, name='detail'),
    path('detail/<str:book_title>/<str:isbn_13>/save/', views.save, name='save'),
    path('comment/<str:book_title>/<int:bullet_item_id>/', views.comment, name='comment'),
    path('comment/<str:book_title>/<int:bullet_item_id>/post/', views.post_comment, name='post_comment'),
    path('dashboard/like/<int:bullet_item_id>/', views.like, name='like'),
]
