from http import HTTPStatus

from django.test import Client
from django.test import TestCase
from django.urls import reverse


class StaticURLTests(TestCase):
    def test_about_endpoint_status(self) -> None:
        url = reverse('about:about')

        response = Client().get(url)
        self.assertEqual(
            response.status_code,
            HTTPStatus.OK,
            f'Expected: {HTTPStatus.OK}, '
            f'got: {response.status_code}, testcase: {url}',
        )
