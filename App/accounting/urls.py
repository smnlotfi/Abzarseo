
from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name='home'),
    path('login', views.logining, name='login'),
    path('logout', views.logouting, name='logout'),
    path('activate/<slug:uidb64>/<slug:token>/',views.activate,name='activate')
]