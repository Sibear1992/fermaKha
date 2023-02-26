from django.urls import path
from django_registration.backends.one_step.views import RegistrationView
from django_registration.backends.activation.views import ActivationView
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('register/', views.register, name='register'),
    path('shop/', views.shop, name='shop'),
    path('signup/', views.SignUpView.as_view(), name='signup'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),


    # path('activate/<str:activation_key>/', ActivationView.as_view(), name='django_registration_activate'),
    # path('register/success/', views.registration_success, name='registration_success'),
    # path('profile/', views.profile, name='profile'),
    # path('profile/edit/', views.edit_profile, name='edit_profile'),
    # path('logout/', views.logout_request, name='logout'),

]