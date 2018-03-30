from django.views.generic import ListView, DetailView

from .models import Articles
# Create your views here.
class ArticleListView(ListView):
    model = Articles
    template_name= 'home.html'


class ArticleDetailView(DetailView):
    model = Articles
    template_name = 'detail.html'
    context_object_name= 'batman'
