from os.path import isfile
from django.core.mail import send_mail as base_send_mail, EmailMultiAlternatives
from django.urls import reverse
from templated_email import InlineImage, get_templated_mail
from django.template.loader import render_to_string
from application import settings


def send_confirm_email(user, to=None, image_path=settings.DEFAULT_EMAIL_IMAGE):
    if settings.DEBUG:
        to = [admin[1] for admin in settings.ADMINS]
    elif to is None:
        to = user.email
    text = 'Good day! We are glad to greet you on our site! To confirm your email please follow this link: ' + \
           'http://localhost:8000' + reverse('home')
    email = EmailMultiAlternatives("Please confirm your email", text, settings.SITE_NO_REPLY_EMAIL, to)
    pic = InlineImage('title_image.jpg', open(image_path, 'rb').read())
    pic.attach_to_message(email)
    html = render_to_string('core/email/confirm_email.html', {'title_pic': pic, 'username': user.username,
                                                              'confirmation_link': 'http://localhost:8000/'})
    email.attach_alternative(html, 'text/html')
    email.send()


def send_digest_email(user, news, to=None, image_path=settings.DEFAULT_EMAIL_IMAGE):
    if settings.DEBUG:
        to = [admin[1] for admin in settings.ADMINS]
    elif to is None:
        to = user.email
    text = 'There is some news for you: \n\t' + "\n\t".join(news)
    email = EmailMultiAlternatives("News for you", text, settings.SITE_NO_REPLY_EMAIL, to)
    pic = InlineImage('title_image.jpg', open(image_path, 'rb').read())
    pic.attach_to_message(email)
    html = render_to_string('core/email/digest_email.html', {'title_pic': pic, 'username': user.username,
                                                             'confirmation_link': 'http://localhost:8000/',
                                                             'digest_news': news})
    email.attach_alternative(html, 'text/html')
    email.send()


def send_mail(subject, text, html_template, to=None, image_path=settings.DEFAULT_EMAIL_IMAGE):
    if settings.DEBUG or to is None:
        to = [admin[1] for admin in settings.ADMINS]
    email = EmailMultiAlternatives(subject, text, settings.SITE_NO_REPLY_EMAIL, to)
    if isfile(image_path):
        pic = InlineImage('title_image.jpg', open(image_path, 'rb').read())
        pic.attach_to_message(email)
    else:
        pic = image_path
    html = render_to_string(html_template, {'title_pic': pic})
    email.attach_alternative(html, 'text/html')
    email.send()
