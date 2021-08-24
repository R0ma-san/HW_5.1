from django.urls import path
from .views import questions, questions_detail, new_questions, questions_delete

urlpatterns = [
    path('', questions, name='questions'),
    path('<int:pk>/', questions_detail, name='questions_detail'),
    path('new/', new_questions, name='new_questions'),
    path('<int:pk>/delete/', questions_delete, name='questions_delete'),
 
]