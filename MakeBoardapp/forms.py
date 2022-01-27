from cProfile import label
from importlib.resources import contents
from unicodedata import category
from attr import field
from bleach import clean
from django import forms
from matplotlib.pyplot import title
from Mainapp.models import Total_Board
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

    contents = forms.CharField(widget=SummernoteWidget())
    
    type_options = (
        ('질문', '질문'),
        ('해결', '해결')
    )

    type = forms.ChoiceField(
        label='질문/해결 선택',
        widget=forms.Select(),
        choices=type_options
    )

    category_options = (
        ('Python', '파이썬'),
        ('Django', '장고'),
        ('etc', '기타'),
    )

    category = forms.ChoiceField(
        label='카테고리 선택',
        widget=forms.Select(),
        choices=category_options
    )

    field_order = ['title','type','category','contents']

    class Meta:
            model = Total_Board
            fields = ['title','type','category', 'contents'] 
            widgets = {
                'contents' : SummernoteWidget()
            }

    def clean(self):
        cleaned_data = super().clean()

        title = cleaned_data.get('title', '')
        type = cleaned_data.get('type','질문')
        category = cleaned_data.get('category','Django')
        contents = cleaned_data.get('contents','')

        if title == '':
            self.add_error('title', '글 제목을 입력하세요.')
        elif contents == '':
            self.add_error('contents','글 내용을 입력하세요.')
        else:
            self.title = title
            self.type = type
            self.category = category
            self.contents = contents
