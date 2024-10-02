from django.test import SimpleTestCase, TestCase
from django.urls import reverse


class TestHomepageView(SimpleTestCase):
    def test_get_webpage(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)

    def test_get_webpage_by_name(self):
        response = self.client.get(reverse("home"))
        self.assertEqual(response.status_code, 200)

    def test_content_exist_correctly(self):
        response = self.client.get(reverse("home"))
        self.assertContains(response, "<h1>Home Page</h1>")


class TestListView(TestCase):
    def test_get_webpage(self):
        response = self.client.get("/archive/")
        self.assertEqual(response.status_code, 200)

    def test_get_webpage_by_name(self):
        response = self.client.get(reverse("archive-list"))
        self.assertEqual(response.status_code, 200)

    def test_content_exist_correctly(self):
        response = self.client.get(reverse("archive-list"))
        self.assertContains(response, "<h1>Archive List</h1>")
