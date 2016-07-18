from django.test import TestCase
from .models import PostBlog


class PostTests(TestCase):
    """
    Here we'll define the tests
    that we'll run against our Post model
    """

    def test_str(self):
        test_title = PostBlog(title='My Latest Blog Post')
        self.assertEquals(str(test_title),
                          'My Latest Blog Post')