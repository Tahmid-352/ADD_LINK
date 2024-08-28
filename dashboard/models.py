from django.contrib.auth.models import User
from django.db import models
from datetime import date

class Button(models.Model):
    title = models.CharField(max_length=255)
    link = models.URLField()
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='created_buttons')
    last_clicked = models.DateField(null=True, blank=True)
    users_clicked = models.ManyToManyField(User, through='ButtonClick', related_name='clicked_buttons')

    def __str__(self):
        return self.title

class ButtonClick(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    button = models.ForeignKey(Button, on_delete=models.CASCADE)
    clicked_date = models.DateField(default=date.today)
