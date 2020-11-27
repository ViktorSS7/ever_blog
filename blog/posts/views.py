from django.shortcuts import render

from django.template import loader

from django.http import HttpResponseRedirect, HttpResponse

from django.urls import reverse

from django.views import generic

from .services import posts, comments

from .forms import CommentCreateForm


class IndexView(generic.ListView):
    template_name = 'index.twig'
    context_object_name = 'posts_list'

    def get_queryset(self):
        return posts.get_posts_list()


def post_page(request, post_id):
    post = posts.get_post_info_by_id(post_id)

    comment_form = CommentCreateForm()
    comments_list = comments.get_comments_list_by_post_id(post_id)
    comments_output = loader.get_template('comments.twig').render({
        'comments_list': comments_list,
        'post_id': post_id,
        'comment_form': comment_form
    }, request)

    return render(request, 'post.twig', {
        'post': post,
        'comments_list': comments_output
    })


def comment_create(request, post_id):
    if request.method == 'POST':
        form = CommentCreateForm(request.POST)

        if form.is_valid():
            comments.add_comment_to_post(post_id, form.cleaned_data['your_name'], form.cleaned_data['comment'])

    return HttpResponseRedirect(reverse('post_page', args=[post_id]))
