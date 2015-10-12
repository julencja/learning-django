from django.db import models
from django.forms import ModelForm
from django.contrib.auth.models import User

# Create your models here.

class Foo(models.Model):
    bar = models.CharField(max_length=100)
    date_added = models.DateTimeField('date added')
    author = models.ForeignKey(User)

    def __unicode__(self):
        return self.bar

class FooForm(ModelForm):
    class Meta: 
        model = Foo
        fields = ['bar']



