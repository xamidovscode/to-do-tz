from rest_framework import serializers
from . import models
from datetime import datetime, timezone


class TaskSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Task
        fields = (
            "id",
            'title',
            'description',
            'status',
            'due_date',
            'user_data'
        )

    def validate(self, attrs):
        due_date = attrs.get("due_date")
        now = datetime.now(timezone.utc)  # Use the same timezone as `due_date`
        if due_date and due_date <= now:
            raise serializers.ValidationError({"due_date": "Due date must be in the future."})
        return attrs