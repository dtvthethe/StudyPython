from django import forms


class QuestionForm(forms.Form):
    question_text = forms.CharField(max_length=100, label='Question Label')
    email = forms.EmailField(error_messages={'invalid':'Oops! Wrong format Email :D'})
