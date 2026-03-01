from django.views import generic


class IndexView(generic.ListView):
    template_name = "correlations/index.html"
    context_object_name = "latest_entries"

    def get_queryset(self) -> list:
        return ["hello"]


# # Create your views here.
# def index(request) -> HttpResponse:
#     return HttpResponse("Hello World")


# class IndexView(generic.ListView):
#     template_name = "polls/index.html"
#     context_object_name = "latest_question_list"

#     def get_queryset(self):
#         """Return the last five published questions."""
#         return Question.objects.filter(pub_date__lte=timezone.now()).order_by(
#             "-pub_date"
#         )[:5]
