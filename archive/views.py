from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView

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


class CategoryListView(ListView):
    model = Catagory
    template_name = "archive/list.html"
    context_object_name = "catlist"


class CategoryDetailView(DetailView):
    model = Catagory
    template_name = "archive/detail.html"
    context_object_name = "cat"
