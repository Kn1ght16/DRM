import pytest
from rest_framework.test import APIClient
from rest_framework import status
from courses.models import Course, Subscription
from users.models import User


@pytest.fixture
def api_client():
    return APIClient()


@pytest.mark.django_db
def test_set_subscription(api_client):
    user = User.objects.create(email='user@example.com', phone='1234567890', city='City1')
    course = Course.objects.create(title='Course 1', preview='course1_preview.jpg', description='Описание курса 1')

    response = api_client.post(f'/api/courses/{course.id}/subscribe/')
    assert response.status_code == status.HTTP_200_OK

    assert Subscription.objects.filter(user=user, course=course).exists()


@pytest.mark.django_db
def test_remove_subscription(api_client):
    user = User.objects.create(email='user@example.com', phone='1234567890', city='City1')
    course = Course.objects.create(title='Course 1', preview='course1_preview.jpg', description='Описание курса 1')
    subscription = Subscription.objects.create(user=user, course=course)

    response = api_client.delete(f'/api/courses/{course.id}/unsubscribe/')
    assert response.status_code == status.HTTP_200_OK

    assert not Subscription.objects.filter(user=user, course=course).exists()


@pytest.mark.django_db
def test_course_subscription_info(api_client):
    user = User.objects.create(email='user@example.com', phone='1234567890', city='City1')
    course = Course.objects.create(title='Course 1', preview='course1_preview.jpg', description='Описание курса 1')
    subscription = Subscription.objects.create(user=user, course=course)

    response = api_client.get(f'/api/courses/{course.id}/')
    assert response.status_code == status.HTTP_200_OK

    assert response.data['subscribed'] == True
