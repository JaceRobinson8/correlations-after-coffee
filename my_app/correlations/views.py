from django.shortcuts import render
from django.utils import timezone
from django.views import generic

from .models import Post


def post_list(request):
    posts = Post.objects.filter(published_at__lte=timezone.now())
    return render(request, "blog/post_list.html", {"posts": posts})


class DetailView(generic.DetailView):
    template_name = "correlations/detail.html"
    context_object_name = "entry"
