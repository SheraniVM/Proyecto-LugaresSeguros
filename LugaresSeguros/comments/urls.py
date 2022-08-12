from django.urls import path
from .views import CommentView
from .views import CommentSingleView

urlpatterns = [
    path('', CommentView.as_view()),
    path('<int:pk>/', CommentSingleView.as_view())
]