from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from . import serializers
from .utils import create_new_test
from ..verification.models import Test


@api_view(['GET'])
def test_create_view(request):
    """Create test."""
    if request.method == 'GET':
        test = create_new_test()
        serializer = serializers.TestCreateSerializer(test)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def test_result_view(request, login):
    """View test result."""
    if request.method == 'GET':
        test = get_object_or_404(Test, login=login)
        serializer = serializers.TestViewSerializer(test)
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def finish_iq_test(request, login):
    """Save iq test result."""
    request.data['login'] = login
    serializer = serializers.IQTestSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save(login=login)
        return Response(status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def finish_eq_test(request, login):
    """Save eq test result."""
    request.data['login'] = login
    serializer = serializers.EQTestSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save(login=login)
        return Response(status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
