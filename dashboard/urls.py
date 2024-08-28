from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name='home'),  # Home page
   path('register/', views.register, name='register'),  # Registration page
   path('login/', views.user_login, name='login'),  # Login page
   path('logout/', views.user_logout, name='logout'),
   path('buttons/', views.buttons, name='buttons'),
   path('admin/add-button/', views.add_button, name='add_button'),
   path('click-button/<int:button_id>/', views.button_click, name='button_click'),
]
