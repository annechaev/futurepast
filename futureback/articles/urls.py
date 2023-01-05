from django.urls import path

from articles.views import ArticlesHome, update_db, AboutUs, ArticlesCategory, DbUses

urlpatterns = [
    path('', ArticlesHome.as_view(), name='home'),
    path('about/', AboutUs.as_view(), name='about'),
    path('category/<slug:cat_slug>/', ArticlesCategory.as_view(), name='category'),
    path('db/', DbUses.as_view(), name='db')
]
