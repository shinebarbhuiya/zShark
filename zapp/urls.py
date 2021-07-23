from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.loginPage, name='login'),
    path('logout/', views.logoutUser, name='logout'),
    path('signup/', views.signup, name='signup'),
    path('terms/', views.terms, name="terms"),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('error', views.error, name="error"),

]

handler404 = 'zapp.views.notfound'