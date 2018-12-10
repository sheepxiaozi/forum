from django.urls import resolve
from django.test import TestCase
from django.urls import reverse
from .views import signup


class SignUpTests(TestCase):
    """ 测试状态码（200=success） """
    def test_signup_status_code(self):
        url = reverse('signup')
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)

    def test_signup_url_resolves_signup_view(self):
        """ URL /signup/ 是否返回了正确的视图函数 """
        view = resolve('/signup/')
        self.assertEquals(view.func, signup)


