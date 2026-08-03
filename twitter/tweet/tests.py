from django.test import TestCase
from django.urls import reverse


class TweetCreateViewTests(TestCase):
    def test_create_page_renders_form_fields(self):
        response = self.client.get(reverse("tweet_create"))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'name="content"')
        self.assertContains(response, 'name="photo"')
