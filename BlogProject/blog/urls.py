from django.urls import path

from . import views

app_name = 'blog'
urlpatterns = [
    path('blog/', views.index, name='index'),
    path('blog/posts/<int:pk>/', views.detail, name='detail'),
]