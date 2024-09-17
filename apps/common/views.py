from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.pagination import PageNumberPagination
from . import serializers
from . import models


class CustomPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 10000


class TaskModelViewSet(viewsets.ModelViewSet):
    queryset = models.Task.objects.filter(is_active=True)
    serializer_class = serializers.TaskSerializer
    lookup_field = 'pk'
    filter_backends = (DjangoFilterBackend,)
    filterset_fields = ('status', 'due_date')
    permission_classes = [IsAuthenticated]
    pagination_class = CustomPagination

    def perform_destroy(self, instance):
        instance.is_active = False
        instance.save()



