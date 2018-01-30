from django.views.generic import ListView, TemplateView

# Create your views here.

class IndexView(TemplateView):

    template_name="blog/index.html"

index = IndexView.as_view()