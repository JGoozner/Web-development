from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Articles
from django.urls import reverse_lazy

# Create your views here.
class ArticleListView(ListView):
    model = Articles
    template_name= 'home.html'


class ArticleDetailView(DetailView):
    model = Articles
    template_name = 'detail.html'
    context_object_name= 'batman'

class ArticleCreateView(CreateView):
    model = Articles
    template_name = 'article_new.html'
    fields = '__all__' #gives all fields from CreateView

class ArticleUpdateView(UpdateView):
    model = Articles
    template_name = 'article_edit.html'
    fields = ['title', 'text']

class ArticleDeleteView(DeleteView):
        model = Articles
        template_name = 'article_delete.html'
        context_object_name= 'batman'
        success_url = reverse_lazy('home')
