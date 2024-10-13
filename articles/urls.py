from django.urls import path
from .views import (
    ArticleCreateView,
    ArticleDeleteView,
    ArticleDetailView,
    ArticlelistView,
    ArticleUpdateView,
)
urlpatterns = [
    path('', ArticlelistView.as_view(), name='article_list'),
    path('new/', ArticleCreateView.as_view(), name='article_new'),
    path('<int:pk>/edit/', ArticleUpdateView.as_view(), name='article_edit'),
    path('<int:pk>/delete/', ArticleDeleteView.as_view(), name='article_delete'),
    path('<int:pk>/detail/', ArticleDetailView.as_view(), name='article_detail'),
]