from django.views.generic import ListView, DetailView
from .models import Post

# Create your views here.

class IndexView(ListView):

    template_name="blog/index.html"
    model = Post
    context_object_name = "post_list"

class PostView(DetailView):
    
    template_name = "blog/post.html"
    model = Post
    context_object_name = "post"    

index = IndexView.as_view()
post = PostView.as_view()