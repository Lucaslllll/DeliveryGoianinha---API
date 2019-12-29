from django.contrib.auth.models import User
from django.contrib.auth.hashers import check_password


class EmailAuthBackend(object):
	
 
	def authenticate(self, username=None, password=None):
		try:
			user = User.objects.get(email=username)
			if user.check_password(password):
				objectss = User.objects.get(email=username)
				return objectss
		except User.DoesNotExist:
			return None
 
	def get_user(self, user_id):
		
		try:
			return User.objects.get(pk=user_id)
		except User.DoesNotExist:
			return None