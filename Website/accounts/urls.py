from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

app_name = 'accounts'

# Here we are not creating Login view or Logout view because its now by default in django

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name="accounts/login.html"),name='login'),
    # By default logout will take you to home page.
    path('logout/', auth_views.LogoutView.as_view(), name="logout"),
    path('signup/', views.SignUp.as_view(), name="signup"),
]
