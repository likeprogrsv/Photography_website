from django.test import TestCase
from main.forms import CommentForm

class TestForms(TestCase):

    def test_comment_from_is_valid(self):
        form = CommentForm(data={
            'content': 'testing comment from testing user'
        })

        self.assertTrue(form.is_valid())
    
