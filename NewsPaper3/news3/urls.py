from django.urls import path
from .views import NewsList, Search, NewsDetailView, NewsCreateView, NewsUpdateView, \
    NewsDeleteView  # импортируем наше представление

urlpatterns = [
    path('', NewsList.as_view()),
    path('search', Search.as_view()),
    path('<int:pk>/', NewsDetailView.as_view(), name='news_detail'),  # Ссылка на детали товара
    path('create/', NewsCreateView.as_view(), name='news_create'),
    # path('update/', NewsCreateView.as_view(), name='news_update'),
    path('update/<int:pk>', NewsUpdateView.as_view(), name='news_update'),
    path('delete/<int:pk>', NewsDeleteView.as_view(), name='news_delete')
]
