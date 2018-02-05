from django.views.generic import ListView, DetailView, TemplateView
from django.shortcuts import get_object_or_404
from .models import Post, Category

# Create your views here.

class IndexView(ListView):

    template_name="blog/index.html"
    model = Post
    context_object_name = "post_list"
    # pagination?

    def get_context_data(self, **kwargs):

        context = super(IndexView, self).get_context_data(**kwargs)
        curriculum_post = Post.objects.get(slug='curriculum')
        context['slug'] = curriculum_post.slug
        # context['categories'] = Category.objects.all()

        return context


class PostView(DetailView):
    
    template_name = "blog/post.html"
    model = Post
    context_object_name = "post"   

class CurriculumView(TemplateView):
    
    template_name = "blog/curriculum.html"

    def get_context_data(self, **kwargs):
        context = super(CurriculumView, self).get_context_data(**kwargs)
        context['curriculum'] = Post.objects.get(slug='curriculum')
        return context

class PostsListView(ListView):
    
    template_name = 'blog/posts_list.html'
    context_object_name = 'posts_list'

    def get_queryset(self):
        queryset = Post.objects.filter(category__slug=self.kwargs['slug'])
        return queryset

    # what is wrong here??
    def get_context_data(self, **kwargs):
        context = super(PostsListView, self).get_context_data(**kwargs)
        context['category'] = Category.objects.get(slug=self.kwargs['slug'])
        return context 

index = IndexView.as_view()
post = PostView.as_view()
curriculum = CurriculumView.as_view()
posts_list = PostsListView.as_view()
# pt_posts = PortuguesePostsView.as_view()
# en_posts = EnglishPostsView.as_view()

    
"""
class PortuguesePostsView(ListView):
    
    template_name = "blog/portuguese_posts.html"
    context_object_name = "pt_br_posts"
    # pagination?

    def get_queryset(self):
        queryset = Post.objects.filter(language="portuguese-br") 
        return queryset

class EnglishPostsView(ListView):
    
    template_name = "blog/english_posts.html"
    context_object_name = "en_posts"
    # pagination?

    def get_queryset(self):
        
        queryset = Post.objects.filter(language="english") 

        return queryset
"""