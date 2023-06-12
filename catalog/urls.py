from django.urls import path ,re_path
from . import views

app_name='catalog'

urlpatterns = [

    path(r'',views.Indexview.as_view(),name='index'),
    path(r'books/',views.Booklistview.as_view(),name='books'),
    path(r'books/<pk>/',views.bookdetailveiw.as_view(),name='bookdetail'),
    path(r'authors/',views.authorlistview.as_view(),name='authors'),
    path(r'authors/<pk>/',views.authordetailview.as_view(),name='authorsdetail'),
    path(r'mybooks/',views.loanedbookinstancelistview.as_view(),name='mybooks'),

    
    
]
