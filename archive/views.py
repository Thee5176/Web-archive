from django.urls import reverse_lazy
from django.views.generic import (
    TemplateView,
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)

from .models import WebArchive, Category


class HomepageView(TemplateView):
    template_name = "archive/home.html"


# Archive
class ArchiveListView(ListView):
    model = WebArchive
    template_name = "archive/list.html"
    context_object_name = "weblist"


class ArchiveDetailView(DetailView):
    model = WebArchive
    template_name = "archive/detail.html"
    context_object_name = "web"


class ArchiveUpdateView(UpdateView):
    model = WebArchive
    fields = "__all__"
    template_name = "archive/form.html"


class ArchiveCreateView(CreateView):
    model = WebArchive
    fields = "__all__"
    template_name = "archive/form.html"


class ArchiveDeleteView(DeleteView):
    model = WebArchive
    fields = "__all__"
    template_name = "archive/delete.html"
    success_url = reverse_lazy("archive-list")


# Category
class CategoryListView(ListView):
    model = Category
    template_name = "archive/list.html"
    context_object_name = "catlist"


class CategoryDetailView(DetailView):
    model = Category
    template_name = "archive/detail.html"
    context_object_name = "cat"


class CategoryUpdateView(UpdateView):
    model = Category
    fields = "__all__"
    template_name = "archive/form.html"


class CategoryCreateView(CreateView):
    model = Category
    fields = "__all__"
    template_name = "archive/form.html"


class CategoryDeleteView(DeleteView):
    model = Category
    template_name = "archive/delete.html"
    success_url = reverse_lazy("category-list")
