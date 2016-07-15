from django.shortcuts import render, redirect
from contact.forms import ContactForm
from django.template.loader import get_template
from django.core.mail import EmailMessage
from django.template import Context

def contact(request):
    form_class = ContactForm

    if request.method == 'POST':
        form = form_class(data=request.POST)

        if form.is_valid():
            contact_name = request.POST.get('contact_name', '')
            contact_email = request.POST.get('contact_email', '')
            form_content = request.POST.get('content', '')

            # Info for email
            template = get_template('contact/contact_template.txt')
            context = Context({'contact_name': contact_name, 'contact_email': contact_email, 'form_content': form_content,})
            content = template.render(context)
            email = EmailMessage(
                "New contact form submission",
                content,
                "Fintopics Social Network" +'',
                ['youremail@gmail.com'],
                headers = {'Reply-To': contact_email }
            )
            email.send()
            return redirect('contact')
    else:
        form_class = ContactForm()

    return render(request, 'contact/contact.html', {'form': form_class,})
