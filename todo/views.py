from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView

class HomeView(TemplateView):
    template_name = 'todo/home.html'

    def get(self, request):
        return render(request, self.template_name)


