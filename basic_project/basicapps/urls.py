from django.urls import path
from basicapps import views

urlpatterns = [
    path('', views.form_name_view, name='form_name_view'),
    path('', views.index, name='index'),
]
