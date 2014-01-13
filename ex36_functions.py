from time import gmtime, strftime
from random import randrange
import os

epee = False
armure = False
magie = False
cle_1 = False
cle_2 = False

poison = False

ecouteurs = False
vampire = False

player_HP = 10
boss_HP = 10


def choix_porte():
	porte = input("> ")
	if "bleu" in porte:
		porte_bleue_intro()
	elif "rouge" in porte:
		porte_rouge_intro()
	elif "vert" in porte:
		porte_verte_intro()
	else:
		print("Merci d'etre plus clair. Quelle porte choisissez vous ?")
		choix_porte()
		
def porte_bleue_intro():
	print("\nPorte bleue. Bienvenue.")
	print("Vous entrez dans une petite salle, bien decoree, les murs sont tout bleus.")
	print("Un lapin tout moche, mais en costard, est assis a un bureau et lit son journal.\n")
	porte_bleue()

def porte_bleue():
	global ecouteurs
	global armure
	global epee
	print("Que voulez-vous faire ?")
	print("\t1. Lui mettre un coup de pied.")
	print("\t2. Crier pour lui faire peur.")
	print("\t3. Lui demander l'heure.")
	if ecouteurs == True:
		print("\t4. Lui demander gentiment d'enlever ses ecouteurs.")
	if ecouteurs == False and epee == True:
		print("\t4. Le menacer avec votre epee.")
	if ecouteurs == True and epee == True:
		print("\t5. Le menacer avec votre epee.")
	rep_bleue = input("\n> ")
	if rep_bleue == "1" or "pied" in rep_bleue.lower():
		print("\nLe lapin tout moche vous mord la jambe, et vous mourrez a cause du poison dans ses dents. Game over !")
		os.system("pause")
		quit()
	elif (rep_bleue == "2" or "crier" in rep_bleue.lower()) and ecouteurs == False:
		print("\nLe lapin met des ecouteurs pour masquer le bruit que vous faites.\n")
		ecouteurs = True
		porte_bleue()
	elif (rep_bleue == "2" or "crier" in rep_bleue.lower()) and ecouteurs == True:
		print("\nLe lapin ne vous entend pas car il est en train d'ecouter Rain Over Me, de Pitbull, son idole...\n")
		porte_bleue()
	elif (rep_bleue == "3" or "heure" in rep_bleue.lower()) and ecouteurs == False:
		print("\nLe lapin vous indique qu'il est", strftime("%H:%M"), "et sort un coffre de son bureau...")
		print("Il vous demande d'ouvrir le coffre...\n")
		print("Voulez-vous ouvrir le coffre ?\n")
		coffre_bleu = input("> ")
		if coffre_bleu.lower() == "oui" or "ouvr" in coffre_bleu.lower():
			print("\nFelicitations, vous venez d'obtenir l'armure magique du lapin tout moche !\n")
			armure = True
		else:
			print("\nTant pis, pas de cadeau pour vous...\n")
		print("Le lapin devoile une porte derobee, au fond de la salle...\n")
		porte_violette()
	elif (rep_bleue == "3" or "heure" in rep_bleue.lower()) and ecouteurs == True:
		print("\nLe lapin ne vous entend pas et fait caca partout dans la salle...\n")
		porte_bleue()
	elif (rep_bleue == "4" or "enleve" in rep_bleue.lower()) and ecouteurs == True:
		print("\nVous demandez au lapin d'enlever ses ecouteurs. Il les enleve apres avoir fini sa chanson de Pitbull, Rain Over Me...\n")
		ecouteurs = False
		porte_bleue()
	elif (rep_bleue == "4" or rep_bleue == "5" or "epee" in rep_bleue.lower()) and epee == True:
		print("\nLe lapin prend peur et s'enfuit en laissant un coffre derriere lui...\n")
		print("Voulez-vous ouvrir le coffre ?")
		coffre_bleu = input("> ")
		if coffre_bleu.lower() == "oui" or "ouvr" in coffre_bleu.lower():
			print("Felicitations, vous venez d'obtenir l'armure magique du lapin tout moche !")
			armure = True
		else:
			print("Tant pis, pas de cadeau pour vous...")
		print("Vous decouvrez une porte derobee, au fond de la salle...\n")
		porte_violette()
		
	else:
		print("\nMerci d'etre plus clair sur ce que vous voulez faire...\n")
		porte_bleue()
		
