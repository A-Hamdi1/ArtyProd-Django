from django.forms import IntegerField
from rest_framework.serializers import ModelSerializer
from artyweb.models import Client, DemandeProjet, Formateur, Formation, Panier, Personnel, Equipe, Projet, Service
 
class EquipeSerializer(ModelSerializer):
 
    class Meta:
        model = Equipe
        fields = ['id', 'nom', 'description', 'image']

class PersonnelSerializer(ModelSerializer):
    equipe_id = IntegerField()

    class Meta:
        model = Personnel
        fields = ['id', 'nom', 'cv', 'equipe_id']

class ClientSerializer(ModelSerializer):
    class Meta:
        model = Client
        fields = ['id', 'user', 'address', 'phone_number']


class ServiceSerializer(ModelSerializer):
    class Meta:
        model = Service
        fields = ['id', 'nom', 'description', 'type', 'image']


class ProjetSerializer(ModelSerializer):
    class Meta:
        model = Projet
        fields = ['id', 'libelle', 'description', 'date_debut', 'date_fin', 'acheve', 'image', 'service', 'equipe']


class FormationSerializer(ModelSerializer):
    class Meta:
        model = Formation
        fields = ['id', 'nom', 'photo', 'description', 'datedebut', 'datefin', 'nbheure_semaine', 'prix', 'formateur', 'lienmeet', 'service']

class FormateurSerializer(ModelSerializer):
    class Meta:
        model = Formateur
        fields = ['id', 'fullname', 'photo', 'domaine', 'rating']

class DemandeProjetSerializer(ModelSerializer):
    class Meta:
        model = DemandeProjet
        fields = ['id', 'libelle', 'description', 'date_demande', 'service','equipe','client','statut']

class PanierSerializer(ModelSerializer):
    class Meta:
        model = Panier
        fields = ['id', 'user', 'formations', 'date_ajout', 'quantite','total_prix']