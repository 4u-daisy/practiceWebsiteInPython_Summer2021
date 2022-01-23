from typing import Dict, Union, Any
from django.shortcuts import render, redirect
from .models import article
from .forms import articleForm
from django.views.generic import DetailView, UpdateView, DeleteView

def news_home(request):
    news = article.objects.order_by('date')
    return render(request, 'news/news_home.html', {'news': news})

class newsDetailView(DetailView):
    model = article
    template_name = 'news/detail_view.html'
    context_object_name = 'article'

class newsUpdateView(UpdateView):
    model = article
    template_name = 'news/create.html'
    form_class = articleForm

class newsDeleteView(DeleteView):
    model = article
    success_url = '/news/'
    template_name ='news/delete.html'

def create(request):
    error = ''
    if request.method == 'POST':
        form = articleForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            error = "Форма была неверной"
    form = articleForm()
    data = {
        'form': form,
        'error': error
    }
    return render(request, 'news/create.html', data)