def porte_rouge_intro():
	print("\nPorte rouge. Bienvenue.")
	print("Vous arrivez dans une salle rouge, entierement vide.\n")
	porte_rouge()

def porte_rouge():
	global poison
	global vampire
	global magie
	print("Que faites-vous ?")
	print("\t1. Vous commencez a pisser sur les murs pour voir ce qu'il se passe.")
	print("\t2. Vous faites une sieste.")
	if vampire == False:
		print("\t3. Vous levez les yeux vers le plafond.")
	if vampire == True:
		print("\t3. Vous demandez au vampire s'il peut se nourir d'autre chose que de sang.")
	rep_rouge = input("> ")
	if (rep_rouge == "1" or ("pisse" or "mur") in rep_rouge) and vampire == False:
		print("\nVous ne pouvez plus vous arreter de pisser, et vous finissez noye dans votre pisse. Game over !")
		os.system("pause")
		quit()
	elif (rep_rouge == "1" or ("pisse" or "mur") in rep_rouge) and vampire == True:
		print("\nLe vampire vous mord aux parties genitales et un etrange pouvoir s'empare de vous...")
		print("Vous avez recupere un pouvoir magique !\n")
		magie = True
		print("Vos nouveaux pouvoirs vous permettent de voir une porte orange, cachee au fond de la salle.\n")
		porte_orange()
	elif (rep_rouge == "2" or "sieste" in rep_rouge) and vampire == True:
		print("\nLe vampire vous reveille des que vous commencez a vous endormir. Un vrai nazi...\n")
		porte_rouge()
	elif (rep_rouge == "2" or "sieste" in rep_rouge) and poison == False:
		print("\nPendant que vous dormez, un scorpion noir de trois metres vient vous piquer.\n")
		poison = True
		porte_rouge()
	elif (rep_rouge == "2" or "sieste" in rep_rouge) and poison == True:
		print("\nVous n'arrivez plus a dormir.\n")
		porte_rouge()
	elif (rep_rouge == "3" or "plafond" in rep_rouge) and vampire == False:
		print("\nVous remarquez qu'un vampire dort colle au plafond. Il se reveille et vous rejoint au sol.\n")
		vampire = True
		porte_rouge()
	elif (rep_rouge == "3" or "sang" in rep_rouge) and vampire == True:
		print("\nLe vampire vous repond qu'il aime aussi le tofu. Pour vous remercier de votre gentillesse, il vous\
mord aux parties genitales...")
		print("Vous avez recupere un pouvoir magique !\n")
		magie = True
		print("Vos nouveaux pouvoirs vous permettent de voir une porte orange, cachee au fond de la salle.\n")
		porte_orange()
	else:
		print("Merci d'etre plus clair...\n")
		porte_rouge()

def porte_verte_intro():
	print("\nPorte verte. Bienvenue.")
	print("La salle est remplie de plantes vertes.")
	print("Un coffre est pose au milieu de la salle.")
	print("Vous apercevez un ecriteau a cote...\n")
	porte_verte()	
	
