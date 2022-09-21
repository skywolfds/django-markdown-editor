# app/testPosts.py

from django.test import TestCase
from app.models import Post


class PostTestCase(TestCase):
    def testPost(self):
        post = Post(title="My Title", description="Meaningful Description", wiki="Post Body")
        self.assertEqual(post.title, "My Title")
        self.assertEqual(post.description, "Meaningful Description")
        self.assertAlmostEqual(post.wiki, "Post Body")
