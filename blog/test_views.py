from django.test import TestCase


class TestViews(TestCase):

    def test_get_post_list(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')

    # def test_get_comment
