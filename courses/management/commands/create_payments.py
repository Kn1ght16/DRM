from django.core.management.base import BaseCommand
from datetime import date
from courses.models import Payment, Course, Lesson
from drm_users.models import User
from courses.serializers import PaymentSerializer


class Command(BaseCommand):
    help = 'Create fixture data for payments model'

    def handle(self, *args, **kwargs):
        # Создаем несколько пользователей и курсов для тестовых данных
        user1 = User.objects.create(email='user1@example.com', phone='1234567890', city='City1', avatar='avatar1.jpg')
        user2 = User.objects.create(email='user2@example.com', phone='9876543210', city='City2', avatar='avatar2.jpg')
        course1 = Course.objects.get(title='Course 1')
        course2 = Course.objects.get(title='Course 2')
        lesson1 = Lesson.objects.create(title='Lesson 1', description='Описание к уроку 1',
                                        preview='lesson1_preview.jpg', video_link='https://example.com/lesson1')
        lesson2 = Lesson.objects.create(title='Lesson 2', description='Описание к уроку 2',
                                        preview='lesson2_preview.jpg', video_link='https://example.com/lesson2')

        # Создаем несколько записей платежей с помощью фикстур
        payments_data = [
            {
                'user': user1,
                'payment_date': date(2023, 7, 1),
                'paid_course_or_lesson': course1,
                'paid_amount': 50.00,
                'payment_method': 'cash',
            },
            {
                'user': user1,
                'payment_date': date(2023, 7, 3),
                'paid_course_or_lesson': course2,
                'paid_amount': 70.00,
                'payment_method': 'bank_transfer',
            },
            {
                'user': user2,
                'payment_date': date(2023, 7, 2),
                'paid_course_or_lesson': course1,  # Используем course1, а не lesson1
                'paid_amount': 20.00,
                'payment_method': 'cash',
            },
        ]

        for payment_data in payments_data:
            Payment.objects.create(**payment_data)

        self.stdout.write(self.style.SUCCESS('Успешно созданные платежные системы'))
        self.stdout.write(self.style.SUCCESS('Успешно созданные платежные системы'))
