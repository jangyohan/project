from django.urls import path
from . import views

app_name = 'articles'

urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.create, name='create'),
    path('<int:article_pk>/', views.detail, name='detail'),
    path('<int:article_pk>/delete/', views.delete, name='delete'),
    path('<int:article_pk>/update/', views.update, name='update'),
    path('comment/', views.comment, name='comment'),
    path('<int:article_pk>/comments/', views.comment_create, name='comments_create'),
    path('comments/<int:comment_pk>/', views.comment_update_and_delete, name='comment_update_and_delete'),
]