from unittest import TestCase
from app import app


class Test(TestCase):
    def test_notice(self):
        with app.app_context() as ctx:
            res = app.test_client().get('/notice')
            print(res)

    def test_post_notice(self):
        with app.app_context() as ctx:
            res = app.test_client().post('/echo_call')
            print(res)