from django.urls import path

from . import views

urlpatterns = [
    path('',views.scraper,name='scraper'),
    path('delete/',views.clear,name='clear'),

]
