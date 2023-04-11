from django import forms
from .models import Article, Comment
# forms.py

# article을 위한 form(html form)을 만들어주는 class
# class convention -> PascalCase
# Model정보를 기반으로 만들어지는 Form
class ArticleForm(forms.ModelForm):
    # Model 정보도 함께 가지고 있어야 겠다.
    class Meta:
        # model = ModelClass -> ModelClass에 정의된 각종 필드들을 그대로 활용
        model = Article
        # title - CharField, content - TextField
        fields = '__all__'

# Model정보를 기반으로 만들어지는 Form
class CommentForm(forms.ModelForm):
    # Model 정보도 함께 가지고 있어야 겠다.
    class Meta:
        # model = ModelClass -> ModelClass에 정의된 각종 필드들을 그대로 활용
        model = Comment
        # title - CharField, content - TextField
        # fields = '__all__'
        fields = ('content', )
        # exclude = ('article', )

