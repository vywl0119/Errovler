from cProfile import label
from importlib.resources import contents
from unicodedata import category
from attr import field
from bleach import clean
from django import forms

from Mainapp.models import Board
from django_summernote.fields import SummernoteTextField
from django_summernote.widgets import SummernoteWidget

class BoardPost(forms.ModelForm):
    title = forms.CharField(
        label='글 제목',
        widget=forms.TextInput(
            attrs={
                'placeholder': '게시글 제목'
            }),
    )

    contents = SummernoteTextField()
    
    options = (
        ('Python', '파이썬'),
        ('Django', '장고'),
        ('etc', '기타'),
    )

    category = forms.ChoiceField(
        label='카테고리 선택',
        widget=forms.Select(),
        choices=options
    )

    field_order = ['title','category','contents']

    class Meta:
            model = Board
            fields = ['title','category', 'contents'] 
            widgets = {
                'contents' : SummernoteWidget()
            }
    def clean(self):
        cleaned_data = super().clean()

        title = cleaned_data.get('title', '')
        category = cleaned_data.get('category','Django')
        contents = cleaned_data.get('contents','')

        if title == '':
            self.add_error('title', '글 제목을 입력하세요.')
        elif contents == '':
            self.add_error('contents','글 내용을 입력하세요.')
        else:
            self.title = title
            self.category = category
            self.contents = contents
