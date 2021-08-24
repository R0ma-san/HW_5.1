from django import forms
from .models import Question

class QuestionsForm(forms.ModelForm):
    first_name = forms.CharField(max_length=100, required=True)
    email = forms.EmailField(required=True)
    question = forms.TextInput 

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['first_name'].label = 'Имя'
        self.fields['email'].label = 'Почта'
        self.fields['question'].label = 'Вопрос'

    class Meta:
        model = Question
        fields = ('first_name', 'email', 'question')