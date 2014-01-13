from ex36_functions import *

nom_joueur = input("\nComment vous appelez-vous ?\n> ")
print("Bienvenue a vous, %s !\n" % nom_joueur)
print("Vous avez maintenant le choix entre trois portes :\n\
\tLa porte bleue, a gauche,\n\
\tLa porte rouge, a droite,\n\
\tLa porte verte, en face de vous.\n\nLaquelle choisissez-vous?")

choix_porte()
