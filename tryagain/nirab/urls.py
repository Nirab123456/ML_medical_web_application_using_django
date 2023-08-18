from django.urls import path,include
from . import views

urlpatterns = [
    # path('',views.home,name='home'),
    path('',views.index_new,name='index_new'),
    path('index_new/',views.index_new,name='index_new'),

    path('logout/',views.logout_user,name='logout_user'),
    path('login_register/',views.login_register,name='login_register'),





    path('<int:year>/<str:month>',views.event,name='event'),
    path('profile/',views.profile,name='profile'),
    path('real/',views.real, name='real'),
    path('record',views.view_record,name='record'),
    path('delete_record/',views.delete_record,name='delete_record'),
    path('add_event/',views.add_event,name='add_event'),
    path('join_event/<int:event_id>', views.join_event, name='join_event'),
    path('leave_event/<int:event_id>', views.leave_event, name='leave_event'),
    path('BN_OCR/',views.BN_OCR,name='BN_OCR'),
    path('ENG_OCR/',views.ENG_OCR,name='ENG_OCR'),
    path('download_text/<path:text_path>/', views.download_text, name='download_text'),
    path('download_pdf/<path:pdf_path>/', views.download_pdf, name='download_pdf'),
    path('index/', views.index, name='index'),
    path('save_mail_form/', views.save_mail_form, name='save_mail_form'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('profile_picture/', views.profile_picture, name='profile_picture'),
    path('ENG_OCR_HANDWRITTEN', views.ENG_OCR_HANDWRITTEN, name='ENG_OCR_HANDWRITTEN'),
    path('ENG_TEXT_HANDWRITTEN/', views.ENG_TEXT_HANDWRITTEN, name='ENG_TEXT_HANDWRITTEN'),
    path('about/', views.about, name='about'),
    path('hire_me/', views.hire_me, name='hire_me'),
    path('projects/', views.projects, name='projects'),
    path('add_or_update_record/', views.add_or_update_record, name='add_or_update_record'),
    path('add_or_update_profile_picture/', views.add_or_update_profile_picture, name='add_or_update_profile_picture'),
    path('base_ocr/', views.base_ocr, name='base_ocr'),
    path('base_handwritten/', views.base_handwritten, name='base_handwritten'),
    path('change_password/', views.change_password, name='change_password'),









    path('get_medication_details/', views.get_medication_details, name='get_medication_details'),
    path('get_generic_medication_details/', views.get_generic_medication_details, name='get_generic_medication_details'),
    path('med_search/', views.med_search, name='med_search'), 
    path('med_search_generic/', views.med_search_generic, name='med_search_generic'),
    path('med_search_results/', views.med_search_results, name='med_search_results'),





    path('medicine_details/', views.medicine_details, name='medicine_details'),
    path('get_medicine_details/', views.get_medicine_details, name='get_medicine_details'),
    path('med_details_search_results/', views.med_details_search_results, name='med_details_search_results'),
    path('medicine_details_generic/', views.medicine_details_generic, name='medicine_details_generic'),
    path('get_medicine_details_generic/', views.get_medicine_details_generic, name='get_medicine_details_generic'),




    path('get_word_recommendations/', views.get_word_recommendations, name='get_word_recommendations'),
    path('get_generic_name_recommendations/', views.get_generic_name_recommendations, name='get_generic_name_recommendations'),








    path('medicine_chatbot/', views.medicine_chatbot, name='medicine_chatbot'),
    path('get_medicine_chat/', views.get_medicine_chat, name='get_medicine_chat'),




    path('presciption_classification_beta/', views.presciption_classification_beta, name='presciption_classification_beta'),
    path('get_presciption_classification_beta/', views.get_presciption_classification_beta, name='get_presciption_classification_beta'),
    path('presciption_classification_beta_results/', views.presciption_classification_beta_results, name='presciption_classification_beta_results'),



    path('main_bmi_calculator/', views.main_bmi_calculator, name='main_bmi_calculator'),
    path('C_V_D_prediction/', views.C_V_D_prediction, name='C_V_D_prediction'),
    path('get_C_V_D_prediction/', views.get_C_V_D_prediction, name='get_C_V_D_prediction'),



    path('personal_diary_input/', views.personal_diary_input, name='personal_diary_input'),
    path('predict_mental_health/', views.predict_mental_health, name='predict_mental_health'),


    path('trial/', views.trial, name='trial'),
]