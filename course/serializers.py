from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from course.models import Course, Lesson
from course.validators import YoutubeOnlyValidator
from users.models import Subscription


class LessonSerializer(ModelSerializer):
    class Meta:
        model = Lesson
        exclude = ("owner",)
        validators = [
            YoutubeOnlyValidator(field='video_url')
        ]


class CourseSerializer(ModelSerializer):
    lesson_count = serializers.SerializerMethodField()
    lessons = LessonSerializer(many=True, source="lesson_set")
    is_subscribed = serializers.SerializerMethodField()

    class Meta:
        model = Course
        fields = "__all__"

    def get_lesson_count(self, obj):
        return obj.lesson_set.count()

    def get_is_subscribed(self, obj):
        user = self.context.get('request').user
        if user.is_anonymous:
            return False
        return Subscription.objects.filter(user=user, course=obj).exists()


class LessonDetailSerializer(ModelSerializer):
    class Meta:
        model = Lesson
        fields = "__all__"
