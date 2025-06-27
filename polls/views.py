from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import generic

from .models import Question, Choice
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Question

class IndexView(generic.ListView):
    template_name = "polls/index.html"
    context_object_name = "latest_question_list"

    def get_queryset(self):
        return Question.objects.order_by("-pub_date")[:5]


class DetailView(generic.DetailView):
    model = Question
    template_name = "polls/detail.html"


class ResultsView(generic.DetailView):
    model = Question
    template_name = "polls/results.html"

class QuestionCreateView(CreateView):
    model = Question
    fields = ["question_text", "pub_date"]
    template_name = "polls/question_form.html"

class QuestionUpdateView(UpdateView):
    model = Question
    fields = ["question_text", "pub_date"]
    template_name = "polls/question_form.html"

class QuestionDeleteView(DeleteView):
    model = Question
    success_url = "/polls/"
    template_name = "polls/question_confirm_delete.html"


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST["choice"])
    except (KeyError, Choice.DoesNotExist):
        return render(request, "polls/detail.html", {
            "question": question,
            "error_message": "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse("polls:results", args=(question.id,)))
