from django import forms
from news.models import Post, Comment

filter_choices = (
    ("بازدید - (زیاد به کم)", "بازدید - (زیاد به کم)"),
    ("بازدید - (کم به زیاد)", "بازدید - (کم به زیاد)"),
    ("تاریخ - (جدید به قدیم)", "تاریخ - (جدید به قدیم)"),
    ("تاریخ - (قدیم به جدید)", "تاریخ - (جدید به قدیم)")
)


class FilterForm(forms.Form):
    choice_field = forms.ChoiceField(choices=filter_choices, required=False, label="بر اساس",
                                     widget=forms.Select(attrs={"class": "filter-input"}))
    start_date = forms.DateField(required=False, label="تاریخ شروع",
                                 widget=forms.DateInput(attrs={"class": "filter-input"}))
    end_date = forms.DateField(required=False, label="تاریخ پایان",
                               widget=forms.DateInput(attrs={"class": "filter-input"}))


class NewsForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ["title", "promote", "text", "image"]


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ["text"]


class CommentValidationForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ["is_valid"]
