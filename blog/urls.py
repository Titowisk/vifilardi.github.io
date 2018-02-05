from django.urls import path, re_path

from blog import views

urlpatterns = [
    path('', views.index, name='index'),
    re_path(r'articles/(?P<slug>[\w_-]+)?', views.post, name='post'),
    # re_path(r'my_cv/(?P<slug>[\w_-]+)?', views.curriculum, name='curriculum'),
    # path('pt-br', views.pt_posts, name='pt-br'),
    # path('en', views.en_posts, name='en'),
    re_path(r'category/(?P<slug>[\w_-]+)?', views.posts_list, name='posts_list'),
    path('my_curriculum', views.curriculum, name='curriculum'),

]

# r'^articles/<str:date_published>/(?P<slug>[\w_-]+)?'