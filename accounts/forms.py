from django import forms
from django.contrib.auth.forms import UserCreationForm
from accounts.models import User
from django.core.exceptions import ValidationError


class UserRegistrationForm(UserCreationForm):
    MONTH_CHOICES = [(i, i,) for i in xrange(1, 12)]
    YEAR_CHOICES = [(i, i,) for i in xrange(2015, 2036)]
    first_name = forms.CharField(label='First name')
    last_name = forms.CharField(label='Last name')
    credit_card_number = forms.CharField(label='Credit card number')
    cvv = forms.CharField(label='Security code (CVV)')
    expiry_month = forms.ChoiceField(label="Month", choices=MONTH_CHOICES)
    expiry_year = forms.ChoiceField(label="Year", choices=YEAR_CHOICES)
    stripe_id = forms.CharField(widget=forms.HiddenInput)
    user_profile_picture = forms.ImageField(label='Profile picture', required=False)
    city = forms.CharField(label='City')
    country = forms.CharField(label='Country')
    education = forms.CharField(label='Education')
    interest = forms.CharField(label='Interest')
    password1 = forms.CharField(
        label='Password',
        widget=forms.PasswordInput
    )

    password2 = forms.CharField(
        label='Password confirmation',
        widget=forms.PasswordInput
    )

    class Meta:
        model = User
        fields = ['email', 'password1', 'password2', 'stripe_id',  'first_name' , 'last_name', 'city', 'country', 'education', 'interest', 'user_profile_picture'   ]
        exclude = ['username']

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')

        if password1 and password2 and password1 != password2:
            message = "Passwords do not match"
            raise forms.ValidationError(message)

        return password2

    def clean_email(self):
        email = self.cleaned_data.get('email')

        if not email:
            message = "Please enter your email address"
            raise forms.ValidationError(message)

        return email


    def save(self, commit=True):
        instance = super(UserRegistrationForm, self).save(commit=False)

        # automatically set to email address to create a unique identifier
        instance.username = instance.email

        if commit:
            instance.save()

        return instance


class UserLoginForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)


#Just a test. I'll delete it.
class UpdateProfileForm(forms.ModelForm):
    user_profile_picture = forms.ImageField(label='Profile picture', required=False)
    city = forms.CharField(label='City')

    class Meta:
        model = User
        fields = ('user_profile_picture', 'city')

    def clean_city(self):
        city = self.cleaned_data.get('city')

        return city

    def save(self, commit=True):
        user = super(UpdateProfileForm, self).save(commit=False)
        user.email = self.cleaned_data['city']

        if commit:
            user.save()

        return user