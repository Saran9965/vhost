# from django.contrib import admin
# from django.urls import path
# from myapp import views
# from django.http import HttpResponseNotFound

# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('', views.frontpage,name='frontpage'),
#     path('signup/', views.signup,name='signup'),
#     path('login/', views.loginpage,name='login'),
#     path('home/', views.HomePage,name='home'),
#     path('logout/', views.logoutpage,name='logout'),
#     path('admin/deleteall/',views.block_view),
#     path('hiddenpage/',views.block_view),
# ]

# handler404 = 'myapp.views.custom_404_view'

from django.contrib import admin
from django.urls import path
from myapp import views

urlpatterns = [
    path('admin/', admin.site.urls),

    # Auth routes
    path('', views.frontpage, name='frontpage'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.loginpage, name='login'),
    path('logout/', views.logoutpage, name='logout'),

    # Protected user home
    path('home/', views.HomePage, name='home'),

    # Blocked/restricted routes
    path('admin/deleteall/', views.block_view),
    path('hiddenpage/', views.block_view),
]

# Custom error handler (404)
handler404 = 'myapp.views.custom_404_view'
handler404 = 'myapp.views.custom_404_view'
