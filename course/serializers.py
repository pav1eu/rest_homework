from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from course.models import Course, Lesson


class LessonSerializer(ModelSerializer):
    class Meta:
        model = Lesson
        fields = "__all__"


class CourseSerializer(ModelSerializer):
    lesson_count = serializers.SerializerMethodField()
    lessons = LessonSerializer(many=True, source="lesson_set")

    class Meta:
        model = Course
        fields = "__all__"

    def get_lesson_count(self, obj):
        return obj.lesson_set.count()


class LessonDetailSerializer(ModelSerializer):
    class Meta:
        model = Course
        fields = "__all__"
