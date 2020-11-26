from django.shortcuts import render

from .services import posts


def index(request):
    posts_list = posts.get_posts_list()

    return render(request, 'index.twig', {
        'posts_list': posts_list
    })


def post_page(request, post_id):
    post = posts.get_post_info_by_id(post_id)

    return render(request, 'post.twig', {
        'post': post
    })