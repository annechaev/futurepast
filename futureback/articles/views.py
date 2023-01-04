from django.http import HttpResponse
from django.views.generic import ListView
from helper import FileHelper
from articles.models import Articles, Authors, Categories


class ArticlesHome(ListView):
    model = Articles
    template_name = 'articles/index.html'
    context_object_name = 'articles'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Главная страница")
        return dict(list(context.items()) + list(c_def.items()))

    def get_user_context(self, **kwargs):
        context = kwargs
        context['menu'] = Categories.objects.all()

        return context

    def get_queryset(self):
        return Articles.objects.all()


def update_db(request):
    if Articles.objects.all().count() > 0:
        return HttpResponse("База данных уже наполнена")
    content = FileHelper.open_json_file("articles", "articles.json")
    categories = list(set((get_values(content, "category"))))
    authors = list(set((get_values(content, "author"))))
    authors_list = []
    categories_list = []
    for author in authors:
        data = Authors(name=author)
        data.save()
        authors_list.append({
            "id": data.pk,
            "name": author,
            "data": data
        })
    for category in categories:
        data = Categories(title=category)
        data.save()
        categories_list.append({
            "id": data.pk,
            "title": category,
            "data": data
        })
    for article in content:
        cat_data = list(filter(lambda cat: cat['title'] == article['category'], categories_list))[0]
        author_data = list(filter(lambda aut: aut['name'] == article['author'], authors_list))[0]
        article_db = Articles(
            title=article['title'],
            content=article['content'],
            views=article['views'],
            author_id=author_data['data'],
            category_id=cat_data['data'])
        article_db.save()
    return HttpResponse("База наполнилась данными. Проверьте, пожалуйста")


def get_values(a_list, key):
    res = []
    for item in a_list:
        res.append(item[key])

    return res
