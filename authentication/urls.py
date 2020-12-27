from django.urls import path
from . import views
from forum import views as forumviews

urlpatterns = [
    path('', views.index, name='index'),
    path('home/', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('logout/', views.logout_view, name='logout'),
    path('forum/', forumviews.index, name='forumview'),
]
