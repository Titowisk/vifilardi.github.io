from django.views.generic import ListView, DetailView
from .models import Post

# Create your views here.

class IndexView(ListView):

    template_name="blog/index.html"
    model = Post
    context_object_name = "post_list"

class PostView(ListView):
    
    template_name = "blog/post.html"
    model = Post
    context_object_name = "post"

    def get_context_data(self, **kwargs):
        context = super(PostView, self).get_context_data(**kwargs)
        context['post_test'] = Post.objects.get(id=3)

        return context
    

index = IndexView.as_view()
post = PostView.as_view()