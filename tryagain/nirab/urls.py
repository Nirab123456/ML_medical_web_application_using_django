from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('login/',views.login_user,name='login_user'),
    path('real/',views.real, name='real'),
    path('logout/',views.logout_user,name='logout_user'),
    path('register/',views.register_user,name='register'),
    path('records/',views.view_records,name='records'),
    path('records/<int:pk>',views.view_record,name='record'),

]
