from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
     path('', views.tweet_list, name='tweet_list'),
     path('create/', views.tweet_create, name='tweet_create'),
     path('<int:tweet_id>/edit/', views.tweet_edit, name='tweet_edit'),
     path('<int:tweet_id>/delete/', views.tweet_delete, name='tweet_delete'),
     path('register/', views.register, name='register'),
] 
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)