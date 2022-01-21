from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('widgets/create', views.add_widget, name='add_widget')
]