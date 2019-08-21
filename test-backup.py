from unittest import TestCase
from app import app
from flask import session


class FlaskTests(TestCase):
    
​   def setUp(self):
    self.client = app.test_client()
    app.config['TESTING'] = True
    app.config['DEBUG_TB_HOSTS'] = ['dont-show-debug-toolbar']
​
    def test_homepage(self):
​
        with self.client as client:
            response = client.get('/')
            html = response.get_data(as_text=True)
            self.assertEqual(response.status_code, 302)
            
            
# self.assertIn('<h1></h1>', html)
# self.assertIn('<form action="/conversion/" method="POST">', html)
# self.assertIn('<input type="number" step=".01"', html)
​
#     def test_redirect_and_flash(self):
#         usd = currencies.Currency('USD')
# ​
#         self.assertEqual(currencies.should_redirect_and_flash(usd, usd, 5),
#                          False)
# ​
#     def test_convert_currencies(self):
#         usd = currencies.Currency('USD')
# ​
#         self.assertEqual(currencies.convert_currencies(usd, usd, 5), 5)