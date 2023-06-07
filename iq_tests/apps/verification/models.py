from shortuuid.django_fields import ShortUUIDField

from django.conf import settings
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.utils import timezone

AVAILABLE_CHOICES = tuple(zip(
    settings.AVAILABLE_CHOICES,
    settings.AVAILABLE_CHOICES
))


class ModelWithDurationField(models.Model):
    """Model with Duration field."""
    duration = models.DurationField(null=True, blank=True)

    class Meta:
        abstract = True


class IQTest(ModelWithDurationField):
    """IQ test model."""
    result = models.SmallIntegerField(
        null=True,
        blank=True,
        validators=[
            MinValueValidator(settings.MIN_IQ_RESULT),
            MaxValueValidator(settings.MAX_IQ_RESULT)
        ]
    )


class Result(models.Model):
    """Result of eq tests."""
    result = models.CharField(max_length=1, choices=AVAILABLE_CHOICES)


class EQTestResult(models.Model):
    """Many-to-many relationship between EQ test and Result."""
    eq_test = models.ForeignKey('EQTest', on_delete=models.CASCADE)
    result = models.ForeignKey('Result', on_delete=models.CASCADE)


class EQTest(ModelWithDurationField):
    """EQ test model."""
    result = models.ManyToManyField(Result, through=EQTestResult)


class Test(models.Model):
    """Model of test."""
    login = ShortUUIDField(length=settings.TEST_UUID_LENGTH, primary_key=True)
    iq_test = models.ForeignKey(IQTest, on_delete=models.CASCADE)
    eq_test = models.ForeignKey(EQTest, on_delete=models.CASCADE)
    start_date = models.DateTimeField(default=timezone.now)
