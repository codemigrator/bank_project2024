from django.urls import path

from credentials import views

app_name = 'credentials'
urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('inform/', views.inform, name='inform'),
    path('personal_details_form/',views.personal_details_form, name='details_form'),
    path('ajax/load_branches/',views.load_branches,name='ajax_branch_url'),
    path('logout/', views.logout, name='logout')

]
