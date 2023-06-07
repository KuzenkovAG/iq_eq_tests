from rest_framework import serializers


class CreatableSlugRelatedField(serializers.SlugRelatedField):
    """Slug related field with get or create obj."""
    def to_internal_value(self, data):
        return self.get_queryset().get_or_create(result=data)[0]
