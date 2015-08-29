from django.db import models


class FaqItem(models.Model):
    question = models.TextField()
    answer = models.TextField(blank=True)

    def __str__(self):
        return self.question