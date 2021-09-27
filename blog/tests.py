from django.test import TestCase
from forms import CommentForm

# Create your tests here.

# class TestCommentForm(TestCase):
#     def test_comment_body_is_required(self):
#         form = CommentForm({'body': ''})
#         self.assertFalse(form.is_valid())
#         self.asssertIn('name', form.errors.keys())
#         self.assertEqual(form.errors['body'][0], 'This field is required')
