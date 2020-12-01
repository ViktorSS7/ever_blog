from ..models import Comment

import datetime


def get_comment_by_id(comment_id):
    return Comment.objects.get(id=comment_id)


def get_comments_list_by_post_id(post_id):
    return Comment.objects.filter(post_id=post_id)


def add_comment_to_post(post_id, user, body):
    comment = Comment(post_id=post_id, user=user, body=body)
    comment.date_added = datetime.datetime.now()
    comment.save()

    return comment.id


def delete_comment(comment_id):
    comment = Comment.objects.get(id=comment_id)
    comment.delete()


def get_post_by_comment_id(comment_id):
    return Comment.objects.get(id=comment_id).post
