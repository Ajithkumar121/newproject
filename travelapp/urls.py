from .import views
from django.urls import path

urlpatterns = [

    path('',views.index,name='index'),
    path('destinations/',views.destination,name="destinations"),
    path('elements/', views.elements, name="elements"),
    path('news/', views.news, name="news"),
    path('contact/', views.contact, name="contact"),
    path('registration/',views.registration,name="registration"),
    path('login/',views.login,name="login"),
    path('logout/',views.logout,name="logout"),
]
