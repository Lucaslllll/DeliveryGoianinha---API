from django.conf.urls import url
from django.urls import include
from . import api, views
from knox import views as knox_views

urlpatterns = [
	url(r'api/auth', include('knox.urls')),
	url(r'^api/auth/registrar$', api.RegistrarAPI.as_view()),
	url(r'^api/auth/login$', api.LoginAPI.as_view()),
	url(r'^api/auth/user$', api.UserAPI.as_view()),
	url(r'^logout/', knox_views.LogoutView.as_view(), name='knox_logout'),
	url(r'^logoutall/', knox_views.LogoutAllView.as_view(), name='knox_logoutall'),
	url(r'^api-token-auth/', views.CustomAuthToken.as_view()),
	url(r'^verify-token/', api.VerifyToken.as_view())
]