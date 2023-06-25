from django.db import models
from django.utils import timezone

from django.utils.text import slugify
from profiles.models import Profile

from user.models import User


TAG_CHOICES = [
        ('Research', 'Research'),
        ('News', 'News'),
        ('Games', 'Games'),
        ('Technology', 'Technology'),
        ('Health', 'Health'),
        ('Science', 'Science'),
        ('Enviroment', 'Enviroment'),
        ('Physics', 'Physics'),
        ('Earth', 'Earth'),
]



class Post(models.Model):
    title = models.CharField(max_length=200)
    sub_title = models.CharField(max_length=200)
    author = models.ForeignKey(Profile, on_delete=models.CASCADE)
    content = models.TextField()
    tag = models.CharField(choices=TAG_CHOICES, max_length=15)
    image = models.ImageField(upload_to='post/')
    social = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(blank=True, null=True)

    class Meta:
        app_label = 'blog'

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if self.slug == None:
            slug = slugify(self.title[:50])
            has_slug = Post.objects.filter(slug=slug).exists()
            count = 1
            while has_slug:
                count += 1
                slug=slugify(self.title) + '-' + str(count)
                has_slug = Post.objects.filter(slug=slug).exists()
            self.slug = slug
        super().save(*args, **kwargs)



class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    approved_com = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
            app_label = 'blog'
            
    def __str__(self):
        return f'{self.author} - {self.text}' 