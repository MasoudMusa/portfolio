from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages
from .models import Category, Project


def portfolio_index(request):
    categories = Category.objects.all()
    projects = Project.objects.select_related('category').all()
    
    if request.method == 'POST':
        # Form Handling
        name = request.POST.get('name')
        sender_email = request.POST.get('email')
        subject = request.POST.get('subject')
        user_message = request.POST.get('message')

        email_body = f"From: {name} <{sender_email}>\n\nSubject: {subject}\n\nMessage:\n{user_message}"

        try:
            send_mail(
                subject=f"Portfolio Inquiry: {subject}",
                message=email_body,
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=[settings.CONTACT_EMAIL],
                fail_silently=False,
            )
            messages.success(request, "Your message has been sent!")
        except Exception:
            messages.error(request, "Failed to send message. Please try again later.")
            
        return redirect('home')

    return render(request, 'core/index.html', {
        'categories': categories,
        'projects': projects
    })