from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import DemandeProjet, Equipe, Formation, Personnel, Service, Projet

class ContactForm(forms.Form):
    name = forms.CharField(max_length=100, required=True)
    email = forms.EmailField(required=True)
    subject = forms.CharField(max_length=100, required=True)
    message = forms.CharField(widget=forms.Textarea, required=True)


class UserRegistrationForm(UserCreationForm):
    first_name = forms.CharField(label='Prénom')
    last_name = forms.CharField(label='Nom')
    email = forms.EmailField(label='Adresse e-mail')

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')

class ServiceForm(forms.ModelForm):
    class Meta:
        model = Service
        fields = ['nom', 'description', 'image']
        widgets = {
            'nom': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
            'image': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }

class ProjetForm(forms.ModelForm):
    class Meta:
        model = Projet
        fields = ('libelle', 'description', 'date_debut', 'date_fin', 'acheve', 'image', 'service', 'equipe')
        widgets = {
            'date_debut': forms.DateInput(attrs={'type': 'date'}),
            'date_fin': forms.DateInput(attrs={'type': 'date'})
        }    

class EquipForm(forms.ModelForm):
    class Meta:
        model = Equipe
        fields = ['nom', 'description', 'image']
        widgets = {
            'nom': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
            'image': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }
        
        
class PersonnelForm(forms.ModelForm):
    equipe = forms.ModelChoiceField(queryset=Equipe.objects.all(), widget=forms.Select(attrs={'class': 'form-control'}))
    class Meta:
        model = Personnel
        fields = ['nom', 'cv', 'photo','equipe']
        widgets = {
            'nom': forms.TextInput(attrs={'class': 'form-control'}),
            'cv': forms.Textarea(attrs={'class': 'form-control'}),
            'photo': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        } 
        
        
class DemandeProjetForm(forms.ModelForm):
    class Meta:
        model = DemandeProjet
        exclude = ['client', 'date_demande', 'statut', 'equipe']
        labels = {
            'libelle': 'Libellé',
            'description': 'Description',
            'service': 'Service',
        } 

class DemandeProjetEditForm(forms.ModelForm):
    class Meta:
        model = DemandeProjet
        exclude = ['client', 'libelle', 'description', 'service', 'date_demande' ]
        labels = {
            'statut': 'Statut',
            'equipe': 'Equipe',
        }
        
class FormationForm(forms.ModelForm):
    class Meta:
        model = Formation
        fields = ['nom', 'photo', 'description', 'datedebut', 'datefin', 'nbheure_semaine', 'formateur', 'lienmeet', 'service']
        widgets = {
            'datedebut': forms.DateInput(attrs={'type': 'date'}),
            'datefin': forms.DateInput(attrs={'type': 'date'})
        }