from django.test import TestCase
from model_bakery import baker
from rest_framework.test import APIClient
from django.contrib.auth.models import User
from training.models import Activity, UserActivity


class ActivityAPITestCase(TestCase):
    client = APIClient()
    url = '/activity/'

    def setUp(self):
        email = 'abc@examle.com'
        self.user = baker.make(User, email=email)

    def test_activity_list_api_status(self):
        resp = self.client.get(self.url)
        self.assertEqual(resp.status_code, 200)

    def test_activity_list_api_content(self):
        baker.make(Activity, _quantity=3)
        resp = self.client.get(self.url)
        self.assertEqual(resp.status_code, 200)
        content = resp.json()
        self.assertEqual(content['count'], 3)


class UserActivityAPITestCase(TestCase):
    client = APIClient()
    url = '/user-activity/'

    def setUp(self):
        email = 'abc@examle.com'
        self.user = baker.make(User, email=email)

    def test_user_activity_list_api_status(self):
        resp = self.client.get(self.url)
        self.assertEqual(resp.status_code, 200)

    def test_activity_list_api_content(self):
        activity1 = baker.make(Activity)
        activity2 = baker.make(Activity)
        baker.make(UserActivity, user=self.user, activity=activity1, _quantity=2)
        baker.make(UserActivity, user=self.user, activity=activity2, _quantity=3)
        resp = self.client.get(self.url)
        self.assertEqual(resp.status_code, 200)
        content = resp.json()
        self.assertEqual(content['count'], 5)