from rest_framework.routers import DefaultRouter
from . import views


router = DefaultRouter()
router.register(r'chats', views.ChatViewSet, base_name='Thread')

urlpatterns = router.urls