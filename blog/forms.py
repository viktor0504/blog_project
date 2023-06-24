from django import forms

from .models import Comment, Post, TAG_CHOICES



class AddPostForm(forms.Form):
    title = forms.CharField(max_length=200, widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "Title"}))
    sub_title = forms.CharField(max_length=200, widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "Sub title"}))
    content = forms.CharField(widget=forms.Textarea(attrs={"class": "form-control", "placeholder": "Content"}))
    tag = forms.ChoiceField(choices=TAG_CHOICES)
    social = forms.CharField(max_length=50, widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "Social"}))
    image = forms.ImageField(widget=forms.ClearableFileInput(attrs={"class": "form-control-file"}))
    
    def save(self, author, **kwargs):
        data = self.cleaned_data
        title = data['title']
        sub_title = data['sub_title']
        content = data['content']
        tag = data['tag']
        social = data['social']
        image = data['image']
        
        # Create and save the data
        author_profile = author.profile  # Assuming there's a one-to-one relationship between User and Profile models
        obj = Post(image=image, title=title, sub_title=sub_title, author=author_profile, content=content, tag=tag, social=social)
        obj.save(**kwargs)



class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = [ 'text']
        widgets = {
            'text': forms.Textarea(attrs={'placeholder': 'Your Comment', 'rows': 4}),
        }
    


class CommentEditForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text']
        widgets = {
            'text': forms.Textarea(attrs={'rows': 4}),
        }