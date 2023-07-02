from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('<int:year>/<str:month>',views.event,name='event'),
    path('login/',views.login_user,name='login_user'),
    path('real/',views.real, name='real'),
    path('logout/',views.logout_user,name='logout_user'),
    path('register/',views.register_user,name='register'),
    path('records/',views.view_records,name='records'),
    path('add_user_record',views.add_user_record,name='add_user_record'),
    path('records/<int:pk>',views.view_record,name='record'),
    path('delete_record/<int:pk>',views.delete_record,name='delete_record'),
    path('update_record/<int:pk>',views.update_record,name='update_record'),
    path('add_record',views.add_record,name='add_record'),
    path('add_event',views.add_event,name='add_event'),
    path('join_event/<int:event_id>', views.join_event, name='join_event'),

]
