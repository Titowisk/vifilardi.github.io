from django.views.generic import ListView, DetailView
from .models import Post

# Create your views here.

class IndexView(ListView):

    template_name="blog/index.html"
    model = Post
    context_object_name = "post_list"
    # pagination?

class PostView(DetailView):
    
    template_name = "blog/post.html"
    model = Post
    context_object_name = "post"    

class PortuguesePostsView(ListView):
    
    template_name = "blog/portuguese_posts.html"
    context_object_name = "pt_br_posts"
    # pagination?

    def get_queryset(self):
        
        queryset = Post.objects.filter(language="portuguese-br") 

        return queryset


index = IndexView.as_view()
post = PostView.as_view()
pt_posts = PortuguesePostsView.as_view()