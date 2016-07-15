from django import forms

# our new form
class ContactForm(forms.Form):
    contact_name = forms.CharField(required=True, label='Name', max_length=100)
    sender = forms.EmailField(required=True, label='Email')
    message = forms.CharField(required=True, label='What do you want to tell us?', widget=forms.Textarea)
    cc_myself = forms.BooleanField(required=False, label='With copy to myself?')

    def __init__(self, *args, **kwargs):
        super(ContactForm, self).__init__(*args, **kwargs)
        self.fields['contact_name']
        self.fields['sender']
        self.fields['message']