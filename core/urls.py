"""core URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView

from cbv.views import MyView, View1, View2, PublisherList, PublisherDetail, BookList, AcmeBookList, PublisherBookList, \
    AuthorDetailView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('mine/', MyView.as_view(), name='my-view'),
    path('about/', TemplateView.as_view(template_name='about.html')),

    # passando os parâmetros para as_view() terá prioridade sobre a view em views.py
    path('view1/', View1.as_view(mensagem="Passando a mensagem em urls.py"), name='view1'),
    path('view2/', View2.as_view(), name='view2'),

    path('publishers/', PublisherList.as_view()),
    path('publishers/detail/<int:pk>', PublisherDetail.as_view()),

    path('book/list', BookList.as_view()),

    path('book/filter/acme', AcmeBookList.as_view()),

    path('book/<publisher>', PublisherBookList.as_view()),

    path('authors/<int:pk>', AuthorDetailView.as_view()),
]
