from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    AuteurViewSet,
    LivreViewSet,
    CategorieViewSet,
    ExemplaireViewSet,
    EmpruntViewSet,
    CommentaireViewSet,
    EvaluationViewSet,
    LogoutView,
)

router = DefaultRouter()
router.register(r'auteurs', AuteurViewSet)
router.register(r'livres', LivreViewSet)
router.register(r'categories', CategorieViewSet)
router.register(r'exemplaires', ExemplaireViewSet)
router.register(r'emprunts', EmpruntViewSet)
router.register(r'commentaires', CommentaireViewSet)
router.register(r'evaluations', EvaluationViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('logout/', LogoutView.as_view(), name='logout'),
]
