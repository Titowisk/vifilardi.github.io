from django.views.generic import ListView, DetailView, TemplateView
from .models import Post

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


index = IndexView.as_view()
post = PostView.as_view()
curriculum = CurriculumView.as_view()
pt_posts = PortuguesePostsView.as_view()
en_posts = EnglishPostsView.as_view()