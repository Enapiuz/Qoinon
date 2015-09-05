from django.db import models


class FaqItem(models.Model):
    question = models.CharField(max_length=500)
    answer = models.TextField(blank=True)

    def __str__(self):
        return self.question