from django.urls import path

from .views import SignUp, MyLoginView, MyLogoutView, signup_success, Profile

app_name = "account"

urlpatterns = [
    path('', Profile.as_view(), name="profile"),
    path('signup/', SignUp.as_view(), name="signup"),
    path('signup_success/', signup_success, name="signup_success"),
    path('login/', MyLoginView.as_view(), name="login"),
    path('logout/', MyLogoutView.as_view(), name="logout"),
]
