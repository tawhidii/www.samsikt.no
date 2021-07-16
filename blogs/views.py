from django.shortcuts import render

from django.shortcuts import render, get_object_or_404

from .models import Category, Post


def post_list(request):
    posts = Post.objects.filter(is_published=True).order_by('published_at')

    context = {
        'posts': posts,
    }

    return render(request, 'blogs/blog-list.html', context)


def post_details(request, slug):
    post = get_object_or_404(Post, slug=slug)
    categories = Category.objects.all()
    counter_categories = categories.values('title', 'slug')

    context = {
        'post': post,
        'categories': counter_categories,
    }

    return render(request, 'blogs/blog-details.html', context)


def category_details(request, slug):
    category = get_object_or_404(Category, slug=slug)
    category_post = Post.objects.filter(category=category).filter(is_published=True).all()
    context = {
        'post_count': category_post.count(),
        'category_post': category_post
    }

    return render(request, 'blogs/category-details.html', context)
