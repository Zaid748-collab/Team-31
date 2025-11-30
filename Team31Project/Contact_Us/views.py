from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings
from .models import ContactMessage


def contact_view(request):
    success = False

    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        subject = request.POST.get("subject")
        message = request.POST.get("message")

        # Sauvegarde en base
        ContactMessage.objects.create(
            name=name,
            email=email,
            subject=subject,
            message=message,
        )

        # Construction du contenu de l'email
        email_subject = f"New contact form submission: {subject}"
        email_body = f"""
New message from the Contact Us form:

Name: {name}
Email: {email}
Subject: {subject}

Message:
{message}
"""

        # Adresse qui va recevoir le message
        recipient = ["team31astontech@gmail.com"]  # par ex: ton camarade

        # Envoi de l'email
        send_mail(
            subject=email_subject,
            message=email_body,
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=recipient,
            fail_silently=False,
        )

        success = True

    return render(request, "Contact_Us/Contact_Us.html", {"success": success})


