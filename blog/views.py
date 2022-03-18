import random

from django.contrib.admin.views.decorators import staff_member_required
from django.http import Http404
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView

from .models import Article
from .forms import ArticleForm


class ArticleListView(ListView):
    model = Article
    template_name = 'blog/list.html'
    paginate_by = 20
    ordering = ['-id']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        subject = Article.objects.order_by(
            'subject').values_list('subject', flat=True).distinct()

        context['subject'] = subject
        return context

    def get_queryset(self):
        articles = Article.objects.all()

        if self.kwargs.get('keywors'):
            articles = articles.filter(keywors=self.kwargs['keywors'])
            if len(articles) == 0:
                raise Http404()

        return articles


class ArticleDetailView(DetailView):
    model = Article
    template_name = 'blog/detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        articles = Article.objects.filter(
            author=self.object.author
        ).exclude(
            title=self.object.title
        )
        articles = list(articles)
        random.shuffle(articles)
        context['articles'] = articles

        return context


@method_decorator(staff_member_required, name='dispatch')
class ArticleCreate(CreateView):
    model = Article
    form_class = ArticleForm
    success_url = reverse_lazy('blog:article')


@method_decorator(staff_member_required, name='dispatch')
class ArticleUpdate(UpdateView):
    model = Article
    form_class = ArticleForm
    template_name_suffix = '_update_form'

    def get_success_url(self):
        return reverse_lazy('blog:update', args=[self.object.slug]) + '?ok'


@method_decorator(staff_member_required, name='dispatch')
class ArticleDelete(DeleteView):
    model = Article
    success_url = reverse_lazy('blog:article')
