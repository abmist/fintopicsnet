from django.shortcuts import render, get_object_or_404
from .models import Contact
from django.contrib.auth.decorators import login_required


@login_required
def get_contacts(request):
    return render(request, "contacts/contacts.html", {'contact_list': Contact.objects.all()})

@login_required
def get_contacts_detail(request, contact_id):
    contacts = get_object_or_404(Contact, pk=contact_id)
    return render(request, "contacts/contacts_detail.html", {'details': contacts})
