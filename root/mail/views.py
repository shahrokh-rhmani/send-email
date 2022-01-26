from django.shortcuts import render
from django.http import HttpResponse
from django.core.mail import send_mail


def home(request):
    context = {

    }

    return render(request, 'home.html', context)


def sendmail(request):
    subject = 'sending an email with django'
    email_message = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua'
    from_email = 'test@test.com'
    to_email = 'django@test.com'
    
    send_mail(
        subject,
        email_message,
        from_email,
        [to_email],
        fail_silently=False,
    )
    return HttpResponse('successfully')
