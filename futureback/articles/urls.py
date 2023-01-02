from django.urls import path

from articles.views import ArticlesHome, update_db

urlpatterns = [
    path('', ArticlesHome.as_view(), name='home'),
    path('update_db/', update_db)
]
