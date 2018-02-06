from django.urls import path, re_path

from blog import views

urlpatterns = [
    path('', views.index, name='index'),
    re_path(r'articles/(?P<slug>[\w_-]+)?', views.post, name='post'),
    re_path(r'category/(?P<slug>[\w_-]+)?', views.posts_list, name='posts_list'),
    path('my_curriculum', views.curriculum, name='curriculum'),
    path('tags', views.tags, name='tags'),
    re_path(r'tags/(?P<slug>[\w_-]+)?', views.posts_list_by_tag, name='posts_list_by_tag'),

]

# r'^articles/<str:date_published>/(?P<slug>[\w_-]+)?'