from django.shortcuts import render, get_object_or_404
from .models import Contact
from django.contrib.auth.decorators import login_required
from django.http import Http404


@login_required
def get_contacts(request):
    return render(request, "contacts/contacts.html", {'contact_list': Contact.objects.all()})


@login_required
def get_details(request, contact_id):
    try:
        contact = Contact.objects.filter(pk=contact_id)
    except Contact.DoesNotExist:
        raise Http404("Noooo")
    return render(request, "contacts/contacts_detail.html", {'details': contact })
