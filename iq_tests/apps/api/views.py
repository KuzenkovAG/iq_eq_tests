from rest_framework import generics

from . import serializers, utils
from ..verification.models import Test


class TestCreateView(generics.CreateAPIView):
    """Create test."""
    serializer_class = serializers.TestCreateSerializer

    def perform_create(self, serializer):
        eq_test = utils.create_eq_test()
        iq_test = utils.create_iq_test()
        serializer.save(eq_test=eq_test, iq_test=iq_test)


class TestRetrieveView(generics.RetrieveAPIView):
    """Get test."""
    serializer_class = serializers.TestViewSerializer
    queryset = Test.objects.all()
    lookup_field = 'login'


class IQTestUpdateView(generics.UpdateAPIView):
    """Update iq test result."""
    serializer_class = serializers.IQTestSerializer
    queryset = Test.objects.all()
    lookup_field = 'login'

    def perform_update(self, serializer):
        login = self.kwargs.get('login')
        serializer.save(login=login)


class EQTestUpdateView(generics.UpdateAPIView):
    """Save eq test result."""
    serializer_class = serializers.EQTestSerializer
    queryset = Test.objects.all()
    lookup_field = 'login'

    def perform_update(self, serializer):
        login = self.kwargs.get('login')
        serializer.save(login=login)
