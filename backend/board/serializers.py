from rest_framework import serializers
from .models import BoardVO as board


class BoardSerializer(serializers.Serializer):
    # id = serializers.IntegerField()
    title = serializers.CharField()
    content = serializers.CharField()
    created_at = serializers.DateTimeField(read_only=True)
    updated_at = serializers.DateTimeField(read_only=True)

    class Meta:
        medel = board
        fields = '__all__'

    def create(self, validated_data):
        return board.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.content = validated_data.get('context', instance.content)
        return instance
