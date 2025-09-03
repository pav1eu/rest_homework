from django.test import TestCase
from django.db import IntegrityError
from django.contrib.auth.models import Group
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from course.models import Lesson, Course
from users.models import User, Subscription


class LessonCRUDTest(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(email="test@test.com", password="pass123")
        moderators_group, _ = Group.objects.get_or_create(name="Модераторы")
        self.user.groups.add(moderators_group)
        self.client.force_authenticate(self.user)
        self.course = Course.objects.create(title="Test course", owner=self.user)
        self.lesson = Lesson.objects.create(title="Lesson 1", course=self.course, owner=self.user)

    def test_create_lesson(self):
        url = reverse("course:lesson-create")
        data = {"title": "New lesson", "course": self.course.id, "video_url": "http://video.youtube.com"}
        response = self.client.post(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data["title"], data["title"])
        self.assertEqual(response.data["course"], self.course.id)

    def test_update_lesson(self):
        url = reverse("course:lesson-update", args=[self.lesson.id])
        data = {"title": "Updated lesson"}
        response = self.client.patch(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["title"], data["title"])

    def test_delete_lesson(self):
        url = reverse("course:lesson-delete", args=[self.lesson.id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_list_lessons(self):
        url = reverse("course:lesson-list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_retrieve_lesson(self):
        url = reverse("course:lesson-retrieve", args=[self.lesson.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["id"], self.lesson.id)
        self.assertEqual(response.data["title"], self.lesson.title)



class SubscriptionModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(email="sub@test.com", password="12345")
        self.course = Course.objects.create(title="Python course", owner=self.user)

    def test_create_subscription(self):
        sub = Subscription.objects.create(user=self.user, course=self.course)
        self.assertEqual(sub.user, self.user)
        self.assertEqual(sub.course, self.course)
        self.assertIsNotNone(sub.created_at)

    def test_delete_subscription(self):
        sub = Subscription.objects.create(user=self.user, course=self.course)
        self.assertTrue(Subscription.objects.filter(id=sub.id).exists())
        sub.delete()
        self.assertFalse(Subscription.objects.filter(id=sub.id).exists())
