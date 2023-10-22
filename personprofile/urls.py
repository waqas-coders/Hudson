from django.urls import path
from . import views

urlpatterns = [
    path('', views.front_page, name='front_page'),
    path('create/', views.add_person, name='add_person'),
    path('list/', views.list_people, name='list_people')
]
