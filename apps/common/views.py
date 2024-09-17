from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.pagination import PageNumberPagination
from rest_framework.exceptions import PermissionDenied
from . import serializers
from . import models


class CustomPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 10000


class TaskModelViewSet(viewsets.ModelViewSet):
    queryset = models.Task.objects.filter(is_active=True).select_related("user")
    serializer_class = serializers.TaskSerializer
    lookup_field = 'pk'
    filter_backends = (DjangoFilterBackend,)
    filterset_fields = ('status', 'due_date')
    permission_classes = [IsAuthenticated]
    pagination_class = CustomPagination

    def perform_destroy(self, instance):
        if instance.user != self.request.user:
            raise PermissionDenied("You do not have permission to delete this task.")
        instance.is_active = False
        instance.save()


    def perform_update(self, serializer):
        if serializer.instance.user != self.request.user:
            raise PermissionDenied("You do not have permission to update this task.")
        serializer.save()

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)



