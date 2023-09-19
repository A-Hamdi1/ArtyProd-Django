from django import template

register = template.Library()

@register.filter
def user_belongs_to_team(user, equipe_nom):
    return user.groups.filter(name=equipe_nom).exists()
