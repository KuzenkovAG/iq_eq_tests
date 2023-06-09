import datetime as dt

from django.conf import settings
from rest_framework import serializers
from rest_framework.validators import ValidationError

from .fields import CreatableSlugRelatedField
from ..verification.models import EQTest, EQTestResult, IQTest, Result, Test

RESULT_LEN = 5


class TestCreateSerializer(serializers.ModelSerializer):
    """Serializer for create test."""
    class Meta:
        model = Test
        fields = ('login',)


class IQTestSerializer(serializers.ModelSerializer):
    """Serializer for update IQ test."""
    class Meta:
        model = IQTest
        fields = ('result', 'duration',)
        read_only = ('duration',)

    def validate(self, data):
        test = self.instance
        if test.iq_test.duration is not None:
            raise ValidationError('Test already passed.')
        return data

    def update(self, test, validated_data):
        duration = dt.datetime.now(dt.timezone.utc) - test.start_date
        test.iq_test.duration = duration
        test.iq_test.result = validated_data.get('result')
        test.iq_test.save()
        return test.iq_test


class EQTestSerializer(serializers.ModelSerializer):
    """Serializer for update EQ test."""
    result = CreatableSlugRelatedField(
        many=True, slug_field='result', queryset=Result.objects.all()
    )

    class Meta:
        model = EQTest
        fields = ('result', 'duration',)
        read_only = ('duration',)

    def validate_result(self, values):
        for value in values:
            if value.result not in settings.AVAILABLE_CHOICES:
                available = ', '.join(settings.AVAILABLE_CHOICES)
                raise ValidationError(
                    f'Each element should be in list - {available}.'
                )
        if len(values) != RESULT_LEN:
            raise ValidationError(
                f'Results should be have only {RESULT_LEN} elements.'
            )
        return values

    def validate(self, data):
        test = self.instance
        if test.eq_test.duration is not None:
            raise ValidationError('Test already passed.')
        return data

    def update(self, test, validated_data):
        results = validated_data.get('result')
        duration = dt.datetime.now(dt.timezone.utc) - test.start_date
        test.eq_test.duration = duration
        test.eq_test.save()
        EQTestResult.objects.filter(eq_test=test.eq_test).delete()
        objects = [
            EQTestResult(eq_test=test.eq_test, result=result)
            for result in results
        ]
        EQTestResult.objects.bulk_create(objects)
        return test.eq_test


class TestViewSerializer(serializers.ModelSerializer):
    """Serializer for View test results."""
    iq_test = IQTestSerializer()
    eq_test = EQTestSerializer()

    class Meta:
        model = Test
        fields = ('login', 'iq_test', 'eq_test')
