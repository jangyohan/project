from django.urls import path
from . import views

app_name = 'articles'

urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.create, name='create'),
    path('<int:article_pk>/', views.detail, name='detail'),
    path('<int:article_pk>/certificates/', views.certificate_list, name='certificate_list'),
    path('<int:article_pk>/certificates/create/', views.certificate_create, name='certificate_create'),
    path('<int:article_pk>/certificates/<int:certificate_pk>/', views.certificate_detail, name='certificate_detail'),
    path('<int:article_pk>/languages/', views.language_list, name='language_list'),
    path('<int:article_pk>/languages/create/', views.language_create, name='language_create'),
    path('<int:article_pk>/languages/<int:language_pk>/', views.language_detail, name='language_detail'),
    path('<int:article_pk>/careers/', views.career_list, name='career_list'),
    path('<int:article_pk>/careers/create/', views.career_create, name='career_create'),
    path('<int:article_pk>/careers/<int:career_pk>/', views.career_detail, name='career_detail'),
    path('<int:article_pk>/selfintroductions/<int:recruitment_pk>/', views.selfintroduction_list, name='selfintroduction_list'),
    path('<int:article_pk>/selfintroductions/', views.selfintroduction_list2, name='selfintroduction_list2'),
    path('<int:article_pk>/selfintroductions/<int:recruitment_pk>/create/', views.selfintroduction_create, name='selfintroduction_create'),
    path('<int:article_pk>/selfintroductions/<int:recruitment_pk>/<int:selfintroduction_pk>/', views.selfintroduction_detail, name='selfintroduction_detail'),
    path('search/<str:query>/', views.search, name='search'),
]