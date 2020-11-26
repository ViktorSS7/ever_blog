from ..models import Post


def get_posts_list():
    return Post.objects.all()


def get_post_info_by_id(post_id):
    return Post.objects.get(id=post_id)
