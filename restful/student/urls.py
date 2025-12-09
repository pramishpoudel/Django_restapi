from django.urls import path,include
from . import views

urlpatterns = [    
    path('',views.students),
    path('about/',views.about),
]