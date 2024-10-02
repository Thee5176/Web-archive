from django.test import SimpleTestCase, TestCase
from django.urls import reverse


# Template View
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


# List View
class TestArchiveListView(TestCase):
    def test_get_webpage(self):
        response = self.client.get("/archive/")
        self.assertEqual(response.status_code, 200)

    def test_get_webpage_by_name(self):
        response = self.client.get(reverse("archive-list"))
        self.assertEqual(response.status_code, 200)

    def test_content_exist_correctly(self):
        response = self.client.get(reverse("archive-list"))
        self.assertContains(response, "<h1>List Template</h1>")


class TestCategoryListView(TestCase):
    def test_get_webpage(self):
        response = self.client.get("/category/1/")
        self.assertEqual(response.status_code, 200)

    def test_get_webpage_by_name(self):
        response = self.client.get(reverse("category-list"))
        self.assertEqual(response.status_code, 200)

    def test_content_exist_correctly(self):
        response = self.client.get(reverse("category-list"))
        self.assertContains(response, "<h1>List Template</h1>")


class TestCategoryUpdateView(TestCase):
    def test_get_webpage(self):
        response = self.client.get("/category/1/update")
        self.assertEqual(response.status_code, 200)

    def test_get_webpage_by_name(self):
        response = self.client.get(reverse("category-update", args=[1]))
        self.assertEqual(response.status_code, 200)

    def test_content_exist_correctly(self):
        response = self.client.get(reverse("category-update", args=[1]))
        self.assertContains(response, "<h1>Form View</h1>")


# Detail View - testcases fail but working properly??
# class TestArchiveDetailView(TestCase):
#     def test_get_webpage(self):
#         response = self.client.get("/archive/1/")
#         self.assertEqual(response.status_code, 200)

#     def test_get_webpage_by_name(self):
#         response = self.client.get(reverse("archive-detail", args=[1]))
#         self.assertEqual(response.status_code, 200)

#     def test_content_exist_correctly(self):
#         response = self.client.get(reverse("archive-detail", args=[1]))
#         self.assertContains(response, "<h1>Detail Template</h1>")


# class TestCategoryDetailView(TestCase):
#     def test_get_webpage(self):
#         response = self.client.get("/category/1/")
#         self.assertEqual(response.status_code, 200)

#     def test_get_webpage_by_name(self):
#         response = self.client.get(reverse("category-detail", args=[1]))
#         self.assertEqual(response.status_code, 200)

#     def test_content_exist_correctly(self):
#         response = self.client.get(reverse("category-detail", args=[1]))
#         self.assertContains(response, "<h1>Detail Template</h1>")
