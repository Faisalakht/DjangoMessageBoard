from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='forumlist'),
    path('create/', views.createtopic, name='createtopic'),
    path('topic/<int:id>', views.topic, name='topic'),
    path('post/<int:id>', views.edit_post, name='post')
]
