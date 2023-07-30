import pytest
from rest_framework.test import APIClient
from rest_framework import status
from courses.models import Lesson


@pytest.fixture
def api_client():
    return APIClient()


@pytest.mark.django_db
def test_create_lesson(api_client):
    lesson_data = {
        'title': 'Lesson 1',
        'description': 'Описание урока 1',
        'preview': 'lesson1_preview.jpg',
        'video_link': 'https://youtube.com/lesson1'
    }

    response = api_client.post('/api/lessons/', lesson_data)
    assert response.status_code == status.HTTP_201_CREATED

    lesson = Lesson.objects.get(pk=response.data['id'])
    assert lesson.title == lesson_data['title']


@pytest.mark.django_db
def test_get_lesson(api_client):
    lesson_data = {
        'title': 'Lesson 1',
        'description': 'Описание урока 1',
        'preview': 'lesson1_preview.jpg',
        'video_link': 'https://youtube.com/lesson1'
    }
    lesson = Lesson.objects.create(**lesson_data)

    response = api_client.get(f'/api/lessons/{lesson.id}/')
    assert response.status_code == status.HTTP_200_OK
    assert response.data['title'] == lesson_data['title']


@pytest.mark.django_db
def test_update_lesson(api_client):
    lesson_data = {
        'title': 'Lesson 1',
        'description': 'Описание урока 1',
        'preview': 'lesson1_preview.jpg',
        'video_link': 'https://youtube.com/lesson1'
    }
    lesson = Lesson.objects.create(**lesson_data)

    updated_data = {
        'title': 'Updated Lesson 1',
        'description': 'Обновленное описание урока 1',
        'preview': 'updated_preview.jpg',
        'video_link': 'https://youtube.com/updated_lesson1'
    }

    response = api_client.put(f'/api/lessons/{lesson.id}/', updated_data)
    assert response.status_code == status.HTTP_200_OK

    lesson.refresh_from_db()
    assert lesson.title == updated_data['title']


@pytest.mark.django_db
def test_delete_lesson(api_client):
    lesson_data = {
        'title': 'Lesson 1',
        'description': 'Описание урока 1',
        'preview': 'lesson1_preview.jpg',
        'video_link': 'https://youtube.com/lesson1'
    }
    lesson = Lesson.objects.create(**lesson_data)

    response = api_client.delete(f'/api/lessons/{lesson.id}/')
    assert response.status_code == status.HTTP_204_NO_CONTENT

    with pytest.raises(Lesson.DoesNotExist):
        Lesson.objects.get(pk=lesson.id)
