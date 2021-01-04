from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'movies'

urlpatterns = [
    path('<query>/search/', views.search, name='search'),
    path('', views.index, name='index'),
    path('create/', views.create, name='create'),
    path('<int:movie_pk>', views.detail, name='detail'),
    path('<int:movie_pk>/delete/', views.delete, name='delete'),
    path('<int:movie_pk>/update/', views.update, name='update'),
    # data insert url
    path('dump/', views.dump, name='dump'),
    path('info/<int:key>/', views.info, name="info"),
    path('best/',views.best, name="best"),

    path('allmovie/<selected>', views.allmovie, name='allmovie'),
    # data insert url2
    # path('dump2/', views.dump2, name='dump2'),    
    
    # data insert url3
    path('dump3/', views.dump3, name='dump3'),
    path('recommend/<int:count>',views.recommend, name="recommend"),
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



