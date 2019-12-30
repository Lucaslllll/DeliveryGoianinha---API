from django.conf.urls import url
from django.urls import include
from . import api, views, utils
from django.urls import path

from rest_framework import routers
router = routers.DefaultRouter()

router.register('api/codigo', api.CodigoViewSet, 'codigo')
urlpatterns = router.urls



urlpatterns += [
	path('api/auth/register_email', api.RegistrarEmailAPI.as_view(), name='register_email'),
	path('api/auth/register_confirme', api.RegistrarConfirmeAPI.as_view(), name='register_confime'),
	path('api/auth/register', api.RegistrarAPI.as_view(), name='register'),

	path('api/auth/login', api.LoginAPI.as_view(), name='login'),
	path('api/auth/user', api.UserAPI.as_view(), name='user'),
	path('logout', api.Logout.as_view(), name='logout'),
	path('api-token-auth', views.CustomAuthToken.as_view(), name='token'),
	path('verify-token', api.VerifyToken.as_view(), name='verify-token'),
	path('reset-password', api.ResetPasswordAPI.as_view(), name='reset-password'),
	path('recovery-password', api.EmailList.as_view(), name='recovery-password'),
	path('recovery-confirme/<int:pk>/<str:token>', api.EmailConfirme.as_view(), name='recovery-confirme'),
	path('change-password', api.ChangePassword.as_view(), name='change-password'),
]