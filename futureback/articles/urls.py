from django.urls import path

from articles.views import ArticlesHome

urlpatterns = [
    path('', ArticlesHome.as_view(), name='home')
]
