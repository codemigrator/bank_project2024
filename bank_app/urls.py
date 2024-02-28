from django .urls import path

from bank_app import views
app_name = 'bank_app'
urlpatterns = [
    path('', views.home, name='home'),
    path('bank/', views.home, name='bank'),

]
