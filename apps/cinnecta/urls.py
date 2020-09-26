from rest_framework.routers import SimpleRouter

from .views import (
    TextsViewSet,
)

router = SimpleRouter()
router.register('text', TextsViewSet)