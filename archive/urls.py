from django.urls import path
from .views import (
    HomepageView,
    ArchiveListView,
    CategoryListView,
    ArchiveDetailView,
    CategoryDetailView,
    ArchiveUpdateView,
    CategoryUpdateView,
    ArchiveCreateView,
    CategoryCreateView,
    ArchiveDeleteView,
    CategoryDeleteView,
)


urlpatterns = [
    path("", HomepageView.as_view(), name="home"),
    path("archive/", ArchiveListView.as_view(), name="archive-list"),
    path("archive/create", ArchiveCreateView.as_view(), name="archive-create"),
    path("archive/<int:pk>/", ArchiveDetailView.as_view(), name="archive-detail"),
    path("archive/<int:pk>/update", ArchiveUpdateView.as_view(), name="archive-update"),
    path("archive/<int:pk>/delete", ArchiveDeleteView.as_view(), name="archive-delete"),
    path("category/", CategoryListView.as_view(), name="category-list"),
    path("category/create", CategoryCreateView.as_view(), name="category-create"),
    path("category/<int:pk>/", CategoryDetailView.as_view(), name="category-detail"),
    path(
        "category/<int:pk>/update", CategoryUpdateView.as_view(), name="category-update"
    ),
    path(
        "category/<int:pk>/delete", CategoryDeleteView.as_view(), name="category-delete"
    ),
]
