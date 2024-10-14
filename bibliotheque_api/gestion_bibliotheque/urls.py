from rest_framework.routers import DefaultRouter
from .views import AuteurViewSet, LivreViewSet, ExemplaireViewSet

router = DefaultRouter()
router.register(r'auteurs', AuteurViewSet)
router.register(r'livres', LivreViewSet)
router.register(r'exemplaires', ExemplaireViewSet)

urlpatterns = router.urls
