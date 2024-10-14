from django.db import models

class Auteur(models.Model):
    nom = models.CharField(max_length=255)
    biographie = models.TextField()
    date_de_naissance = models.DateField()
    date_de_deces = models.DateField(null=True, blank=True)
    nationalite = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='auteurs_photos/', null=True, blank=True)

    def __str__(self):
        return self.nom

class Categorie(models.Model):
    nom = models.CharField(max_length=255)
    description = models.TextField()
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.nom

class Editeur(models.Model):
    nom = models.CharField(max_length=255)
    adresse = models.CharField(max_length=255)
    site_web = models.URLField(null=True, blank=True)
    email_contact = models.EmailField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    logo = models.ImageField(upload_to='editeurs_logos/', null=True, blank=True)

    def __str__(self):
        return self.nom

class Livre(models.Model):
    titre = models.CharField(max_length=255)
    resume = models.TextField()
    date_de_publication = models.DateField()
    isbn = models.CharField(max_length=13, unique=True)
    nombre_de_pages = models.IntegerField()
    langue = models.CharField(max_length=50)
    image_de_couverture = models.ImageField(upload_to='livres_couvertures/', null=True, blank=True)
    format = models.CharField(max_length=50, choices=[('Broché', 'Broché'), ('Relié', 'Relié'), ('Numérique', 'Numérique')])
    categorie = models.ForeignKey(Categorie, on_delete=models.CASCADE, related_name='livres')
    auteurs = models.ManyToManyField(Auteur, related_name='livres')
    editeur = models.ForeignKey(Editeur, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.titre

class Exemplaire(models.Model):
    livre = models.ForeignKey(Livre, on_delete=models.CASCADE, related_name='exemplaires')
    etat = models.CharField(max_length=50)
    date_acquisition = models.DateField()
    localisation = models.CharField(max_length=255)
    disponibilite = models.BooleanField(default=True)

    def __str__(self):
        return f'Exemplaire de {self.livre.titre}'

class Emprunt(models.Model):
    exemplaire = models.ForeignKey(Exemplaire, on_delete=models.CASCADE, related_name='emprunts')
    utilisateur = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    date_emprunt = models.DateTimeField(auto_now_add=True)
    date_retour_prevue = models.DateTimeField()
    date_retour_effective = models.DateTimeField(null=True, blank=True)
    statut = models.CharField(max_length=50, choices=[('En cours', 'En cours'), ('Terminé', 'Terminé'), ('En retard', 'En retard')])
    remarques = models.TextField(null=True, blank=True)

    def __str__(self):
        return f'{self.utilisateur.username} - {self.exemplaire.livre.titre}'

class Commentaire(models.Model):
    utilisateur = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    livre = models.ForeignKey(Livre, on_delete=models.CASCADE, related_name='commentaires')
    contenu = models.TextField()
    date_publication = models.DateTimeField(auto_now_add=True)
    visible = models.BooleanField(default=True)
    modere = models.BooleanField(default=False)

    def __str__(self):
        return f'Commentaire de {self.utilisateur.username} sur {self.livre.titre}'

class Evaluation(models.Model):
    utilisateur = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    livre = models.ForeignKey(Livre, on_delete=models.CASCADE, related_name='evaluations')
    note = models.IntegerField()
    commentaire = models.TextField(null=True, blank=True)
    date_evaluation = models.DateTimeField(auto_now_add=True)
    recommande = models.BooleanField(default=False)

    def __str__(self):
        return f'Évaluation de {self.utilisateur.username} - {self.livre.titre} : {self.note}/5'
