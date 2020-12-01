from django import forms


class CommentCreateForm(forms.Form):

    comment = forms.CharField(widget=forms.Textarea)

