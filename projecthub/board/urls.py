from django.conf import settings
from django.urls import path
from django.contrib.auth.views import LogoutView

from . import views
from debug_toolbar.toolbar import debug_toolbar_urls

urlpatterns = [
    path("", views.home, name="home"),
    path("login/", views.user_login, name="user_login"),
    path("register/", views.register, name="user_registration"),
    path('logout/', LogoutView.as_view(next_page='home'), name='user_logout'),
]

if settings.DEBUG:
    urlpatterns += debug_toolbar_urls()
