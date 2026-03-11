from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings

def contact_view(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        full_message = f"""
        Name: {name}
        Email: {email}
        Message: {message}
        """

        send_mail(
            subject='New Message from Contact Form',
            message=full_message,
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[settings.EMAIL_HOST_USER],
        )

        return render(request, 'index.html', {'success': True})  # ✅ success pass ho raha hai

    return render(request, 'index.html')
