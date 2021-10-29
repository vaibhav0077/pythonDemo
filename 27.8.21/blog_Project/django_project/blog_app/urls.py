from django.urls import path
from . import views


urlpatterns = [
    path('blog/', views.blog_home, name='blog_home'),
    path('', views.home, name='homePage'),
    path('demo/', views.Demo, name='Demo'),
    path('about/', views.about, name = 'blog_about'),
    path('blog/about', views.blog_about, name='blog_about'),
    path('users/templates/users/register', views.register, name='Register'),
    path('login/', views.login, name='Login'),
    path('logout/', views.logout, name='logout'),
    path('profile/', views.profile, name='profile'),
]