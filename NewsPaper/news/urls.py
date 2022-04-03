from django.urls import path
from .views import PostList, SearchList, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView

urlpatterns = [
    path('', PostList.as_view()),
    path('search/', SearchList.as_view()),
    path('<int:pk>/', PostDetailView.as_view(), name='post_detail'),  # Ссылка на детали товара
    path('create/', PostCreateView.as_view(), name='post_create'),  # Ссылка на создание товара
    path('create/<int:pk>', PostUpdateView.as_view(), name='post_update'),
    path('delete/<int:pk>', PostDeleteView.as_view(), name='post_delete'),


]