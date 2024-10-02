from django.urls import path
from .views import HomepageView, ArchiveListView


urlpatterns = [
    path("", HomepageView.as_view(), name="home"),
    path("archive/", ArchiveListView.as_view(), name="archive-list"),
]
