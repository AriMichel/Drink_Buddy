from django.test import TestCase, Client
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

class PostViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.factory = RequestFactory()
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.post = Post.objects.create(
            title='Test Post',
            content='This is a test post.',
            author=self.user
        )

    def test_post_list_view(self):
        request = self.factory.get(reverse('post'))
        response = PostListView.as_view()(request)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'blog/post_home.html')

    def test_post_detail_view(self):
        request = self.factory.get(reverse('post-detail', kwargs={'pk': self.post.pk}))
        response = PostDetailView.as_view()(request, pk=self.post.pk)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'blog/post_detail.html')

    def test_post_create_view(self):
        request = self.factory.post(reverse('post-create'), data={'title': 'New Post', 'content': 'This is a new post.'})
        request.user = self.user
        response = PostCreateView.as_view()(request)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('post/2/', kwargs={'pk': 2}))

    def test_post_update_view(self):
        request = self.factory.post(reverse('post-update', kwargs={'pk': self.post.pk}), data={'title': 'Updated Post', 'content': 'This post has been updated.'})
        request.user = self.user
        response = PostUpdateView.as_view()(request, pk=self.post.pk)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('post-detail', kwargs={'pk': self.post.pk}))

    def test_post_delete_view(self):
        request = self.factory.post(reverse('post-delete', kwargs={'pk': self.post.pk}))
        request.user = self.user
        response = PostDeleteView.as_view()(request, pk=self.post.pk)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('post-list'))


