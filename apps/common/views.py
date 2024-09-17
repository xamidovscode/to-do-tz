from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from . import serializers
from . import models


class TaskModelViewSet(viewsets.ModelViewSet):
    queryset = models.Task.objects.filter(is_active=True)
    serializer_class = serializers.TaskSerializer
    lookup_field = 'pk'
    filter_backends = (DjangoFilterBackend,)
    filterset_fields = ('status', )

    def perform_destroy(self, instance):
        instance.is_active = False
        instance.save()



