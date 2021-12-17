from rest_framework import serializers

from .models import BookTime, ReserveBookTime


class BookTimeSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookTime
        fields = ['id', 'floor', 'parking_space_id', 'booking_start_time', 'booking_end_time']

    def validate(self, attrs):
        if attrs['booking_start_time'] > attrs['booking_end_time']:
            raise serializers.ValidationError({"end_time": "End time error"})
        return attrs


class ReserveSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReserveBookTime
        fields = ['id', 'book_time']
        read_only_fields = ['created_at', 'updated_at', 'owner']
