from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from django.views import View
from django.views.generic import ListView, DetailView
from django.views.generic.base import TemplateView
from cbv.models import Publisher, Book, Author


class MyView(View):
    def get(self, request, *args, **kwargs):
        return HttpResponse('Hello World')


class View1(View):
    """ Classe mãe com uma mensagem """
    mensagem = 'Essa é a View 1'

    def get(self, request):
        return HttpResponse(self.mensagem)


class View2(View1):
    """ Classe filha que substitui a mensagem para essa view 2 """
    mensagem = 'Essa é a View 2'


class PublisherList(ListView):
    model = Publisher


# class PublisherDetail(DetailView):
#     model = Publisher
#
#     def get_context_data(self, **kwargs):
#         """ Chame a implementação de base primeiro para obter um contexto """
#         context = super().get_context_data(**kwargs)
#         """ Adiciona um QuerySet para todos os livros """
#         context['book_list'] = Book.objects.all()
#         return context


class PublisherDetail(DetailView):
    context_object_name = 'publisher'
    queryset = Publisher.objects.all()


class BookList(ListView):
    queryset = Book.objects.order_by('-publication_date')
    context_object_name = 'book_list'


class AcmeBookList(ListView):
    context_object_name = 'book_list'
    queryset = Book.objects.filter(publisher__name='ACME Publishing')
    # queryset = Book.objects.all()
    template_name = 'cbv/acme_list.html'


class PublisherBookList(ListView):
    template_name = 'cbv/books_by_publisher.html'
    context_object_name = 'publisher'

    def get_queryset(self):
        self.publisher = get_object_or_404(Publisher, name=self.kwargs['publisher'])
        return Book.objects.filter(publisher=self.publisher)


class AuthorDetailView(DetailView):
    queryset = Author.objects.all()

    def get_object(self, queryset=None):
        obj = super().get_object()
        # Salva a data do último acesso
        obj.last_accessed = timezone.now()
        obj.save()
        return obj



# class HomePageView(TemplateView):
#     template_name = 'home.html'
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['latest_articles'] = Article