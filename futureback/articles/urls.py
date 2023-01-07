from django.urls import path

from articles.views import ArticlesHome, update_db, AboutUs, ArticlesCategory, DbUses, ShowArticle

urlpatterns = [
    path('', ArticlesHome.as_view(), name='home'),
    path('about/', AboutUs.as_view(), name='about'),
    path('category/<slug:cat_slug>/', ArticlesCategory.as_view(), name='category'),
    path('article/<slug:article_slug>/', ShowArticle.as_view(), name='article'),
    path('db/', DbUses.as_view(), name='db')
]
