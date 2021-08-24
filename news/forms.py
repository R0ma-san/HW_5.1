from django import forms
from .models import News

class NewsForm(forms.ModelForm):
    title = forms.CharField(max_length=255)
    body = forms.TextInput

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['title'].label = 'Заголовок'
        self.fields['body'].label = 'Текст'

    class Meta:
        model = News
        fields = ('title', 'body', 'editor_name')