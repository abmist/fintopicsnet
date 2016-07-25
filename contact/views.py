from django.shortcuts import render, redirect
from contact.forms import ContactForm
from django.template.loader import get_template
from django.template import Context
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect

def contact(request):

    if request.method == 'POST':
        form = ContactForm(request.POST)

        if form.is_valid():
            contact_name = form.cleaned_data['contact_name']
            sender = form.cleaned_data['sender']
            message = form.cleaned_data['message']
            cc_myself = form.cleaned_data['cc_myself']

            recipients = ['me@example.com']
            if cc_myself:
                recipients.append(sender)

            send_mail(contact_name, message, sender, recipients)
            return redirect('contact')

    else:
        form = ContactForm()

    return render(request, 'contact/contact.html', {'form': form,})
