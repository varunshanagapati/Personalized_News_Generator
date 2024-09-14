from django.urls import path
from . import views

urlpatterns = [
    path('', views.all,name='articles-all'),
    path('home/', views.home,name='articles-home'),
    path('world/', views.world,name='articles-world'),
    path('politics/',views.politics,name='articles-politics'),
    path('business/',views.business,name='articles-business'),
    path('science-tech/',views.science_tech,name='articles-science-tech'),
    path('entertainment/',views.entertainment,name='articles-entertainment'),
    path('sports/',views.sports,name='articles-sports'),

]
