from .models import Comment, RATE_CHOICE
from django import forms


class CommentForm(forms.ModelForm):
    rating = forms.ChoiceField(choices=RATE_CHOICE, widget=forms.Select(), required=True)

    class Meta:
        model = Comment
        fields = ('name', 'rating', 'body')
