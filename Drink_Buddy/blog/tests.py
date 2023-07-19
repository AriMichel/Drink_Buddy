from django.test import TestCase
from django.test import TestCase, RequestFactory
from django.urls import reverse
from django.utils import timezone
from django.contrib.auth.models import User
from blog.models import Post
from blog.views import PostListView, PostCreateView, PostDetailView, PostUpdateView, PostDeleteView


class PostModelTest(TestCase):
    def setUp(self):
        # Create a user for testing
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        
        # Create a post for testing
        self.post = Post.objects.create(
            title='Test Post',
            content='This is a test post.',
            author=self.user
        )
    
    def test_str_representation(self):
        self.assertEqual(str(self.post), 'Test Post')
    
    def test_absolute_url(self):
        expected_url = '/post/1/'.format(self.post.pk)
        self.assertEqual(self.post.get_absolute_url(), expected_url)



  
