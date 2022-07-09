from django.urls import path
from .views import home_view, redirect_url_view, urls_list

appname = 'shortener'

urlpatterns = [
    path('', home_view, name='home'),
    path('urls_list', urls_list, name='urls_list'),
    path('<str:shortened_part>', redirect_url_view, name='redirect')
]
