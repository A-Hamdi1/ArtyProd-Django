from django.urls import include, path
from rest_framework import routers
from . import views
from .views import ClientAPIView, DemandeProjetAPIView, EquipeAPIView, FormateurAPIView, FormationAPIView, PanierAPIView, PersonnelViewSet, ProjetAPIView, ServiceAPIView

router = routers.DefaultRouter()
router.register('personnel', PersonnelViewSet)

urlpatterns = [	
               
    #----------------------------API------------------------------------------
               
    path('api/equipe/', EquipeAPIView.as_view()),
    path('api/client/', ClientAPIView.as_view()),
    path('api/service/', ServiceAPIView.as_view()),
    path('api/projet/', ProjetAPIView.as_view()),
    path('api/formation/', FormationAPIView.as_view()),
    path('api/formateur/', FormateurAPIView.as_view()),
    path('api/demandeprojet/', DemandeProjetAPIView.as_view()),
    path('api/panier/', PanierAPIView.as_view()),
    path('api/', include(router.urls)),
    #---------------------Portfolio------------------------------------------
    path('projet/<int:projet_id>/', views.detailprojet, name='detailprojet'),
    path('', views.projet, name='projet'),
    
    
    
    
    
    
    
    path('add_projet/', views.add_projet, name='add_projet'),
    path('projet/<int:projet_id>/delete/', views.delete_projet, name='delete_projet'),
    path('projet/<int:projet_id>/edit/', views.edit_projet, name='edit_projet'),

    #-----------------------------SERVICE------------------------------------
    path('services/<int:service_id>/projets/', views.filter_projet, name='projets'),
    path('projet/<int:pk>/', views.filter_projet, name='projet'),
    path('add_service/', views.add_service, name='add_service'),
    path('services/<int:service_id>/edit/', views.edit_service, name='edit_service'),
    path('services/<int:service_id>/delete/', views.delete_service, name='delete_service'),
    #--------------------------------EQUIPE-------------------------------------
    path('equipe/',views.equipe, name = 'equipe'),
    path('equipe/', views.equipe, name='equipe'),
    path('add_equipe/', views.add_equipe, name='add_equipe'),
    path('equipes/<int:equipe_id>/edit/', views.edit_equipe, name='edit_equipe'),
    path('equipes/<int:equipe_id>/delete/', views.delete_equipe, name='delete_equipe'),

    #--------------------------------PERSONNEL---------------------------------------
    path('personnel/<int:equipe_id>/', views.personnel, name='personnel'),
    path('personnel/add/', views.add_personnel, name='add_personnel'),
    path('personnel/<int:personnel_id>/edit/', views.edit_personnel, name='edit_personnel'),
    path('personnel/<int:personnel_id>/delete/', views.delete_personnel, name='delete_personnel'),
    
    #--------------------------------FORMATION---------------------------------------
    path('service/<int:service_id>/formations/', views.formations, name='formations'),
    path('ajouter-formation/', views.ajouter_formation, name='ajouter_formation'),
    path('modifier-formation/<int:formation_id>/', views.modifier_formation, name='modifier_formation'),
    path('supprimer-formation/<int:formation_id>/', views.supprimer_formation, name='supprimer_formation'),
    
    
    path('supprimer-formation2/<int:form_id>/', views.supprimer_formation2, name='supprimer_formation2'),
    path('ajouter_formation2/', views.ajouter_formation2, name='ajouter_formation2'),
    path('formation/modifier/<int:formation_id>/', views.modifier_formation2, name='modifier_formation2'),

    #--------------------------------ALL FORMATION---------------------------------------
    path('formations/', views.allformations, name='all_formations'),

    
    #--------------------------------FORMATEUR---------------------------------------
    path('formateur/<int:formateur_id>/', views.formateur_detail, name='formateur_detail'),
    
    #--------------------------------PANIER-------------------------------------------
    path('panier/', views.panier, name='panier'),
    path('formation/<int:formation_id>/ajouter-au-panier/', views.ajouter_au_panier, name='ajouter_au_panier'),
    path('panier/supprimer/<int:formation_id>/', views.supprimer_formation_panier, name='supprimer_formation_panier'),
    path('panier/vider/', views.vider_panier, name='vider_panier'),

    path('confirmer-commande/', views.confirmer_commande, name='confirmer_commande'),

#--------------------------------DEMANDE PROJET---------------------------------------
    path('demande_projet/', views.demande_projet, name='demande_projet'),
    path('demande_projet_list/', views.demande_projet_list, name='demande_projet_list'),
    path('demande_projet/<int:demande_projet_id>/edit/', views.modifier_demande_projet, name='modifier_demande_projet'),
    path('demande_projet/<int:demande_projet_id>/delete/', views.supprimer_demande_projet, name='supprimer_demande_projet'),


    #---------------------------------CONTACT------------------------------------------
    path('service/', views.services, name='service'),
    path('contact/', views.contact, name='contact'),
    ]
