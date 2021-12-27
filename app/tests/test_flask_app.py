import unittest
import pytest

from app.flask_app import app


class TestMain(unittest.TestCase):

    def params(self):
        pytest.client = app.test_client()

    def test_main_page(self):
        self.params()
        response = pytest.client.get("/")

        self.assertEqual(response.status_code, 200)


