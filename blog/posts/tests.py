import datetime

from django.test import TestCase

from django.utils import timezone

from .models import Post


class PostModelTest(TestCase):

    def test_was_published_recently_with_future_post(self):
        """
        was_published_recently() returns False for post whose date_added
        is in the future.
        """
        time = timezone.now() + datetime.timedelta(days=30)
        future_post = Post(date_added=time)
        self.assertIs(future_post.was_published_recently(), False)
