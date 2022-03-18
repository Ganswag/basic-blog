from ckeditor.widgets import CKEditorWidget
from django import forms
from .models import Article


class ArticleForm(forms.ModelForm):

    class Meta:
        model = Article
        fields = ('title', 'slug', 'main_picture', 'content')
        widgets = {
            'title': forms.TextInput(
                attrs={'class': 'form-control', 'placeholder': 'Título'}
            ),
            'slug': forms.TextInput(
                attrs={'class': 'form-control', 'placeholder': 'Slug'}
            ),
            'main_picture': forms.ClearableFileInput(
                attrs={'class': 'form-control-file mt-3'}
            ),
            'content': forms.CharField(widget=CKEditorWidget())
        }

        labels = {
            'title': '', 'slug': '', 'content': ''
        }