def porte_verte():
	global epee
	print("Que faites vous ?")
	print("\t1. Vous lisez ce qui est ecrit sur l'ecriteau.")
	print("\t2. Vous mettez un coup de pied dans le coffre pour l'ouvrir.")
	print("\t3. Vous attendez le deluge.")
	rep_verte = input("> ")
	if rep_verte == "1" or "ecriteau" in rep_verte:
		print("\nIl est dit que seul celui qui connait la chanson peut ouvrir le coffre.")
		print("Voulez-vous essayer de chanter ?\n")
		rep_chanson = input("> ")
		if rep_chanson == "oui":
			i = 0
			chanson = "TADADADAAA!"
			while i < 3:
				print("\nMerci d'ecrire les paroles.")
				chanson_test = input("> ")
				i += 1
				if chanson_test == chanson:
					print("\nWHAOU ! Vous avez devine la chanson et l'avez chante avec brio ! Le coffre se met a applaudir !")
					print("Bravo ! Vous avez reussi a ouvrir le coffre ! A l'interieur se trouve une epee !\n")
					print("Voulez-vous la prendre ?\n")
					rep_epee = input("> ")
					if rep_epee.lower() == "oui":
						epee = True
						if cle_2 == True:
							print("\nVous rebroussez chemin arme de votre epee et vous vous dirigez vers la porte rouge.\n")
							porte_rouge_intro()
							break
						elif cle_1 == True:
							print("\nVous rebroussez chemin arme de votre epee et vous vous dirigez vers la porte bleue.\n")
							porte_bleue_intro()
							break
						else:
							print("\nVous rebroussez chemin arme de votre epee et avez maintenant le choix entre la porte bleue ou la porte rouge.\n")
							print("Laquelle choisissez-vous ?")
							porte = input("> ")
							if "rouge" in porte:
								porte_rouge_intro()
								break
							elif "bleu" in porte:
								porte_bleue_intro()
								break
							else:
								print("\nDevant votre incapacite a ecrire correctement une couleur, le coffre prend vie et vous mange. Game over !")
								os.system("pause")
								quit()
					elif rep_epee.lower() == "non":
						epee = False
						if cle_2 == True:
							print("\nVous rebroussez chemin et vous vous dirigez vers la porte rouge.\n")
							porte_rouge_intro()
							break
						elif cle_1 == True:
							print("\nVous rebroussez chemin et vous vous dirigez vers la porte bleue.\n")
							porte_bleue_intro()
							break
						else:
							print("\nVous rebroussez chemin et avez maintenant le choix entre la porte bleue ou la porte rouge.\n")
							print("Laquelle choisissez-vous ?")
							porte = input("> ")
							if "rouge" in porte:
								porte_rouge_intro()
								break
							elif "bleu" in porte:
								porte_bleue_intro()
								break
							else:
								print("\nDevant votre incapacite a ecrire correctement une couleur, le coffre prend vie et vous mange. Game over !")
								os.system("pause")
								quit()
				elif "tada" in chanson_test.lower():
					print("\nBravo ! Vous avez reussi a ouvrir le coffre ! A l'interieur se trouve une epee !")
					print("Voulez-vous la prendre ?\n")
					rep_epee = input("> ")
					if rep_epee.lower() == "oui":
						epee = True
						if cle_2 == True:
							print("\nVous rebroussez chemin arme de votre epee et vous vous dirigez vers la porte rouge.\n")
							porte_rouge_intro()
							break
						elif cle_1 == True:
							print("\nVous rebroussez chemin arme de votre epee et vous vous dirigez vers la porte bleue.\n")
							porte_bleue_intro()
							break
						else:
							print("\nVous rebroussez chemin et avez maintenant le choix entre la porte bleue ou la porte rouge.\n")
							print("Laquelle choisissez-vous ?")
							porte = input("> ")
							if "rouge" in porte:
								porte_rouge_intro()
								break
							elif "bleu" in porte:
								porte_bleue_intro()
								break
							else:
								print("\nDevant votre incapacite a ecrire correctement une couleur, le coffre prend vie et vous mange. Game over !")
								os.system("pause")
								quit()
					elif rep_epee.lower() == "non":
						epee = False
						if cle_2 == True:
							print("\nVous rebroussez chemin et vous vous dirigez vers la porte rouge.\n")
							porte_rouge_intro()
							break
						elif cle_1 == True:
							print("\nVous rebroussez chemin et vous vous dirigez vers la porte bleue.\n")
							porte_bleue_intro()
							break
						else:
							print("\nVous rebroussez chemin et avez maintenant le choix entre la porte bleue ou la porte rouge.\n")
							print("Laquelle choisissez-vous ?")
							porte = input("> ")
							if "rouge" in porte:
								porte_rouge_intro()
								break
							elif "bleu" in porte:
								porte_bleue_intro()
								break
							else:
								print("\nDevant votre incapacite a ecrire correctement une couleur, le coffre prend vie et vous mange. Game over !")
								os.system("pause")
								quit()
				elif "ding ding dong" in chanson_test.lower():
					print("\nPetit coquin... Mais non, ce n'est pas ca...\n")
				else:
					print("\nNon c'est pas ca...\n")
			if i >= 3:
				print("\nVous commencez a ennuyer le coffre qui, baillant, devoile son contenu...")
				print("Vous y decouvrez une epee !")
				print("Voulez-vous la prendre ?\n")
				rep_epee = input("> ")
				if rep_epee.lower() == "oui":
					epee = True
					if cle_2 == True:
						print("\nVous rebroussez chemin arme de votre epee et vous vous dirigez vers la porte rouge.\n")
						porte_rouge_intro()
					elif cle_1 == True:
						print("\nVous rebroussez chemin arme de votre epee et vous vous dirigez vers la porte bleue.\n")
						porte_bleue_intro()
					else:
						print("\nVous rebroussez chemin et avez maintenant le choix entre la porte bleue ou la porte rouge.\n")
						print("Laquelle choisissez-vous ?")
						porte = input("> ")
						if "rouge" in porte:
							porte_rouge_intro()
						elif "bleu" in porte:
							porte_bleue_intro()
						else:
							print("\nDevant votre incapacite a ecrire correctement une couleur, le coffre prend vie et vous mange. Game over !")
							os.system("pause")
							quit()
				elif rep_epee.lower() == "non":
					epee = False
					if cle_2 == True:
						print("\nVous rebroussez chemin et vous vous dirigez vers la porte rouge.\n")
						porte_rouge_intro()
					elif cle_1 == True:
						print("\nVous rebroussez chemin et vous vous dirigez vers la porte bleue.\n")
						porte_bleue_intro()
					else:
						print("\nVous rebroussez chemin et avez maintenant le choix entre la porte bleue ou la porte rouge.\n")
						print("Laquelle choisissez-vous ?")
						porte = input("> ")
						if "rouge" in porte:
							porte_rouge_intro()
						elif "bleu" in porte:
							porte_bleue_intro()
						else:
							print("\nDevant votre incapacite a ecrire correctement une couleur, le coffre prend vie et vous mange. Game over !")
							os.system("pause")
							quit()
		elif rep_chanson == "non":
			print("\nQuel individu sinistre vous etes...\n")
			porte_verte()
		else:
			print("\nMerci de repondre par oui ou par non...\n")
			porte_verte()
	if rep_verte == "2" or ("frapper" or "coup" or "pied") in rep_verte:
		print("\nLa violence de votre coup vous a litteralement dechire la jambe. Vous perdez trop de sang et mourrez. Game over !")
		os.system("pause")
		quit()
	if rep_verte == "3" or ("attend" or "deluge") in rep_verte:
		print("\nUne tempete d'une violente inouie devaste tout dans la salle et vous dechire en petits morceaux. Game over !")
		os.system("pause")
		quit()
	else:
		print("\nMerci d'etre plus clair...\n")
		porte_verte()

