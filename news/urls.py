from django.urls import path
from .views import news, news_detail, new_news, news_edit, news_delete

urlpatterns = [
    path('', news, name='news'),
    path('<int:pk>/', news_detail, name='news_detail'),
    path('new/', new_news, name='new_news'),
    path('<int:pk>/edit/', news_edit, name='news_edit'),
    path('<int:pk>/delete/', news_delete, name='news_delete'),
 
]