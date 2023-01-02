from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import View
from helper import FileHelper


# Create your views here.
class ArticlesHome(View):

    template_name = 'articles/index.html'

    def get(self, request):
        return render(request, self.template_name)


def update_db(request):
    content = FileHelper.open_json_file("articles", "articles.json")
    categories = list(set((get_values(content, "category"))))
    authors = list(set((get_values(content, "author"))))
    print(categories)
    print(authors)

    return HttpResponse("Обработаны нововведения")


def get_values(a_list, key):
    res = []
    for item in a_list:
        res.append(item[key])

    return res
