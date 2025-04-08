from django.contrib import admin
from django.urls import path
from myapp import views
from django.http import HttpResponseNotFound

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.frontpage,name='frontpage'),
    path('signup/', views.signup,name='signup'),
    path('login/', views.loginpage,name='login'),
    path('home/', views.HomePage,name='home'),
    path('logout/', views.logoutpage,name='logout'),
    path('admin/deleteall/',views.block_view),
    path('hiddenpage/',views.block_view),
]

handler404 = 'myapp.views.custom_404_view'
handler500 = 'myapp.views.custom_500_view'

