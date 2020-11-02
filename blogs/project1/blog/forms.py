from blog.models import Blog
from django.forms import ModelForm


class BlogForm(ModelForm):
    class Meta:
        model = Blog
        exclude = ['created_by','slug']