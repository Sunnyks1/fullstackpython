from django.urls import path
from .import views

urlpatterns=[
    path('',views.book_list,name='book_list'),
    path('book/<int:pk>/',views.book_details,name='book_detail'),
    path('book/add/',views.BookCreateViews.as_view(),name='book_add'),
    path('book/<int:pk>/review',views.add_review,name='add_review'),
]