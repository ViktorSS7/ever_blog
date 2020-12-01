from ..models import Comment

import datetime


def get_comments_list_by_post_id(post_id):
    return Comment.objects.filter(post_id=post_id)


def add_comment_to_post(post_id, user, body):
    comment = Comment(post_id=post_id, user=user, body=body)
    comment.date_added = datetime.datetime.now()
    comment.save()

    return comment.id
