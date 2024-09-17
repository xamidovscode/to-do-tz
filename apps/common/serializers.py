from rest_framework import serializers
from . import models


class TaskSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Task
        fields = (
            "id",
            'title',
            'description',
            'status',
            'due_date',
            'user',
            'user_data'
        )