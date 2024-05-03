from django.urls import path
from news.api import views as api_views

urlpatterns = [
    path('journalists/', api_views.JournalistListCreateAPIView.as_view(), name="jounalist-list"),
    path('articles/', api_views.ArticleListCreateAPIView.as_view(), name="article-list"),
    path('articles/<int:pk>', api_views.ArticleDetailAPIView.as_view(), name="article-detail"),
]

# FUNCTION BASED VIEWS
# urlpatterns = [
#     path('articles/', api_views.article_list_create_api_view, name="article-list"),
#     path('articles/<int:pk>', api_views.article_detail_api_view, name="article-detail"),
# ]