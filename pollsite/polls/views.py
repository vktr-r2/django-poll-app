from django.http import HttpResponse, HttpResponseRedirect
from django.views import View
from django.views.generic import TemplateView
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.db.models import F

from .models import Question, Choice


class IndexView(TemplateView):

    def get(self, request):
        latest_questions_list = Question.objects.order_by("-pub_date")[:5]
        context = {"latest_questions_list": latest_questions_list}
        return render(request, "polls/index.html", context)


class DetailView(TemplateView):

    def get(self, request, question_id):
        question = get_object_or_404(Question, pk=question_id)
        return render(request, "polls/detail.html", {"question": question})


class ResultsView(TemplateView):

    def get(self, request, question_id):
        response = (f"You're looking at the results of question {question_id}.")
        return HttpResponse(response, question_id)


class VoteView(View):

    def post(self, request, question_id):
        question = get_object_or_404(Question, pk=question_id)

        try:
            selected_choice = question.choice_set.get(pk=request.POST["choice"])
        except (KeyError, Choice.DoesNotExist):
            # Redisplay the question voting form.
            return render(
                request,
                "polls/detail.html",
                {
                    "question": question,
                    "error_message": "You didn't select a choice.",
                },
            )
        else:
            selected_choice.votes = F("votes") + 1
            selected_choice.save()
            # Always redirect after a POST, this prevents data from being posted twice if a user hits Back button
            return HttpResponseRedirect(reverse("polls:results", args=(question.id,)))
