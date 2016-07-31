from django.test import TestCase
from about.views import about_map
from django.core.urlresolvers import resolve
from django.shortcuts import render_to_response



class AboutPageTest(TestCase):
    
    def test_about_page_status_code_is_ok(self):
        about_page = self.client.get('/about/')
        self.assertEquals(about_page.status_code, 200)

    def test_about_page_status_code_is_not_404(self):
        about_page = self.client.get('/about/')
        self.assertNotEquals(about_page.status_code, 404)

    def test_about_page_status_code_is_not_500(self):
        about_page = self.client.get('/about/')
        self.assertNotEquals(about_page.status_code, 500)

    def test_about_page(self):
        about_page = resolve('/about/')
        self.assertEqual(about_page.func, about_map)

    def test_check_content_is_correct(self):
        about_page = self.client.get('/about/')
        self.assertTemplateUsed(about_page, "about/about.html")
        about_page_template_output = render_to_response("about/about.html").content
        self.assertEquals(about_page.content, about_page_template_output)