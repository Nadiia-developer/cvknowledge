from django.db import models

class Registration(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return str(self.name)

class TheoreticalKnowledge(models.Model):
    theoretical_question = models.CharField(max_length=200, null=True)
    theoretical_answer = models.CharField(max_length=100, null=True)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.theoretical_question
