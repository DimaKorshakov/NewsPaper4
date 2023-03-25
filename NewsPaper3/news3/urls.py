from django.urls import path
from .views import NewsList, Search, NewsDetailView, NewsCreateView, NewsUpdateView  # импортируем наше представление

urlpatterns = [
    path('', NewsList.as_view()),
    path('search', Search.as_view()),
    path('<int:pk>/', NewsDetailView.as_view(), name='news_detail'), # Ссылка на детали товара
    path('create/', NewsCreateView.as_view(), name='news_create'),
    # path('update/', NewsCreateView.as_view(), name='news_update'),
    path('update', NewsUpdateView.as_view(), name='news_update')
]
