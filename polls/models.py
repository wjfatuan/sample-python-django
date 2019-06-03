from django.db import models

class Question(models.Model):
    """
    Stores a poll question.
    """
    question_text = models.CharField(max_length=200, help_text="The question text")
    pubished_date = models.DateTimeField(help_text="Publishing date")

class Choice(models.Model):
    """
    Stores a poll question choice. Related to :model:`polls.Question`
    """
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200, help_text="The text that will appear for this choice")
    votes = models.IntegerField(default=0, help_text="The number of times the choice has been voted")
