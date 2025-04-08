from django.contrib import admin
from django.urls import path
from myapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.frontpage,name='frontpage'),
    path('signup/', views.signup,name='signup'),
    path('login/', views.loginpage,name='login'),
    path('home/', views.HomePage,name='home'),
    path('logout/', views.logoutpage,name='logout'),
]

