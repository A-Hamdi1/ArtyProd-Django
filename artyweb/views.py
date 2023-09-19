from django.conf import settings
from django.shortcuts import get_object_or_404, redirect, render
from .models import Client, Commande, DemandeProjet, Equipe, Formateur, Formation, Panier, Projet, Service, Personnel
from django.core.mail import send_mail
from django.views.decorators.http import require_POST
from .forms import  DemandeProjetEditForm, DemandeProjetForm, EquipForm, FormationForm, PersonnelForm, ProjetForm, ServiceForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
#@user_passes_test(lambda u: u.is_superuser)#, login_url='/error/'
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from artyweb.serializers import ClientSerializer, DemandeProjetSerializer, EquipeSerializer, FormateurSerializer, FormationSerializer, PanierSerializer, PersonnelSerializer, ProjetSerializer, ServiceSerializer
from django.urls import reverse
from paypal.standard.forms import PayPalPaymentsForm
from django.db import transaction


#--------------------------------------------------LES API------------------------------------------------------------------

class EquipeAPIView(APIView):
    def get(self, *args, **kwargs):
        equipe = Equipe.objects.all()
        serializer = EquipeSerializer(equipe, many=True)
        return Response(serializer.data)

class PersonnelViewSet(ModelViewSet):
    queryset = Personnel.objects.all()
    serializer_class = PersonnelSerializer

    def get_queryset(self):
        queryset = super().get_queryset()
        equipe_id = self.request.GET.get('equipe_id')
        if equipe_id:
            queryset = queryset.filter(equipe_id=equipe_id)
        return queryset

class ClientAPIView(APIView):
    def get(self, *args, **kwargs):
        client = Client.objects.all()
        serializer = ClientSerializer(client, many=True)
        return Response(serializer.data)
    
    
class ServiceAPIView(APIView):
    def get(self, *args, **kwargs):
        service = Service.objects.all()
        serializer = ServiceSerializer(service, many=True)
        return Response(serializer.data)

class ProjetAPIView(APIView):
    def get(self, *args, **kwargs):
        projet = Projet.objects.all()
        serializer = ProjetSerializer(projet, many=True)
        return Response(serializer.data)
    
class FormationAPIView(APIView):
    def get(self, *args, **kwargs):
        formation = Formation.objects.all()
        serializer = FormationSerializer(formation, many=True)
        return Response(serializer.data)

class FormateurAPIView(APIView):
    def get(self, *args, **kwargs):
        formateur = Formateur.objects.all()
        serializer = FormateurSerializer(formateur, many=True)
        return Response(serializer.data)

class DemandeProjetAPIView(APIView):
    def get(self, *args, **kwargs):
        demande_projet = DemandeProjet.objects.all()
        serializer = DemandeProjetSerializer(demande_projet, many=True)
        return Response(serializer.data)

class PanierAPIView(APIView):
    def get(self, *args, **kwargs):
        panier = Panier.objects.all()
        serializer = PanierSerializer(panier, many=True)
        return Response(serializer.data)

#--------------------------------------------------DEMANDE PROJETS------------------------------------------------------------------
@login_required
def demande_projet(request):
    if request.method == 'POST':
        form = DemandeProjetForm(request.POST, request.FILES)
        if form.is_valid():
            demande_projet = form.save(commit=False)
            if request.user.is_authenticated:
                client = Client.objects.get(user=request.user)
                demande_projet.client = client
                demande_projet.save()
                messages.success(request, 'Votre demande de projet a été soumise avec succès.')
                return redirect('projet')
            else:
                messages.error(request, 'Vous devez être connecté pour soumettre une demande de projet.')
    else:
        form = DemandeProjetForm()
    return render(request, 'artyweb/demandeprojet/demandeprojet.html', {'form': form})

def demande_projet_list(request):
    demandes_projet = DemandeProjet.objects.all()
    return render(request, 'artyweb/demandeprojet/demande_projet_list.html', {'demandes_projet': demandes_projet})


#---------------------------------------------------CRUD DEMANDE PROJET-----------------------------------------------------------------
def modifier_demande_projet(request, demande_projet_id):
    demande_projet = get_object_or_404(DemandeProjet, id=demande_projet_id)
    if request.method == 'POST':
        form = DemandeProjetEditForm(request.POST, instance=demande_projet)
        if form.is_valid():
            form.save()
            return redirect('demande_projet_list')
    else:
        form = DemandeProjetEditForm(instance=demande_projet)
    return render(request, 'artyweb/demandeprojet/modifier_demande_projet.html', {'form': form})

def supprimer_demande_projet(request, demande_projet_id):
    demande_projet = get_object_or_404(DemandeProjet, id=demande_projet_id)
    demande_projet.delete()
    return redirect('demande_projet_list')

#-----------------------------------------------PORTFOLIO--------------------------------------------------------------------------

