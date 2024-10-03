from django.shortcuts import render, redirect

# Create your views here.
from django.views.generic import TemplateView 
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Task
class HomeView(TemplateView):
    template_name = 'todo/home.html'

    def get(self, request):
        if request.user.is_authenticated:
            return redirect('todo:board')
        return render(request, self.template_name)
    


class BoardView(LoginRequiredMixin, View):
    template_name = 'todo/board.html'
    
    def get(self, request):
        tasks = Task.objects.filter(assignees=request.user)
        return render(request, self.template_name, {'tasks': tasks})


