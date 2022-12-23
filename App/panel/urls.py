from django.urls import path
from . import views




urlpatterns = [
    path('panel',views.keyword_researcher,name='panel'),
]
