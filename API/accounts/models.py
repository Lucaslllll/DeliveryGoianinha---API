from django.db import models
from django.contrib.auth.models import User, AbstractUser


# posting_date nao mostra porque é adicionado na hora

# class CustomUser(AbstractUser):
#     username = models.CharField(max_length=30, unique=False)
#     USERNAME_FIELD = 'email'
    
class Codigo(models.Model):
    code = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    email = models.EmailField(max_length=200, null=True)
    posting_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username