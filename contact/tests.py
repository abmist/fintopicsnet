from django.test import TestCase
from contact.views import contact
from django.core.urlresolvers import resolve
from django.shortcuts import render_to_response



class AboutPageTest(TestCase):

    def test_contact_page_status_code_is_ok(self):
        contact_page = self.client.get('/contact/')
        self.assertEquals(contact_page.status_code, 200)

    def test_contact_page_status_code_is_not_404(self):
        contact_page = self.client.get('/contact/')
        self.assertNotEquals(contact_page.status_code, 404)

    def test_contact_page_status_code_is_not_500(self):
        contact_page = self.client.get('/contact/')
        self.assertNotEquals(contact_page.status_code, 500)

    def test_contact_page(self):
        contact_page = resolve('/contact/')
        self.assertEqual(contact_page.func, contact)

