from .models import Artiles, Comment, Tag
from django.forms import ModelForm, TextInput, DateTimeInput, Textarea, SelectMultiple


class ArtilesForm(ModelForm):
    class Meta:
        model = Artiles
        fields = ['title', 'anons', 'full_text', 'tags']  # Добавляем поле tags

        widgets = {
            "title": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Название статьи'
            }),
            "anons": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Анонс статьи'
            }),

            "full_text": Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Текст статьи'
            }),
            "tags": SelectMultiple(attrs={
                'class': 'form-control'
            }),
        }


class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['content']  # Убираем поле `author`
        widgets = {
            'content': Textarea(attrs={'class': 'form-control', 'placeholder': 'Ваш комментарий'}),
        }


    # Метод для общей валидации
    def clean(self):
        cleaned_data = super().clean()

        content = cleaned_data.get("content")

        if not content:
            self.add_error('content', 'Поле "Комментарий" не может быть пустым!')