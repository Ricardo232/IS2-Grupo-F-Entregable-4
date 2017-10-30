from django.shortcuts import render
from .models import Character


# Create your views here.

def menu(request):
    all_characters = Character.objects.all()

    names = ['Class']
    images = ['']
    health = ['Health']
    mana = ['Mana']
    damage = ['Damage']
    defense = ['Defense']

    for character in all_characters:
        names.append(character.character_name)
        images.append(character.img_path)
        health.append(character.base_health)
        mana.append(character.base_mana)
        damage.append(character.base_damage)
        defense.append(character.base_defense)

    info = [names, health, mana, damage, defense]

    return render(request, 'ConfigGenerator/menu.html', {'info': info,
                                                         'images': images})
