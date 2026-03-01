from django.shortcuts import render
from django.utils import timezone
from django.views import generic

from .models import Post


class IndexView(generic.ListView):
    template_name = "correlations/index.html"
    context_object_name = "latest_entries"

    def get_queryset(self) -> list:
        return Post.objects.all()
        # return Post.objects.filter(published_at__lte=timezone.now())


# def post_list(request):
#     posts = Post.objects.filter(published_at__lte=timezone.now())
#     return render(request, "blog/post_list.html", {"posts": posts})


class DetailView(generic.DetailView):
    template_name = "correlations/detail.html"
    context_object_name = "entry"
