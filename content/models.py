from ckeditor.widgets import CKEditorWidget
from ckeditor_uploader.fields import RichTextUploadingField
from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from django.forms import ModelForm, TextInput, Select, FileInput
from django.urls import reverse
from django.utils.safestring import mark_safe
from mptt.fields import TreeForeignKey
from mptt.models import MPTTModel


class Menu(MPTTModel):
    STATUS = (
        ('True', 'Evet'),
        ('False', 'Hayır'),
    )
    parent = TreeForeignKey('self', blank=True, null=True, related_name='children', on_delete=models.CASCADE)
    #content = models.OneToOneRel(Content, blank= True, on_delete=models.CASCADE) #relation with Content table
    title = models.CharField(max_length=100, unique=True)
    link = models.CharField(max_length=100, blank=True)
    status = models.CharField(max_length=10, choices=STATUS)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    class MPTTMeta:
        order_insertion_by = ['title']

    def __str__(self):
        full_path = [self.title]
        k = self.parent
        while k is not None:
            full_path.append(k.title)
            k = k.parent
        return ' / '.join(full_path[::-1])
TYPE = (
        ('menu', 'menu'),
        ('haber', 'haber'),
        ('duyuru', 'duyuru'),
        ('etkinlik', 'etkinlik'),
    )
STATUS = (
    ('True', 'Evet'),
    ('False', 'Hayır'),
)


class Content(models.Model):

    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    menu = models.OneToOneField(Menu, null=True, blank=True, on_delete=models.CASCADE) #relation with Menu table
    type = models.CharField(max_length=10, choices=TYPE)
    title = models.CharField(max_length=150)
    keywords = models.CharField(max_length=255, blank=True)
    description = models.CharField(max_length=255, blank=True)
    image = models.ImageField( upload_to='images/')
    detail = RichTextUploadingField()
    slug = models.SlugField(null=False, unique=True)
    status = models.CharField(max_length=10, choices=STATUS)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.title

    def image_tag(self):
        return mark_safe('<img src="{}" height="50"/>'.format(self.image.url))
    image_tag.short_description = 'Image'

    def get_absolute_url(self):
        return reverse('content_detail', kwargs={'slug':self.slug})


class CImage(models.Model):
    content = models.ForeignKey(Content, on_delete=models.CASCADE)
    title = models.CharField(max_length=50, blank=True)
    image = models.ImageField(blank=True, upload_to='images/')
    def __str__(self):
        return self.title

    def image_tag(self):
        return mark_safe('<img src="{}" height="50"/>'.format(self.image.url))
    image_tag.short_description = 'Image'

class ContentImageForm(ModelForm):
    class Meta:
        model = CImage
        fields = ['title', 'image']

class Commentcontent(models.Model):
    STATUS = (
        ('New', 'Yeni'),
        ('True', 'Evet'),
        ('False', 'Hayır'),
    )
    content = models.ForeignKey(Content, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    subject = models.CharField(max_length=500, blank=True)
    comment = models.CharField(max_length=200)
    rate = models.IntegerField()
    status = models.CharField(max_length=10, choices=STATUS, default='New')
    ip = models.CharField(blank=True, max_length=20)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.subject

class CommentForm(ModelForm):
    class Meta:
        model = Commentcontent
        fields = ['subject', 'comment', 'rate']

class ContentForm(ModelForm):
    class Meta:
        model = Content
        fields = ['type', 'title', 'keywords', 'description', 'image', 'detail']
        widgets = {
            'title': TextInput(attrs={'class': 'input', 'placeholder' : 'title'}),
            'keywords': TextInput(attrs={'class': 'input', 'placeholder': 'keywords'}),
            'description': TextInput(attrs={'class': 'input', 'placeholder': 'description'}),
            'type': Select(attrs={'class': 'input', 'placeholder': 'city'}, choices=TYPE),
            'image': FileInput(attrs={'class': 'input', 'placeholder': 'image'}),
            'detail': CKEditorWidget(), #Ckeditor input
        }