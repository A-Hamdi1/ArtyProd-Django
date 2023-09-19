from django.contrib import admin
from .models import Client, Formateur, Formation, Panier,Service,Projet,Equipe,Personnel,DemandeProjet

# Register your models here.
admin.site.register(Client)
admin.site.register(Service)
admin.site.register(Formation)
admin.site.register(Formateur)
admin.site.register(Panier)
admin.site.register(Projet)
admin.site.register(Equipe)
admin.site.register(Personnel)
admin.site.register(DemandeProjet)

