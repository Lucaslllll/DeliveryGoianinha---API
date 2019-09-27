from django.conf.urls import url
from django.urls import include
from . import api
from knox import views as knox_views

urlpatterns = [
	url(r'api/auth', include('knox.urls')),
	url(r'^api/auth/registrar$', api.RegistrarAPI.as_view()),
	url(r'^api/auth/login$', api.LoginAPI.as_view()),
	url(r'^api/auth/user$', api.UserAPI.as_view()),
	url(r'^api/auth/logout$', knox_views.LogoutView.as_view(), name='knox_logout'),

]