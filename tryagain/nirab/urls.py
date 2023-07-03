from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('<int:year>/<str:month>',views.event,name='event'),
    path('login/',views.login_user,name='login_user'),
    path('user_profile',views.user_profile,name='user_profile'),
    path('real/',views.real, name='real'),
    path('logout/',views.logout_user,name='logout_user'),
    path('register/',views.register_user,name='register'),
    path('record',views.view_record,name='record'),
    path('delete_record',views.delete_record,name='delete_record'),
    path('update_record',views.update_record,name='update_record'),
    path('add_record',views.add_record,name='add_record'),
    path('add_event',views.add_event,name='add_event'),
    path('join_event/<int:event_id>', views.join_event, name='join_event'),
    path('leave_event/<int:event_id>', views.leave_event, name='leave_event'),
    path('add_image',views.add_image,name='add_image'),
    path('bangla_ocr',views.bangla_ocr,name='bangla_ocr'),
    path('get_ocr',views.get_ocr,name='get_ocr'),

]
