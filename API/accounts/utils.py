from django.core.mail import send_mail
from django.core import mail

from django.template.loader import render_to_string
from .tokens import account_activation_token
from rest_framework.response import Response
from django.contrib.auth.models import User
from django.http import HttpResponse

from random import choice
from .models import Codigo


# gera e confere a senha do usuário

def gera_senha(tamanho, user):
    caracters = '0123456789abcdefghijlmnopqrstuwvxz'
    senha = ''
    for char in range(0, tamanho):
            senha += choice(caracters)
    Codigo.objects.create(code=senha, user=user)
    return  senha

def conferir(user, code):

    try:
        codigo = Codigo.objects.get(user=user, code=code)
    except Codigo.DoesNotExist:
        codigo = None

    if codigo != None:
        return True
    else:
        return False

# Manda email para usuário

def email_client(request, user, info):
    msg_html = render_to_string('email.html', {
        'user': user,
        'codigo': gera_senha(5, user),
        'info': info
        # 'token':account_activation_token.make_token(user),
    })
    connection = mail.get_connection()

    
    connection.open()
    
    email1 = mail.EmailMessage(
        'EntreGO - Suporte',
        msg_html,
        'entrego.oficialdelivery@gmail.com',
        [user.email, ],
        connection=connection,
    )
    email1.send()



