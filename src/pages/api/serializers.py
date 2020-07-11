from rest_framework import serializers

from pages.models import Page


class PageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Page
        fields = [
            'id',
            'title',
            'slug',
            'content',
            'created_at',
            'updated_at',
        ]
