from django import forms

from .models import Task_post

class PostForm(forms.ModelForm):

    class Meta:
        model = Task_post
        fields = ('title', 'description', 'status', 'priority', 'category')