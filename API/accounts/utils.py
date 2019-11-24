from django.core.mail import send_mail
from django.core import mail

from django.template.loader import render_to_string
from .tokens import account_activation_token
from rest_framework.response import Response
from django.contrib.auth.models import User
from django.http import HttpResponse


def email_client(request, user):
    msg_html = render_to_string('email.html', {
        'user': user,
        'token':account_activation_token.make_token(user),
    })
    connection = mail.get_connection()

    
    connection.open()
    
    email1 = mail.EmailMessage(
        'Hello',
        msg_html,
        'entrego.oficialdelivery@gmail.com',
        [user.email, ],
        connection=connection,
    )
    email1.send()



