from rest_framework import viewsets, filters
from .models import Auteur, Livre, Categorie, Exemplaire, Emprunt, Commentaire, Evaluation
from .serializers import (
    AuteurSerializer,
    LivreSerializer,
    CategorieSerializer,
    ExemplaireSerializer,
    EmpruntSerializer,
    CommentaireSerializer,
    EvaluationSerializer,
)
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.pagination import PageNumberPagination
from .filters import AuteurFilter
from .filters import LivreFilter

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from .CustomTokenAuthentication import CustomTokenAuthentication
from .permissions import HasGroupPermission

class LogoutView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        request.user.auth_token.delete()  # Supprimer le token de l'utilisateur
        return Response(status=status.HTTP_200_OK)

class StandardResultsSetPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 100

class AuteurViewSet(viewsets.ModelViewSet):
    queryset = Auteur.objects.all()
    serializer_class = AuteurSerializer
    authentication_classes = [CustomTokenAuthentication]
    permission_classes = [HasGroupPermission]
    pagination_class = StandardResultsSetPagination
    filter_backends = [filters.SearchFilter, filters.OrderingFilter, DjangoFilterBackend]
    search_fields = ['nom', 'biographie', 'nationalite']
    ordering_fields = ['nom', 'date_de_naissance', 'nationalite']
    filterset_fields = ['nationalite']
    
    permission_groups = {
        'create': ['Admin'],
        'partial_update': ['Admin'],
        'retrieve': ['User', 'Admin'],
        'list': ['User', 'Admin'],
    }

class LivreViewSet(viewsets.ModelViewSet):
    queryset = Livre.objects.all()
    serializer_class = LivreSerializer
    authentication_classes = [CustomTokenAuthentication]
    permission_classes = [IsAuthenticated] 
    pagination_class = StandardResultsSetPagination
    filter_backends = [filters.SearchFilter, filters.OrderingFilter, DjangoFilterBackend]
    search_fields = ['titre', 'auteurs__nom', 'categorie__nom']
    ordering_fields = ['titre', 'date_publication', 'categorie']
    filterset_class = LivreFilter

class CategorieViewSet(viewsets.ModelViewSet):
    queryset = Categorie.objects.all()
    serializer_class = CategorieSerializer
    authentication_classes = [CustomTokenAuthentication]
    permission_classes = [IsAuthenticated]

class ExemplaireViewSet(viewsets.ModelViewSet):
    queryset = Exemplaire.objects.all()
    serializer_class = ExemplaireSerializer
    authentication_classes = [CustomTokenAuthentication]
    permission_classes = [IsAuthenticated]

class EmpruntViewSet(viewsets.ModelViewSet):
    queryset = Emprunt.objects.all()
    serializer_class = EmpruntSerializer
    authentication_classes = [CustomTokenAuthentication]
    permission_classes = [IsAuthenticated]

class CommentaireViewSet(viewsets.ModelViewSet):
    queryset = Commentaire.objects.all()
    serializer_class = CommentaireSerializer
    authentication_classes = [CustomTokenAuthentication]
    permission_classes = [IsAuthenticated]

class EvaluationViewSet(viewsets.ModelViewSet):
    queryset = Evaluation.objects.all()
    serializer_class = EvaluationSerializer
    authentication_classes = [CustomTokenAuthentication]
    permission_classes = [IsAuthenticated]
