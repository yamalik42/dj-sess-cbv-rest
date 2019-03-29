from django.db import models
from django.forms import ModelForm

# Create your models here.
class Author(models.Model):
    first_name = models.CharField(max_length=21)
    last_name = models.CharField(max_length=21)

class AuthorForm(ModelForm):
    class Meta:
        model = Author
        fields = ['first_name', 'last_name']
