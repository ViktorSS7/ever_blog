from django import forms


class CommentCreateForm(forms.Form):

    your_name = forms.CharField(label='Your name', max_length=100)
    comment = forms.CharField(widget=forms.Textarea)

