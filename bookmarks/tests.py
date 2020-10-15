import json
from django.urls import reverse
from django.contrib.auth.models import User

from rest_framework.test import APITestCase, APIClient
from rest_framework.views import status
from .models import Bookmark
from .serializers import BookmarkSerializer

class BaseViewTest(APITestCase):
    client = APIClient()

    @staticmethod
    def create_bookmark(title="", url=""):
        if title != "" and url != "":
            Bookmark.objects.create(title=title, url=url)
    
    def login_a_user(self, username="", password=""):
        url = reverse(
            "auth-login",
            kwargs={
                "version": "v1"
            }
        )
        return self.client.post(
            url,
            data=json.dumps({
                "username": username,
                "password": password
            }),
            content_type="application/json"
        )

    def login_client(self, username="", password=""):
        response = self.client.post(
            reverse('create-token'),
            data=json.dumps(
                {
                    'username': username,
                    'password': password
                }
            ),
            content_type='application/json'
        )
        self.token = response.data['token']
        self.client.credentials(
            HTTP_AUTHORIZATION='Bearer ' + self.token
        )
        self.client.login(username=username, password=password)
        return self.token
    
    def setUp(self):
        self.user = User.objects.create_superuser(
            username="test_user",
            email="test@mail.com",
            password="testing",
            first_name="test",
            last_name="user",
        )
        self.create_bookmark("google", "www.google.com")
        self.create_bookmark("github", "www.github.com")
        self.create_bookmark("centrifugal govenor", "https://en.wikipedia.org/wiki/Centrifugal_governor")


class GetAllBookmarksTest(BaseViewTest):

    def test_get_all_bookmarks(self):
        self.login_client('test_user', 'testing')
        response = self.client.get(
            reverse("bookmarks-all", kwargs={"version": "v1"})
        )
        expected = Bookmark.objects.all()
        serialized = BookmarkSerializer(expected, many=True)
        self.assertEqual(response.data, serialized.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

class AuthRegisterUserTest(BaseViewTest):
    def test_register_a_user_with_valid_data(self):
        url = reverse(
            "auth-register",
            kwargs={
                "version": "v1"
            }
        )
        response = self.client.post(
            url,
            data=json.dumps(
                {
                    "username": "new_user",
                    "password": "new_pass",
                    "email": "new_user@mail.com"
                }
            ),
            content_type="application/json"
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_register_a_user_with_invalid_data(self):
        url = reverse(
            "auth-register",
            kwargs={
                "version": "v1"
            }
        )
        response = self.client.post(
            url,
            data=json.dumps(
                {
                    "username": "",
                    "password": "",
                    "email": ""
                }
            ),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

class AuthLoginUserTest(BaseViewTest):

    def test_login_user_with_valid_credentials(self):
        response = self.login_a_user("test_user", "testing")
        self.assertIn("token", response.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        response = self.login_a_user("anonymous", "pass")
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

