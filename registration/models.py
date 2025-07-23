from django.db import models
import random

from django.db import models

class Quiz(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.title

class Question(models.Model):
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE, related_name='questions')
    text = models.TextField()

    def __str__(self):
        return f"{self.text[:50]}..."

class Option(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='options')
    text = models.CharField(max_length=255)
    type = models.CharField(max_length=1, choices=[('A', 'A'), ('B', 'B'), ('C', 'C')])

    def __str__(self):
        return f"{self.text} ({self.type})"

class ResultTip(models.Model):
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE, related_name='tips')
    type = models.CharField(max_length=1, choices=[('A', 'A'), ('B', 'B'), ('C', 'C')])
    do = models.TextField(blank=True)
    dont = models.TextField(blank=True)
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)

    def __str__(self):
        return f"{self.type} Tip for {self.quiz.title}"