def projet(request):	
  list= Projet.objects.all()
  return render( request, 'artyweb/portfolio/portfolio.html',{'list':list} )

@login_required
def detailprojet(request, projet_id):
    projet = get_object_or_404(Projet, pk=projet_id)
    return render(request, 'artyweb/portfolio/detailprojet.html', {'projet': projet})

#-----------------------------------------------SERVICES--------------------------------------------------------------------------
def services(request):
    services = Service.objects.all()
    return render(request, 'artyweb/service/services.html', {'services': services})

def filter_projet(request, service_id):
    service = get_object_or_404(Service, pk=service_id)
    projets = Projet.objects.filter(service=service)
    return render(request, 'artyweb/service/filter_projet.html', {'service': service, 'projets': projets})

#------------------------------------------------EQUIPE--------------------------------------------------------------------------
@login_required
def personnel(request, equipe_id):
    equipe = get_object_or_404(Equipe, pk=equipe_id)
    personnels = Personnel.objects.filter(equipe=equipe)
    context = {
        'equipe': equipe,
        'personnels': personnels,
    }
    return render(request, 'artyweb/personnel/personnel.html', context)

def equipe(request):
    equipe= Equipe.objects.all()
    return render(request, 'artyweb/equipe/equipe.html', {'equipe': equipe})

