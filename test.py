from unittest import TestCase
from app import app


class FlaskTests(TestCase):
    def setUp(self):
        self.client = app.test_client()
        app.config['TESTING'] = True
        app.config['DEBUG_TB_HOSTS'] = ['dont-show-debug-toolbar']

    def test_homepage(self):
        with self.client as client:
            response = client.get('/')
            html = response.get_data(as_text=True)
            self.assertEqual(response.status_code, 302)
            self.assertIn('<h1>Redirecting...</h1>', html)

    def test_users_page(self):
        with self.client as client:
            response = client.get('/users')
            html = response.get_data(as_text=True)
            self.assertEqual(response.status_code, 200)
            self.assertIn('<h1>Users</h1>', html)

    def test_users_new(self):
        with self.client as client:
            response = client.get('/users/new')
            html = response.get_data(as_text=True)
            self.assertEqual(response.status_code, 200)
            self.assertIn('<form action="/users/new" method="POST">', html)

    def test_user_edit(self):
        with self.client as client:
            response = client.get('/users/27/edit')
            html = response.get_data(as_text=True)
            self.assertEqual(response.status_code, 200)
            self.assertIn('<form action="/users/new" method="POST">', html)

    def test_new_post(self):
        with self.client as client:
            response = client.get('/users/20/posts/new')
            html = response.get_data(as_text=True)
            self.assertEqual(response.status_code, 200)
            self.assertIn('<form action="/users/20/posts/new" method="POST">', html)

    def test_users_create_new(self):
        with self.client as client:
            data = {'first_name': 'first', 'last_name': 'last', 'image_url': 'image_url'}
            response = client.post('/users/new', data=data)
            self.assertEqual(response.status_code, 302)

    def test_posts_create_new(self):
        with self.client as client:
            data = {'title': 'title', 'content': ''}
            response = client.post('/users/27/posts/new', data=data)
            self.assertEqual(response.status_code, 302)
