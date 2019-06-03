from django.shortcuts import render

from rest_framework import viewsets
from polls.serializers import QuestionSerializer, ChoiceSerializer
from polls.models import Question, Choice


class QuestionViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Questions to be viewed or edited.
    
    list:
    Return a list of all the questions.
    
    retrieve: 
    Return an specific question.
    
    create:
    Creates a new question.
    
    destroy:
    Deletes an specific question.

    update:
    Updates an specific question.

    partial_update:
    Updates an specific question.

    """
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer


class ChoiceViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Choices to be viewed or edited.
    """
    queryset = Choice.objects.all()
    serializer_class = ChoiceSerializer