#-----------------------------------------------CONTACT--------------------------------------------------------------------------
#@user_passes_test(lambda u: u.is_superuser)
def contact(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        subject=request.POST['subject']
        message = request.POST['message']

        message_body = f"Name: {name}\nEmail: {email}\nSubject: {subject}\nMessage: {message}"

        send_mail(
            'Contact Form Submission',
            message_body,
            settings.DEFAULT_FROM_EMAIL,
            ['majdhamila.isams@gmail.com'],
            fail_silently=False,
        )
        return render(request, 'artyweb/contact/contact.html', {'success': True})
    return render(request, 'artyweb/contact/contact.html')


#-------------------------------------------CRUD SERVICES------------------------------------------------
@require_POST
def delete_service(request, service_id):
    service = get_object_or_404(Service, id=service_id)
    service.delete()
    return redirect('service')

def edit_service(request, service_id):
    service = get_object_or_404(Service, id=service_id)
    if request.method == 'POST':
        form = ServiceForm(request.POST, request.FILES, instance=service)
        if form.is_valid():
            form.save()
            return redirect('service')
    else:
        form = ServiceForm(instance=service)
    return render(request, 'artyweb/service/edit_service.html', {'form': form})

def add_service(request):
    if request.method == 'POST':
        form = ServiceForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('service')
    else:
        form = ServiceForm()
    return render(request, 'artyweb/service/add_service.html', {'form': form})
#----------------------------------------CRUD PORTFOLIO----------------------------------------------------------------
def delete_projet(request, projet_id):
    projet = get_object_or_404(Projet, id=projet_id)
    projet.delete()
    return redirect('projet')

def edit_projet(request, projet_id):
    projet = get_object_or_404(Projet, id=projet_id)
    if request.method == 'POST':
        form = ProjetForm(request.POST, request.FILES, instance=projet)
        if form.is_valid():
            form.save()
            return redirect('projet')
    else:
        form = ProjetForm(instance=projet)
    return render(request, 'artyweb/portfolio/edit_projet.html', {'form': form})

def add_projet(request):
    if request.method == 'POST':
        form = ProjetForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('projet')
    else:
        form = ProjetForm()
    return render(request, 'artyweb/portfolio/add_projet.html', {'form': form})
#----------------------------------------------- CRUD EQUIPE ------------------------------------------------------------
@require_POST
def delete_equipe(request, equipe_id):
    equipe = get_object_or_404(Equipe, id=equipe_id)
    equipe.delete()
    return redirect('equipe')

def edit_equipe(request, equipe_id):
    equipe = get_object_or_404(Equipe, id=equipe_id)
    if request.method == 'POST':
        form = EquipForm(request.POST, request.FILES, instance=equipe)
        if form.is_valid():
            form.save()
            return redirect('service')
    else:
        form = EquipForm(instance=equipe)
    return render(request, 'artyweb/equipe/edit_equipe.html', {'form': form})
def add_equipe(request):
    if request.method == 'POST':
        form = EquipForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('equipe')
    else:
        form = EquipForm()
    return render(request, 'artyweb/equipe/add_equipe.html', {'form': form})

#-------------------------------------------- CRUD PERSONNEL ----------------------------------------------------------------------

@require_POST
def delete_personnel(request, personnel_id):
    personnel = get_object_or_404(Personnel, id=personnel_id)
    personnel.delete()
    return redirect('equipe')

def edit_personnel(request, personnel_id):
    personnel = get_object_or_404(Personnel, id=personnel_id)
    if request.method == 'POST':
        form = PersonnelForm(request.POST, request.FILES, instance=personnel)
        if form.is_valid():
            form.save()
            return redirect('equipe')
    else:
        form = PersonnelForm(instance=personnel)
    return render(request, 'artyweb/personnel/edit_personnel.html', {'form': form})
def add_personnel(request):
    if request.method == 'POST':
        form = PersonnelForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('equipe')
    else:
        form = PersonnelForm()
    return render(request, 'artyweb/personnel/add_personnel.html', {'form': form})
#-------------------------------------------- CRUD FORMATION ----------------------------------------------------------------------

@login_required
def formations(request, service_id):
    formations = Formation.objects.filter(service_id=service_id)
    service = Service.objects.get(id=service_id)
    context = {'formations': formations, 'service': service}
    return render(request, 'artyweb/formation/formation.html', context)

@login_required
def allformations(request):
    formations = Formation.objects.all()
    return render(request, 'artyweb/formation/allformations.html', {'formations': formations})
@login_required
def supprimer_formation2(request, form_id):
    formation = get_object_or_404(Formation, pk=form_id)
    formations = Formation.objects.all()
    formation.delete()
    return render(request, 'artyweb/formation/allformations.html', {'formations': formations})

@login_required
def ajouter_formation2(request):
    formations = Formation.objects.all()    
    if request.method == 'POST':
        form = FormationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        return render(request, 'artyweb/formation/allformations.html', {'formations': formations})
    else:
        form = FormationForm()
    return render(request, 'artyweb/formation/ajouter_formation.html', {'form': form})
@login_required
def modifier_formation2(request, formation_id):
    formation = get_object_or_404(Formation, pk=formation_id)
    formations = Formation.objects.all()
    
    if request.method == 'POST':
        form = FormationForm(request.POST, instance=formation)
        if form.is_valid():
            form.save()
            return render(request, 'artyweb/formation/allformations.html', {'formations': formations})
    else:
        form = FormationForm(instance=formation)
    return render(request, 'artyweb/formation/modifier_formation.html', {'form': form})


@login_required
def ajouter_formation(request):
    if request.method == 'POST':
        form = FormationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('formations', service_id=form.cleaned_data['service'].id)
    else:
        form = FormationForm()
    context = {'form': form}
    return render(request, 'artyweb/formation/ajouter_formation.html', context)

@login_required
def modifier_formation(request, formation_id):
    formation = get_object_or_404(Formation, id=formation_id)
    if request.method == 'POST':
        form = FormationForm(request.POST, request.FILES, instance=formation)
        if form.is_valid():
            form.save()
            return redirect('formations', service_id=form.cleaned_data['service'].id)
    else:
        form = FormationForm(instance=formation)
    context = {'form': form, 'formation': formation}
    return render(request, 'artyweb/formation/modifier_formation.html', context)

def supprimer_formation(request, formation_id):
    formation = get_object_or_404(Formation, id=formation_id)
    formation.delete()
    return redirect('formations', service_id=formation.service.id)
#------------------------------------------------FORMATEUR-------------------------------------------------------------------------
@login_required
def formateur_detail(request, formateur_id):
    formateur = Formateur.objects.get(id=formateur_id)
    context = {'formateur': formateur}
    return render(request, 'artyweb/formation/formateur_detail.html', context)
#------------------------------------------------PANIER-------------------------------------------------------------------------
def panier(request):
    panier = Panier.objects.filter(user=request.user).first()
    return render(request, 'artyweb/panier.html', {'panier': panier})
def ajouter_au_panier(request, formation_id):
    formation = Formation.objects.get(id=formation_id)
    panier, created = Panier.objects.get_or_create(user=request.user)
    panier.formations.add(formation)
    messages.success(request, "La formation a été ajoutée à votre panier.")
    return redirect('panier')
def supprimer_formation_panier(request, formation_id):
    panier = Panier.objects.get(user=request.user)
    formation = Formation.objects.get(id=formation_id)
    panier.formations.remove(formation)
    return redirect('panier')
def vider_panier(request):
    if request.method == 'POST':
        panier = Panier.objects.get(user=request.user)
        panier.formations.clear()
    return redirect('panier')

@transaction.atomic
def create_order(user, panier):
    # Créer une commande vide pour l'utilisateur
    commande = Commande.objects.create(user=user)

@login_required
def confirmer_commande(request):
    panier = Panier.objects.get(user=request.user)
    total = panier.total_prix
    # Créer une commande dans votre base de données et récupérer l'ID de commande
    commande = create_order(request.user, panier)
    # Configuration pour PayPal
    paypal_dict = {
        'business': request.user.email,
        'amount': total,
        'currency_code': 'DT',
        'item_name': 'Formation sur ArtiWeb',
    }
    # Créer le formulaire PayPal et renvoyer le HTML pour le bouton de paiement
    form = PayPalPaymentsForm(initial=paypal_dict)
    context = {
        'form': form,
        'total': total,
    }
    return render(request, 'artyweb/confirmer_commande.html', context)
