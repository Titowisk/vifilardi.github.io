from django.views.generic import ListView, DetailView, TemplateView
from django.shortcuts import get_object_or_404

from .models import Post, Category, Tag

class IndexView(ListView):

    template_name="blog/index.html"
    model = Post
    # context_object_name = "post_list"
    # pagination?

    def get_queryset(self):
        # only posted filters and exclude Curriculum post
        posted_post_list = Post.objects.filter(status="Published").exclude(slug="curriculum")
        
        # sort posts by posted date (latest first)
        posted_post_list = sorted(posted_post_list, reverse=True, key=lambda x:x.posted)

        return posted_post_list

    def get_context_data(self, **kwargs):

        context = super(IndexView, self).get_context_data(**kwargs)

        # custom queryset for latest posted posts only and without curriculum post
        context['post_list'] = self.get_queryset()

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

    def get_queryset(self):
        posted_post_list_by_category = Post.objects.filter(
            category__slug=self.kwargs['slug']
        ).filter(
            status="Published"
        )
        
        return sorted(posted_post_list_by_category, reverse=True, key=lambda x:x.posted)

    # what is wrong here??
    def get_context_data(self, **kwargs):
        context = super(PostsListView, self).get_context_data(**kwargs)
        context['post_list'] = self.get_queryset()
        context['category'] = Category.objects.get(slug=self.kwargs['slug'])
        return context 


class TagsView(ListView):
    
    template_name = 'blog/tags.html'
    model = Tag
    context_object_name = 'tag_list'
    

class PostListByTag(ListView):

    template_name = 'blog/posts_list_by_tag.html'
    context_object_name = 'received_tag_slug'

    def get_queryset(self):
        queryset = Tag.objects.get(slug=self.kwargs['slug'])
        return queryset


index = IndexView.as_view()
post = PostView.as_view()
curriculum = CurriculumView.as_view()
posts_list = PostsListView.as_view()
tags = TagsView.as_view()
posts_list_by_tag = PostListByTag.as_view()