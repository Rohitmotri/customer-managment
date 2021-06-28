from django.contrib.auth import views as auth_views
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home,name= 'home'),
    path('login/',views.loginPage,name= "login"),
    path('register/',views.registerPage,name = "register"),
    path('user/',views.userOnly , name ='user-page'),
    path('logout/',views.logoutUser ,name = "logout"),

    path('accounts/',views.accountSettings, name= 'account'),
    path('products/', views.products,name='products'),
    path('customer/<id>/', views.customer,name = 'customer'),
    
    path('create_order/<id>/',views.create_Order , name = 'create_order'),
    path('update_order/<id>/',views.update_Order, name = 'update_order'),
    path('delete_order/<id>/',views.deleteOrder, name = 'delete_order'),

    path('reset_password/',
    auth_views.PasswordResetView.as_view(),
    name = "reset_password"),
    path('reset_password_sent/',
    auth_views.PasswordResetDoneView.as_view(),
    name = "password_reset_done"),
    path('reset/<uidb64>/<token>',
    auth_views.PasswordResetConfirmView.as_view(),
    name = "password_reset_confirm"),
    path('reset_password_complete/',
    auth_views.PasswordResetCompleteView.as_view(),
    name = "password_reset_complete"),
]