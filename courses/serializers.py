from rest_framework import serializers
from .models import Course, Lesson, Payment


class CourseSerializer(serializers.ModelSerializer):
    num_lessons = serializers.SerializerMethodField()
    lessons = serializers.StringRelatedField(many=True, read_only=True)  # Поле вывода уроков

    class Meta:
        model = Course
        fields = '__all__'

    def get_num_lessons(self, obj):
        # Получаем количество уроков для данного курса
        return obj.lesson_set.count()


class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = '__all__'


class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = '__all__'
