from blog.models import Blog
from django.forms import ModelForm,CharField
from ckeditor.widgets import CKEditorWidget

class BlogForm(ModelForm):
    class Meta:
        model = Blog
        exclude = ['created_by','slug']