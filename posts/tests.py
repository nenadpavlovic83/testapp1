from django.test import TestCase
from django.contrib.auth import get_user_model
# Create your tests here.
from django.urls import reverse

from .models import Posts
User = get_user_model()


class PostsModelTestCase(TestCase):
	def setUp(self):
		test_user = User.objects.create(username='Test_Post_User')

	def test_post_item(self):
		obj = Posts.objects.create(
			user=User.objects.first(),
			content='Some random content'
			)
		self.assertTrue(obj.content == 'Some random content')	
		self.assertTrue(obj.id==1)
		absolute_url = reverse('posts:detail', kwargs={'pk':1})
		self.assertEqual(obj.get_absolute_url(), absolute_url)


	def test_post_url(self):
		obj = Posts.objects.create(
			user=User.objects.first(),
			content='Some random content'
			)
		absolute_url = reverse('posts:detail', kwargs={'pk':1})
		self.assertEqual(obj.get_absolute_url(), absolute_url)
