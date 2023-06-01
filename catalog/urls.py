from django.urls import path ,re_path
from . import views

app_name='catalog'

urlpatterns = [

    path(r'',views.Indexview.as_view(),name='index'),
    path(r'books/',views.Booklistview.as_view(),name='books'),
    path(r'<pk>/',views.bookdetailveiw.as_view(),name='bookdetail')
    
]
