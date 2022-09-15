from django.shortcuts import render
from django.template import loader
from blogging.models import Post
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

# Create your views here.

class PostListView(ListView):
    Model = Post
    queryset = Post.objects.order_by("-published_date")
    template_name = "blogging/list.html"


class PostDetailView(DetailView):
    Model = Post
    queryset = Post.objects.exclude(published_date__exact=None)
    template_name = "blogging/detail.html"
