from django.urls import path, re_path

from blog import views

urlpatterns = [
    path('', views.index, name='index'),
    path('articles/', views.post, name='post'),
]

# r'^articles/<str:date_published>/(?P<slug>[\w_-]+)/?'