from django.conf.urls import url
from django.urls import include
from . import api, views

urlpatterns = [
	url(r'^api/auth/register$', api.RegistrarAPI.as_view()),
	url(r'^api/auth/login$', api.LoginAPI.as_view()),
	url(r'^api/auth/user$', api.UserAPI.as_view()),
	url(r'^logout/', api.Logout.as_view()),
	url(r'^api-token-auth/', views.CustomAuthToken.as_view()),
	url(r'^verify-token/', api.VerifyToken.as_view())
]