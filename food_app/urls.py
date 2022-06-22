from rest_framework import routers

from food_app.views import FoodViewSet

food_router = routers.DefaultRouter()
food_router.register(r'', FoodViewSet)
