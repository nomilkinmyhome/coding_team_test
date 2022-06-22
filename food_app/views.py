from django.db.models import Prefetch
from rest_framework import viewsets

from food_app.models import Food, FoodCategory
from food_app.serializers import FoodListSerializer


class FoodViewSet(viewsets.ModelViewSet):
    serializer_class = FoodListSerializer
    queryset = FoodCategory.objects.filter(food__is_publish=True).prefetch_related(
        Prefetch(
            'food',
            queryset=Food.objects.filter(is_publish=True),
        ),
    ).distinct()
