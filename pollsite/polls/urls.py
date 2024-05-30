from django.urls import path
from .views import IndexView, DetailView, ResultsView, VoteView

app_name = "polls"
urlpatterns = [

    # index of questions
    path("", IndexView.as_view(), name="index"),

    # specific question ex:/polls/5/
    path("<int:question_id>/", DetailView.as_view(), name="detail"),

    # question results ex:/polls/5/results
    path("<int:question_id>/results/", ResultsView.as_view(), name="results"),

    # question vote ex:/polls/5/vote
    path("<int:question_id>/vote/", VoteView.as_view(), name="vote"),

]
