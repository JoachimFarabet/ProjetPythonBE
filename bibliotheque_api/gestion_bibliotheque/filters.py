import django_filters
from gestion_bibliotheque.models import Auteur
from gestion_bibliotheque.models import Livre

class AuteurFilter(django_filters.FilterSet):
    date_de_naissance = django_filters.DateFromToRangeFilter()
    nom = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Auteur
        fields = ['nom', 'nationalite', 'date_de_naissance']

class LivreFilter(django_filters.FilterSet):
    titre = django_filters.CharFilter(lookup_expr='icontains')
    date_publication = django_filters.DateFromToRangeFilter()
    
    class Meta:
        model = Livre
        fields = ['titre', 'auteurs', 'categorie', 'editeur', 'date_publication']