def porte_violette():
	global cle_2
	print("\nPorte violette. Bienvenue.\n")
	print("Vous devrez resoudre un puzzle pour passer la salle suivante. C'est parti !")
	print("Essayez de dechiffrer le message code !")
	nb_chances_violette = randrange(1,10)
	print("\nVous avez %s chances pour y arriver.\n" %nb_chances_violette)
	message_code = ["que", "la", "force", "soit", "avec", "toi"]
	print(sorted(message_code))
	i = 0
	while i < nb_chances_violette:
		i += 1
		rep_violette = input("> ")
		if rep_violette.lower() == " ".join(message_code):
			print("\nBravo, c'est la bonne reponse !")
			print("Une cle tombe du plafond et se glisse dans votre poche.\n")
			cle_2 = True
			print("Vous vous dirigez vers l'antre du demon...\n")
			porte_boss()
			break
		else:
			print("\nNon, ce n'est pas ca... Il vous reste", nb_chances_violette - i, "chance(s).\n")
	if cle_2 != True:
		print("\nMalheureusement, vous n'avez pas trouve le message code... Une corde tombe du plafond et vous vous pendez. Game over !")
		os.system("pause")
		quit()

def porte_orange():
	global cle_1
	print("\nPorte orange. Bienvenue.\n")
	print("Vous devrez resoudre un puzzle pour passer la salle suivante. C'est parti !")
	message_code = "You touched my ding ding dong"
	message_masque = "Upi ypivjrf ,u fomh fomh fpmh"
	for lettre in message_masque:
		print("\t\t",lettre)
	print("Votre objectif est de dechiffrer cette incantation !\n")
	nb_chances_violette = randrange(5,11)
	print("\nVous avez %s chances pour y arriver.\n" %nb_chances_violette)
	i = 0
	while i < nb_chances_violette:
		i += 1
		if i < 4:
			print("Votre reponse :")
			rep_orange = input("> ")
			if rep_orange.lower() == message_code.lower():
				print("Ding Dong, it's a Christmas Song! Une cle magique tombe directement dans votre poche.\n")
				cle_1 = True
				print("Vous vous dirigez vers l'antre du demon...\n")
				porte_boss()
				break
			else:
				print("\nNon, c'est pas ca...\n")
		elif i < 5:
			print("\nIndice 1 : C'est de l'anglais...")
			print("Votre reponse :")
			rep_orange = input("> ")
			if rep_orange.lower() == message_code.lower():
				print("Ding Dong, it's a Christmas Song! Une cle magique tombe directement dans votre poche.\n")
				cle_1 = True
				print("Vous vous dirigez vers l'antre du demon...\n")
				porte_boss()
				break
			else:
				print("\nNon, c'est pas ca...\n")
		elif i < 6:
			print("\nIndice 2 : Incantation psalmodiee en anglais par l'homme a moustache le plus classe depuis Freddie Mercury.")
			print("Votre reponse :")
			rep_orange = input("> ")
			if rep_orange.lower() == message_code.lower():
				print("Ding Dong, it's a Christmas Song! Une cle magique tombe directement dans votre poche.\n")
				cle_1 = True
				print("Vous vous dirigez vers l'antre du demon...\n")
				porte_boss()
				break
			else:
				print("\nNon, c'est pas ca...\n")
		elif i < 7:
			print("\nIndice 3 : Le troisieme indice vous sera donne si vous ne trouvez pas par vous-meme cette fois-ci.")
			print("Votre reponse :")
			rep_orange = input("> ")
			if rep_orange.lower() == message_code.lower():
				print("Ding Dong, it's a Christmas Song! Une cle magique tombe directement dans votre poche.\n")
				cle_1 = True
				print("Vous vous dirigez vers l'antre du demon...\n")
				porte_boss()
				break
			else:
				print("\nIt's a no-no. And you like it!\n")
		elif i < 8:
			print("\nIndice 4 : Bon, vous etes vraiment nul. L'auteur de cette incantation est Gunther.")
			print("Votre reponse :")
			rep_orange = input("> ")
			if rep_orange.lower() == message_code.lower():
				print("Ding Dong, it's a Christmas Song! Une cle magique tombe directement dans votre poche.\n")
				cle_1 = True
				print("Vous vous dirigez vers l'antre du demon...\n")
				porte_boss()
				break
			else:
				print("\nIt's a no-no. And you like it!\n")
		elif i < 9:
			print("\nIndice 5 : Dernier indice. Essayez de decaler d'une lettre sur votre clavier l'incantation...")
			print("Votre reponse :")
			rep_orange = input("> ")
			if rep_orange.lower() == message_code.lower():
				print("Ding Dong, it's a Christmas Song! Une cle magique tombe directement dans votre poche.\n")
				cle_1 = True
				print("Vous vous dirigez vers l'antre du demon...\n")
				porte_boss()
				break
			else:
				print("\nIt's a no-no. And you like it!\n")
	if cle_1 != True:
		print("\nUn ours apparait et vous demande si vous voulez du miel.\n")
		rep_ours = input("> ")
		print("\nL'ours vous arrache la tete d'un coup de patte. Game over !")
		os.system("pause")
		quit()

