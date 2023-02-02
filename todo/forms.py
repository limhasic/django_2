from django import forms
from .models import Todo


class TodoForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = ('title', 'description', 'important')

        # 입력 폼 지정