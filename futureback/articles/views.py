from django.shortcuts import render
from django.views.generic import TemplateView


# Create your views here.
class ArticlesHome(TemplateView):

    template_name = 'articles/index.html'
