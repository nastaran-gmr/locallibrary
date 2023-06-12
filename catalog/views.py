from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.contrib.auth import authenticate, login
from django.views import View
from django.views.generic.base import TemplateView
from django.views.generic.list import ListView
from django.views.generic import DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from . import models

# def index (request):
#     num_book=models.Book.objects.all().count()
#     num_author=models.Author.objects.all().count()
#     num_bookinstance=models.Bookinstance.objects.all().count()
#     num_bookinstance_available=models.Bookinstance.objects.filter(status__exact='a').count
    



#     context={'num_book':num_book,'num_author':num_author,'num_bookinstance':num_bookinstance,'num_bookinstance_available':num_bookinstance_available,}

#     return render(request,'index.html',context)



class Indexview(TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["num_book"] = models.Book.objects.count()
        context["num_author"] = models.Author.objects.count()
        context["num_bookinstance"] = models.Bookinstance.objects.count()
        context["num_bookinstance_available"] = models.Bookinstance.objects.filter(status__exact='a').count()

        return context


class Booklistview(ListView):

    model=models.Book

    # template_name='book_list.html'

class bookdetailveiw(DetailView):
     model =models.Book

     def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context =super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context["book_list"] = models.Book.objects.all()
        return context

    

class authorlistview(ListView) :
    model=models.Author   
    

class authordetailview(DetailView):
    model=models.Author
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["author_list"] =models.Author.objects.all()
        return context
        
 
# def my_view(request):
    # username = request.POST["username"]
    # password = request.POST["password"]
    # user = authenticate(request, username=username, password=password)
    # if user is not None:
    #     login(request, user)
    #     # Redirect to a success page.


    #     return HttpResponseRedirect(reverse('catalog:index', args=[username]))
    #     ...
    # else:


    #     return render(
    #         request,'catalog/index.html',{'error_massage':'user dose not exist'})
        
        

class loanedbookinstancelistview(LoginRequiredMixin,ListView):
    model=models.Bookinstance
    template_name='catalog/loanedbookinstance_list.html'
    def get_queryset(self):
        return models.Bookinstance.objects.filter(borrower=self.request.user).filter(status__exact='o').order_by('due_back')
    

