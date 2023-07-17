from django.test import TestCase
from django.urls import reverse
from unittest.mock import patch
from .models import UserLocation
# Create your tests here.

class LandingPageTests(TestCase):
     # Tests that home.html template is rendered
    def test_render_home_template(self):
        response = self.client.get('/')
        assert response.status_code == 200
        assert 'drink_service/home.html' in [template.name for template in response.templates]

    # AI Generated Test:
    def test_landing_page_view(self):
        response = self.client.get(reverse('landing_page'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'drink_service/landing_page.html')

    def test_landing_page_post(self):
        location = 'Berlin'
        response = self.client.post(reverse('landing_page'), {'location': location})
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, reverse('response_page'))
        self.assertEqual(UserLocation.objects.count(), 1)
        self.assertEqual(UserLocation.objects.latest('id').location, location)