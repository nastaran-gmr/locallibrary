from django.shortcuts import render
from . import models

def index (request):
    num_book=models.Book.objects.all().count()
    num_author=models.Author.objects.all().count()
    num_bookinstance=models.Bookinstance.objects.all().count()
    num_bookinstance_available=models.Bookinstance.objects.filter(status__exact='a').count
    



    context={'num_book':num_book,'num_author':num_author,'num_bookinstance':num_bookinstance,'num_bookinstance_available':num_bookinstance_available,}

    return render(request,'index.html',context)


