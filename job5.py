def toilette(marche, hauteur):
    distance_jour = (marche * hauteur) * 2
    distance_semaine = distance_jour * 7
    return distance_semaine
print(toilette(20,40))