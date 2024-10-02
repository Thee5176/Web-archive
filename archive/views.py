from django.shortcuts import render
from django.views.generic import TemplateView, ListView

from .models import WebArchive, Catagory


class HomepageView(TemplateView):
    template_name = "archive/home.html"


class ArchiveListView(ListView):
    model = WebArchive
    template_name = "archive/list.html"
    context_object_name = "weblist"
