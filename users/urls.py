from .views import LogoutAPI, RegisterAPI, LoginAPI, GetUser, ChangeEmpPasswordView, ChangePasswordView
from django.urls import path

urlpatterns = [
    path('register/', RegisterAPI.as_view(), name='register'),
    path('login/', LoginAPI.as_view(), name='login'),
    path('logout/', LogoutAPI.as_view(), name='logout'),
    path('getuser/', GetUser.as_view()),
    path('changepassword/<str:pk>',
         ChangeEmpPasswordView.as_view(), name='employeepass'),
    path('changepassword/', ChangePasswordView.as_view(), name='selfpass')
]
