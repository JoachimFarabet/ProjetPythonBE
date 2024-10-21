from django.contrib.auth.models import Group
from rest_framework import permissions

def is_in_group(user, group_name):
    """
    Vérifie si un utilisateur appartient à un groupe.
    """
    try:
        return Group.objects.get(name=group_name).user_set.filter(id=user.id).exists()
    except Group.DoesNotExist:
        return False

class HasGroupPermission(permissions.BasePermission):
    """
    Permission personnalisée pour vérifier si l'utilisateur appartient à un groupe.
    """
    def has_permission(self, request, view):
        # Récupérer les groupes requis pour l'action en cours
        required_groups = view.permission_groups.get(view.action)

        if required_groups is None:
            return False

        # Vérifier si l'utilisateur essaye d'accéder à ses propres données
        if "IsSelf" in required_groups:
            if request.user.id == int(view.kwargs.get('pk')):
                return True

        # Vérifier si l'utilisateur appartient à l'un des groupes requis
        return any([is_in_group(request.user, group_name) for group_name in required_groups])
