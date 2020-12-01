from django.shortcuts import render

from django.template import loader

from django.http import HttpResponseRedirect, HttpResponse

from django.urls import reverse

from django.views import generic

from .services import posts, comments

from .forms import CommentCreateForm


class IndexView(generic.ListView):
    template_name = 'posts/post_list.twig'
    context_object_name = 'posts_list'

    def get_queryset(self):
        return posts.get_posts_list()


def post_page(request, post_id):
    post = posts.get_post_info_by_id(post_id)

    comment_form = CommentCreateForm()
    comments_list = comments.get_comments_list_by_post_id(post_id)
    comments_output = loader.get_template('comments/comments.twig').render({
        'comments_list': comments_list,
        'post_id': post_id,
        'comment_form': comment_form
    }, request)

    return render(request, 'posts/post.twig', {
        'post': post,
        'comments_list': comments_output
    })


def comment_create(request, post_id):
    if request.method == 'POST':
        form = CommentCreateForm(request.POST)

        if form.is_valid():
            comments.add_comment_to_post(post_id, request.user, form.cleaned_data['comment'])

    return HttpResponseRedirect(reverse('post_page', args=[post_id]))


def comment_delete(request, comment_id):
    comment = comments.get_comment_by_id(comment_id)

    if comment.user.id == request.user.id:
        comments.delete_comment(comment_id)

    return HttpResponseRedirect(reverse('post_page', args=[
        comment.post_id
    ]))
