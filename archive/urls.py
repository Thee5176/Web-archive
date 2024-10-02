from django.urls import path
from .views import (
    HomepageView,
    ArchiveListView,
    CategoryListView,
    ArchiveDetailView,
    CategoryDetailView,
)


urlpatterns = [
    path("", HomepageView.as_view(), name="home"),
    path("archive/", ArchiveListView.as_view(), name="archive-list"),
    path("archive/<int:pk>/", ArchiveDetailView.as_view(), name="archive-detail"),
    path("category/", CategoryListView.as_view(), name="category-list"),
    path("category/<int:pk>/", CategoryDetailView.as_view(), name="category-detail"),
]
