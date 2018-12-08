from django.urls import resolve
from django.test import TestCase
from django.urls import reverse
from boards.models import Board
from .views import index, board_topics


class IndexTests(TestCase):
    def setUp(self):
        self.board = Board.objects.create(name='Django', description='Django board.')
        url = reverse('index')
        self.response = self.client.get(url)

    def test_index_view_status_code(self):
        self.assertEquals(self.response.status_code, 200)

    def test_index_url_resolves_index_view(self):
        view = resolve('/index/')
        self.assertEquals(view.func, index)

    def test_index_view_contains_link_to_topics_page(self):
        """测试 response 主体是否包含文本 href="/boards/1/"""
        board_topics_url = reverse('board_topics', kwargs={'pk': self.board.pk})
        self.assertContains(self.response, 'href="{0}"'.format(board_topics_url))


class BoardTopicsTests(TestCase):
    def setUp(self):
        Board.objects.create(name='Django', description='Django board.')

    def test_board_topics_view_success_status_code(self):
        """测试 Django 是否对于现有的 Board 返回 status code(状态码) 200(成功)"""
        url = reverse('board_topics', kwargs={'pk': 1})
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)

    def test_board_topics_view_not_found_status_code(self):
        """测试 Django 是否对于不存在于数据库的 Board 返回 status code 404(页面未找到)"""
        url = reverse('board_topics', kwargs={'pk': 99})
        response = self.client.get(url)
        self.assertEquals(response.status_code, 404)

    def test_board_topics_url_resolves_board_topics_view(self):
        """测试 Django 是否使用了正确的视图函数去渲染 topics"""
        view = resolve('/boards/1/')
        self.assertEquals(view.func, board_topics)

    def test_board_topics_view_contains_link_back_to_homepage(self):
        board_topics_url = reverse('board_topics', kwargs={'pk': 1})
        response = self.client.get(board_topics_url)
        homepage_url = reverse('index')
        self.assertContains(response, 'href="{0}"'.format(homepage_url))



