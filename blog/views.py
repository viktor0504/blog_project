import random

from django.shortcuts import get_object_or_404, redirect, render
from django.db.models import DateTimeField
from django.db.models.functions import TruncMonth
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView, DeleteView
from django.views.generic.edit import FormMixin, FormView
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.mail import EmailMessage
from django.urls import reverse

from .forms import AddPostForm, CommentForm, CommentEditForm
from .models import Post, Comment
from user.models import User



@login_required
def subscribe(request):
    # Get the email address from the authenticated user (you may modify this based on your implementation)
    email = request.user.email
    
    # Create and send the subscription email
    subject = 'Subscription Confirmation'
    message = f'Thank you for subscribing! You will now receive updates via email.'
    from_email = 'viktor.05040504@gmail.com'
    to_email = [email]

    email_message = EmailMessage(subject, message, from_email, to_email)
    email_message.send()

    # Redirect back to the home page or any other desired page
    return redirect(reverse('home'))



@login_required
def search_results(request):
    query = request.GET.get('query')
    if query:
        results = Post.objects.filter(title__icontains=query)
    else:
        results = []
    return render(request, 'blog/search_results.html', {'results': results, 'query': query})



@login_required
def comment_edit(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    #import pdb;pdb.set_trace()
    if request.method == 'POST':
        form = CommentEditForm(request.POST, instance=comment)
        if form.is_valid():
            form.save()
            return redirect('blog:blog_detail', slug=comment.post.slug)
    else:
        form = CommentEditForm(instance=comment)
    return render(request, 'blog/comment_edit.html', {'form': form, 'comment': comment})



@login_required
def comment_delete(request, comment_pk):
    comment = Comment.objects.get(pk=comment_pk)
    # Add your logic for deleting the comment
    if request.method == 'POST':
        # Delete the comment
        comment.delete()
        messages.success(request, 'Comment deleted successfully.')
        return redirect('blog:blog_detail', slug=comment.post.slug)
    return render(request, 'blog/comment_delete.html', {'comment': comment})



class PostCreate(LoginRequiredMixin, FormView):
    form_class = AddPostForm
    template_name = 'blog/add_post.html'
    success_url = reverse_lazy('blog:blog_home')
    
    def form_valid(self, form, **kwargs):
        form.save(author=self.request.user,  **kwargs)
        return super().form_valid(form)



class ArchivesListView(LoginRequiredMixin, ListView):
    model = Post
    template_name = 'blog/blog_archives.html'
    context_object_name = 'posts'
    
    def get(self, request, year):
        posts = Post.objects.filter(created_at__year=year)
        context = {'year': year, 'posts': posts}
        #import pdb;pdb.set_trace()
        return render(request, 'blog/blog_archives.html', context)



class BlogListView(LoginRequiredMixin, ListView):
    model = Post
    template_name = 'blog/blog_list.html'
    context_object_name = 'posts'
    
    def get_queryset(self):
        tag = self.kwargs.get('tag')
        queryset = super().get_queryset()
        filtered_posts = queryset.filter(tag=tag)
        
        return filtered_posts



class BlogHomeView(LoginRequiredMixin, ListView):
    model = Post
    template_name = 'blog/blog_home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        posts = Post.objects.all()
        random_post = random.choice(posts)
        context['post'] = random_post
        
        #Get the first post of all times
        context['older_post'] = Post.objects.order_by('-created_at').last()
        #Get me the last post
        context['recent_post'] = Post.objects.order_by('created_at').last()

        context['news_posts'] = Post.objects.order_by('created_at')[:6]
        #import pdb;pdb.set_trace()

        context['authors'] = User.objects.all()

        filtered_objects = Post.objects.annotate(month_year=TruncMonth('created_at', output_field=DateTimeField())).values('month_year').distinct().order_by('month_year')
        
        context['filtered_objects']= filtered_objects

        
        return context



class PostDetailView(LoginRequiredMixin, FormMixin, DetailView):
    model = Post
    template_name = 'blog/blog_detail.html'
    context_object_name = 'post_detail'
    form_class = CommentForm

    def get_success_url(self):
        return reverse_lazy('blog:blog_detail', kwargs={'slug': self.object.slug})

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = self.get_form()
        if form.is_valid():
            # Process the form data
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        form.instance.post = self.object
        form.instance.author = self.request.user
        form.save()
        return super().form_valid(form)



class PostDeleteView(LoginRequiredMixin, DeleteView):
    model = Post
    template_name = 'blog/delete_post.html'
    success_url = '/blog/'