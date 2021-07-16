from django.urls import path
from .views import post_list, post_details, category_details

urlpatterns = [
    path('blogs/', post_list, name='blog-list'),
    path('post-details/<slug:slug>/', post_details, name='post-details'),
    path('category/<slug:slug>/', category_details, name='category-details')

]
