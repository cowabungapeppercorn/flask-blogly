from unittest import TestCase
from app import app
from flask import session, flash


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
            response = client.get('/users/12/edit')
            html = response.get_data(as_text=True)
            self.assertEqual(response.status_code, 200)
            self.assertIn('<form action="/users/new" method="POST">', html)
