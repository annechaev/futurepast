from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from django.views import View
from django.views.generic import ListView

from articles.utils import DataMixin, update_db
from articles.models import Articles, Authors, Categories


class ArticlesHome(DataMixin, ListView):
    model = Articles
    template_name = 'articles/index.html'
    context_object_name = 'articles'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Главная страница", db_title="Наполнить БД")
        return dict(list(context.items()) + list(c_def.items()))

    def get_queryset(self):
        return Articles.objects.all()


class ArticlesCategory(DataMixin, ListView):
    model = Articles
    template_name = 'articles/index.html'
    context_object_name = 'articles'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        selected_category = str(context['articles'][0].category_id)
        c_def = self.get_user_context(title="Категория - " + selected_category,
                                      db_title="Наполнить БД",
                                      selected_category=selected_category)
        return dict(list(context.items()) + list(c_def.items()))

    def get_queryset(self):
        return Articles.objects.filter(category_id__slug=self.kwargs['cat_slug']).select_related('category_id')


class AboutUs(DataMixin, View):
    template_name = 'articles/about.html'

    def get(self, request):
        c_def = self.get_user_context(title="О нас")
        return render(request, self.template_name, context=dict(list(c_def.items())))


class DbUses(View):

    def get(self, request):
        update_db()
        return redirect('home')
