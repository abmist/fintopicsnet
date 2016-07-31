from django.test import TestCase
from .models import User
from .forms import UserRegistrationForm
from django import forms
from django.conf import settings


class CustomUserTest(TestCase):

    def test_manager_create(self):
        user = User.objects._create_user(None, "test@test.com",
                                         "password",
                                         False, False)
        self.assertIsNotNone(user)

        with self.assertRaises(ValueError):
            user = User.objects._create_user(None, None, "password",
                                             False, False)

    def test_registration_form(self):
        form = UserRegistrationForm({
            'email': 'professional_tester@test.com',
            'password1': 'Iwillenter_1',
            'password2': 'Iwillenter_1',
            'stripe_id': settings.STRIPE_SECRET,
            'credit_card_number': 4242424242424242,
            'cvv': 123,
            'expiry_month': 9,
            'expiry_year': 2033,
            'first_name': 'Adam',
            'last_name': 'Smith',
            'city': 'London',
            'country': 'England',
            'education': 'IT',
            'interest': 'Branding',
        })
        self.assertTrue(form.is_valid())

    def test_registration_form_fails_with_missing_email(self):
        form = UserRegistrationForm({
            'password1': 'Iwillenter_1',
            'password2': 'Iwillenter_1',
            'stripe_id': settings.STRIPE_SECRET,
            'credit_card_number': 4242424242424242,
            'cvv': 123,
            'expiry_month': 1,
            'expiry_year': 2033
        })
        self.assertFalse(form.is_valid())
        self.assertRaisesMessage(forms.ValidationError,
                                 "Please enter your email address",
                                 form.full_clean())

    def test_registration_fails_with_empty_password1(self):
        form = UserRegistrationForm({
            'email': 'professional_tester@test.com',
            'password2': 'Iwillenter_1',
            'stripe_id': settings.STRIPE_SECRET,
            'credit_card_number': 4242424242424242,
            'cvv': 123,
            'expiry_month': 1,
            'expiry_year': 2033
        })
        self.assertFalse(form.is_valid())
        self.assertRaisesMessage(forms.ValidationError,
                                 "Passwords do not match",
                                 form.full_clean())

    def test_registration_fails_with_empty_password2(self):
        form = UserRegistrationForm({
            'email': 'professional_tester@test.com',
            'password1': 'Iwillenter_1',
            'stripe_id': settings.STRIPE_SECRET,
            'credit_card_number': 4242424242424242,
            'cvv': 123,
            'expiry_month': 1,
            'expiry_year': 2033
        })
        self.assertFalse(form.is_valid())
        self.assertRaisesMessage(forms.ValidationError,
                                 "Passwords do not match",
                                 form.full_clean())

    def test_registration_form_fails_with_passwords_that_dont_match(self):
        form = UserRegistrationForm({
            'email': 'professional_tester@test.com',
            'password1': 'Iwillenter_1',
            'password2': 'Iwillenterawrongpassword',
            'stripe_id': settings.STRIPE_SECRET,
            'credit_card_number': 4242424242424242,
            'cvv': 123,
            'expiry_month': 1,
            'expiry_year': 2033
        })
        self.assertFalse(form.is_valid())
        self.assertRaisesMessage(forms.ValidationError,
                                 "Passwords do not match",
                                 form.full_clean())

    def test_registration_fails_with_cvv(self):
        form = UserRegistrationForm({
            'email': 'professional_tester@test.com',
            'password1': 'Iwillenter_1',
            'stripe_id': settings.STRIPE_SECRET,
            'credit_card_number': 4242424242424242,
            'expiry_month': 1,
            'expiry_year': 2033
        })
        self.assertFalse(form.is_valid())
        self.assertRaisesMessage(forms.ValidationError,
                                 "Please enter your cvv",
                                 form.full_clean())

    def test_registration_fails_with_expiry_year(self):
        form = UserRegistrationForm({
            'email': 'professional_tester@test.com',
            'password1': 'Iwillenter_1',
            'stripe_id': settings.STRIPE_SECRET,
            'credit_card_number': 4242424242424242,
            'cvv': 123,
            'expiry_month': 1,
        })
        self.assertFalse(form.is_valid())
        self.assertRaisesMessage(forms.ValidationError,
                                 "Please enter your expiry_year",
                                 form.full_clean())