from django.test import TestCase
from blog.views import post_list
from .models import PostBlog
from django.core.urlresolvers import resolve
from django.shortcuts import render_to_response



class BlogPageTest(TestCase):

    def test_blog_page_status_code_is_ok(self):
        blog_page = self.client.get('/blog/')
        self.assertEquals(blog_page.status_code, 200)

    def test_blog_page_status_code_is_not_404(self):
        blog_page = self.client.get('/blog/')
        self.assertNotEquals(blog_page.status_code, 404)

    def test_blog_page_status_code_is_not_500(self):
        blog_page = self.client.get('/blog/')
        self.assertNotEquals(blog_page.status_code, 500)

    def test_blog_page(self):
        blog_page = resolve('/blog/')
        self.assertEqual(blog_page.func, post_list)

    def test_check_content_is_correct(self):
        blog_page = self.client.get('/blog/')
        self.assertTemplateUsed(blog_page, "blog/blog_posts.html")




