from django.db import models
from django.contrib.auth.models import User


# posting_date nao mostra porque é adicionado na hora

class Codigo(models.Model):
    code = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    posting_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username