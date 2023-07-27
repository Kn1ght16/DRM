from django.db import models
from users.models import User


class Course(models.Model):
    title = models.CharField(max_length=200)
    preview = models.ImageField(upload_to='previews/')
    description = models.TextField()

    def __str__(self):
        return self.title


class Lesson(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    preview = models.ImageField(upload_to='previews/')
    video_link = models.URLField()

    def __str__(self):
        return self.title


class Payment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    payment_date = models.DateField()
    paid_course_or_lesson = models.ForeignKey(
        Course, on_delete=models.CASCADE, null=True, blank=True)
    paid_amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_method_choices = (
        ('cash', 'Наличные'),
        ('bank_transfer', 'Перевод на счет'),
    )
    payment_method = models.CharField(
        max_length=15, choices=payment_method_choices)

    def __str__(self):
        return f"Платеж {self.pk} - {self.user.email}"
