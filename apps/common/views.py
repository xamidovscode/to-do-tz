from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from . import serializers
from . import models


class TaskModelViewSet(viewsets.ModelViewSet):
    queryset = models.Task.objects.filter(is_active=True)
    serializer_class = serializers.TaskSerializer
    lookup_field = 'pk'
    filter_backends = (DjangoFilterBackend,)
    filterset_fields = ('status', 'due_date')
    permission_classes = [IsAuthenticated]

    def perform_destroy(self, instance):
        instance.is_active = False
        instance.save()



