from django.urls import path
from .views import (
    HomepageView,
    ArchiveListView,
    CategoryListView,
    ArchiveDetailView,
    CategoryDetailView,
    ArchiveUpdateView,
    ArchiveCreateView,
    ArchiveDeleteView,
)


urlpatterns = [
    path("", HomepageView.as_view(), name="home"),
    path("archive/", ArchiveListView.as_view(), name="archive-list"),
    path("archive/<int:pk>/", ArchiveDetailView.as_view(), name="archive-detail"),
    path("archive/<int:pk>/update", ArchiveUpdateView.as_view(), name="archive-update"),
    path("archive/<int:pk>/delete", ArchiveDeleteView.as_view(), name="archive-delete"),
    path("archive/create", ArchiveCreateView.as_view(), name="archive-create"),
    path("category/", CategoryListView.as_view(), name="category-list"),
    path("category/<int:pk>/", CategoryDetailView.as_view(), name="category-detail"),
]