def porte_boss():
	if cle_1 == True and cle_2 == True:
		print("\nVous arrivez chez le maitre des lieux...")
		print("Il s'agit de la derniere partie du jeu...")
		print("Voici votre equipement et votre statut :")
		if epee == True:
			print("\tEpee")
		if armure == True:
			print("\tArmure")
		if magie == True:
			print("\tMagie")
		if poison == True:
			print("\tPar ailleurs, vous etes empoisonne, il ne vous reste plus longtemps a vivre et vous commencez a voir des penis de partout...")
		if poison == False:
			print("\tVous etes en pleine forme.")
		combat_boss()		
	elif cle_1 == True and cle_2 == False:
		print("\nIl vous manque une cle, vous devez rebrousser chemin...\n")
		if epee == False:
			print("Voulez vous choisir la porte verte ou la porte bleue ?")
			choix_porte = input("> ")
			if "vert" in choix_porte:
				porte_verte_intro()
			elif "bleu" in choix_porte:
				porte_bleue_intro()
			else:
				print("\nDevant votre incapacite a ecrire correctement une couleur, le plafond s'ecroule et vous ecrase. Game over !")
				os.system("pause")
				quit()
		else:
			print("\nVous vous rebroussez chemin et vous dirigez vers la porte bleue.\n")
			porte_bleue_intro()
	else:
		print("\nIl vous manque une cle, vous devez rebrousser chemin...\n")
		if epee == False:
			print("Voulez vous choisir la porte verte ou la porte rouge ?")
			choix_porte = input("> ")
			if "vert" in choix_porte:
				porte_verte_intro()
			elif "rouge" in choix_porte:
				porte_rouge_intro()
			else:
				print("\nDevant votre incapacite a ecrire correctement une couleur, le plafond s'ecroule et vous ecrase. Game over !")
				os.system("pause")
				quit()
		else:
			print("\nVous vous rebroussez chemin et vous dirigez vers la porte rouge.\n")
			porte_rouge_intro()

