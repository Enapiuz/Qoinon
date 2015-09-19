from django.db import models


class FaqCategory(models.Model):
    title_en = models.CharField(max_length=200)

    def __str__(self):
        return self.title_en

class FaqItem(models.Model):
    question = models.CharField(max_length=500)
    answer = models.TextField(blank=True)
    visible = models.BooleanField(default=True)
    category = models.ForeignKey(FaqCategory, default=None, null=True)
    position = models.IntegerField(default=0)

    def __str__(self):
        if self.category is not None:
            cat = '[' + self.category.title_en + '] '
        else:
            cat = ''
        return cat + self.question

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