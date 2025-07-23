from django.test import TestCase
from django.contrib.auth.models import User
from django.shortcuts import reverse
from .models import Postblog

class BlogPostTest(TestCase):
    def setUp(self):
        self.user = User.objects.create(username='Mobile')
        self.post1 = Postblog.objects.create(
            title ='ApplePhone',
            text = 'The Best',
            status = Postblog.STATUS_CHOICES[0],
            author = self.user,
        )

    def test_post_list_url(self):
        response = self.client.get('/blog/')
        self.assertEqual(response.status_code, 200)

    def test_post_list_url_by_name(self):
        response = self.client.get(reverse('posts_list'))
        self.assertEqual(response.status_code, 200)
