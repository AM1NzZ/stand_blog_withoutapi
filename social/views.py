from django.shortcuts import render, redirect
from .models import Contactus
from .forms import ContactUsForm


def contact(request):
    if request.method == 'POST':
        form = ContactUsForm(data=request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            subject = form.cleaned_data['subject']
            body = form.cleaned_data['body']
            Contactus.objects.create(name=name, email=email, subject=subject, body=body)
            return redirect('contact')
        else:
            return render(request, 'social/contactus.html', {'form': form})
    else:
        form = ContactUsForm()

    return render(request, "social/contactus.html", {'form': form})
