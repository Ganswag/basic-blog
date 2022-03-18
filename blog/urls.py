from django.urls import path
from .views import (
    ArticleListView, ArticleDetailView, ArticleCreate,
    ArticleUpdate, ArticleDelete)


urlpatterns = [
    path('', ArticleListView.as_view(), name='articles'),
    path('crear-nueva-entrada/', ArticleCreate.as_view(), name='create'),
    path('<slug:slug>/', ArticleDetailView.as_view(), name='article'),
    path('<slug:slug>/actualizar/', ArticleUpdate.as_view(), name='update'),
    path('<slug:slug>/borrar/', ArticleDelete.as_view(), name='delete'),
]
