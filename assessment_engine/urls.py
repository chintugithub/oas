from django.urls import path
from . import views

# URLConf
urlpatterns = [
    path('standards/', views.standard_list),
    path('subjects/', views.subject_list),
]