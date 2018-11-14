from django.urls import path, include
from accounts.views import user_login,user_logout,user_success,user_register

app_name="accounts"
urlpatterns = [
    path('login/',user_login,name="user_login"),
    path('login/success/',user_success,name="user_success"),
    path('logout/',user_logout,name="user_logout"),
    path('register/',user_register,name="user_register")
]

