from django.urls import path, include
from .views import article_list, article_detail, ArticleAPIView, ArticleDetails, GenericAPIView, ArticleViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('article-viewset', ArticleViewSet, basename='article-viewset')

urlpatterns = [
    path('api/article', article_list),
    path('api/article/<int:pk>', article_detail),
    path('api/article-view', ArticleAPIView.as_view()),
    path('api/article-detail/<int:id>', ArticleDetails.as_view()),
    path('api/generic-view/<int:id>', GenericAPIView.as_view()),
    path('viewset/', include(router.urls)),
    path('viewset/<int:pk>', include(router.urls))
]
