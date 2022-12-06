from django.shortcuts import render
from django.views.generic import ListView


# Create your views here.
class ArticlesHome(ListView):

    template_name = 'articles/index.html'

    def get_queryset(self):
        return [(1,), (2,)]
