from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Question(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    question_text = models.CharField(max_length=200)
    enquiry_date = models.DateTimeField("date enquired", auto_now_add=True)

    def __str__(self) -> str:
        return self.question_text
    
    def was_enquired_on(self):
        return self.enquiry_date