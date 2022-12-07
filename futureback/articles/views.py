from django.shortcuts import render
from django.views.generic import View


# Create your views here.
class ArticlesHome(View):

    template_name = 'articles/index.html'

    def get(self, request):
        return render(request, self.template_name)
