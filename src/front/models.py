from django.db import models


class FaqItem(models.Model):
    question = models.CharField(max_length=500)
    answer = models.TextField(blank=True)

    def __str__(self):
        return self.question

class ContactForm(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=200)
    text = models.TextField(max_length=5000)
    solved = models.BooleanField(default=False)

    def __str__(self):
        if self.solved:
            solved = '[solved] '
        else:
            solved = ''
        return solved + '[' + self.name + ']: ' + self.text[:20] + '...'