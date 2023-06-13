from django.contrib.auth.views import LogoutView
from django.urls import path

from . import views

urlpatterns = [
    # Main pages
    path('', views.HomePage.as_view(), name='home'),
    path('get_started/', views.GetStartedPage, name='get-started'),

    # Account pages
    path('signup/', views.SignUpPage.as_view(), name='signup'),
    path('login/', views.LoginPage.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('edit_account/', views.EditAccountPage.as_view(), name='edit-account'),
    path('change_password/', views.ChangePasswordPage.as_view(), name='change-password'),
    path('delete_account/', views.DeleteAccountPage.as_view(), name='delete-account'),
]