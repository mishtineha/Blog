from django.db import models
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
from django.contrib.auth.models import User

class Blog(models.Model):
    title = models.CharField(max_length = 20)
    description = models.CharField(max_length = 100)
    slug = models.CharField(max_length = 20,default = None,null = True,unique = True)
    created_by = models.ForeignKey(User,on_delete = models.CASCADE,default = None,null = True)
    created_at = models.DateTimeField(auto_now_add = True)
    content = models.TextField(max_length = 2500)
    cover = models.ImageField(upload_to = 'files/',default = None,null = True)

    # def save(self,**kwargs):
    #     self.slug = ("-").join(self.title.split(" ")) + "-" + self.id
    #     self.save()
    #     super(self,**kwargs).save()

# Create your models here.
