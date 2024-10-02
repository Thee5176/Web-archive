from django.shortcuts import render
from django.views.generic import (
    TemplateView,
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)

from .models import WebArchive, Catagory


class HomepageView(TemplateView):
    template_name = "archive/home.html"


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


class CategoryListView(ListView):
    model = Catagory
    template_name = "archive/list.html"
    context_object_name = "catlist"


class CategoryDetailView(DetailView):
    model = Catagory
    template_name = "archive/detail.html"
    context_object_name = "cat"
