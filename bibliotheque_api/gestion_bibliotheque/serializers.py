from rest_framework import serializers
from .models import Auteur, Livre, Categorie, Exemplaire, Emprunt, Commentaire, Evaluation, Editeur

class AuteurSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Auteur
        fields = '__all__'

class LivreSerializer(serializers.HyperlinkedModelSerializer):
    auteurs = AuteurSerializer(many=True)  # Utilisation d'AuteurSerializer

    class Meta:
        model = Livre 
        fields = '__all__'

    def to_representation(self, instance):
        # Modifie la représentation pour ne montrer que les URLs des auteurs
        representation = super().to_representation(instance)
        representation['auteurs'] = [auteur['url'] for auteur in representation['auteurs']]
        return representation

class CategorieSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Categorie
        fields = '__all__'

class ExemplaireSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Exemplaire
        fields = '__all__'

class EmpruntSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Emprunt
        fields = '__all__'

class CommentaireSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Commentaire
        fields = '__all__'

class EvaluationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Evaluation
        fields = '__all__'
