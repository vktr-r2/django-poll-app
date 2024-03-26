from django.http import HttpResponse
from django.views import View
from django.views.generic import TemplateView
from django.shortcuts import render, get_object_or_404

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


class VoteView(TemplateView):
    
    def post(self, request, question_id):
        response = (f"You're voting on question {question_id}")
        return HttpResponse(response, question_id)