def combat_boss():
	global player_HP
	global boss_HP
	prompt = "> "
	prompt_poison = "8===> "
	epee_dmg = 2
	magie_dmg = 3
	armure_dmg = -1
	poison_dmg = 1
	attaque = ""
	boss_epee = 2
	boss_magie = 3
	attaque_boss = 0
	
	print("\nVous voila maintenant face au demon... Qui n'est autre que Justin Bieber.")
	print("Tentez de le terrasser avec votre force !\n")
	while boss_HP > 0 and player_HP > 0:
			print("Il vous reste", player_HP, "point(s) de vie.")	
			print("Que voulez-vous faire ?")
			print("\t1. Utiliser votre magie ?")
			if epee == True:
				print("\t2. Lui mettre un coup d'epee ?")
			if poison == True:
				attaque = input(prompt_poison)
			elif poison == False:
				attaque = input(prompt)
			if attaque == "1" or "magie" in attaque:
				print("\nVous lancez un rayon magique tout droit sorti de votre entrejambe qui va s'ecraser sur le visage de Justin Bieber !\n")
				boss_HP -= magie_dmg
				if boss_HP > 0:
					print("J.B. a encore", boss_HP, "point(s) de vie.")
				elif boss_HP <= 0:
					break
			elif (attaque == "2" or "epee" in attaque) and epee == True:
				print("\nVous donnez un grand coup d'epee a Justin Bieber qui lance un cri de douleur, et vous aimez ca.\n")
				boss_HP -= epee_dmg
				if boss_HP > 0:
					print("J.B. a encore", boss_HP, "point(s) de vie.")
				elif boss_HP <= 0:
					break
			else:
				print("\nVous n'avez pas ete assez clair, vous perdez un tour...\n")
				print("J.B. a encore", boss_HP, "point(s) de vie.")
			print("\nC'est au tour de Justin Bieber de vous attaquer.\n")
			attaque_boss = randrange(1, 3)
			if attaque_boss == 1:
				print("\nJustin Bieber vous met un coup de son epee rose en caoutchouc !\n")
				player_HP -= boss_epee
				if armure == True:
					player_HP -= armure_dmg
					print("Votre armure vous protege un peu")
				if poison == True:
					player_HP -= poison_dmg
					print("Vous etes toujours empoisone, vous perdez un peu plus de vie...")			
			elif attaque_boss == 2:
				print("\nJustin Bieber vous chante une chanson. Attaque violente !\n")
				player_HP -= boss_magie
				if armure == True:
					player_HP -= armure_dmg
					print("Votre armure vous protege un peu")
				if poison == True:
					player_HP -= poison_dmg
					print("Vous etes toujours empoisone, vous perdez un peu plus de vie...")
	if boss_HP <= 0:
		print("Bravo ! Vous avez battu le boss ! Vous voila maintenant libre ! Vous pouvez sortir du donjon. VICTOIRE !")
		os.system("pause")
		quit()
	elif player_HP <= 0:
		print("Quel dommage, et quelle honte surtout ! Vous avez ete battu par Justin Bieber... Il vous chante une autre chanson\
pour vous accompagner dans l'autre monde. GAME OVER !")
		os.system("pause")
		quit()
