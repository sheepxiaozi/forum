from django.test import TestCase
from django.urls import resolve
from ..views import BoardListView


class HomeTests(TestCase):
    def test_home_url_resolves_home_view(self):
        view = resolve('/index/')
        self.assertEquals(view.func.view_class, BoardListView)


