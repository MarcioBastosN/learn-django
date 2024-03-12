from django.urls import path

from . import views

app_name = 'pessoas'

urlpatterns =[
    path("", views.IndexView.as_view(), name='index'),
    path("genero", views.GenerosView.as_view(), name='generos'),
    path("homens", views.HomenView.as_view(), name='homens'),
    path("mulher", views.MulhersView.as_view(), name='mulhers'),
    # path("mulher", views.MulhersView.as_view(), name='mulhers')


]