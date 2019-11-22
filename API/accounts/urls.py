from django.conf.urls import url
from django.urls import include
from . import api, views
from django.urls import path


urlpatterns = [
	path('api/auth/register', api.RegistrarAPI.as_view(), name='register'),
	path('api/auth/login', api.LoginAPI.as_view(), name='login'),
	path('api/auth/user', api.UserAPI.as_view(), name='user'),
	path('logout', api.Logout.as_view(), name='logout'),
	path('api-token-auth', views.CustomAuthToken.as_view(), name='token'),
	path('verify-token', api.VerifyToken.as_view(), name='verify-token'),
	path('reset-password', api.ResetPasswordAPI, name='reset-password')
]