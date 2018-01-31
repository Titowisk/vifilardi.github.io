from django.views.generic import ListView, TemplateView
from .models import Post

# Create your views here.

class IndexView(ListView):

    template_name="blog/index.html"
    model = Post
    context_object_name = "post_list"

index = IndexView.as_view()