# from django.db import models

# Create your models here.
from django.db import models

class ChatResponse(models.Model):
    input_text = "hello"
    response_text = "I am a chatbot"

