from http import HTTPStatus

from django.test import Client
from django.test import TestCase
from django.urls import reverse_lazy


class StaticURLTests(TestCase):
    def test_events_list_endpoint_status(self) -> None:
        url = reverse_lazy('events:events_list')

        response = Client().get(url)
        self.assertEqual(
            response.status_code,
            HTTPStatus.OK,
            f'Expected: {HTTPStatus.OK}, '
            f'got: {response.status_code}, testcase: {url}',
        )
