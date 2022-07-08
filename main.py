from random import randrange
from math import ceil
user_money = 1000
print("=======================================BIENVENU DANS LE JEUX MCASINO🎉😂====================================\n")
#------------------------------------------Règle du jeux-------------------------------------
aide = str(input("Entrez H pour en savoir plus ou appuyez sur n'importe quoi pour commencer directement\t"))
if aide == "H" or aide == 'h':
    print("\tLe joueur mise sur un numéro compris entre 0 et 49 (50 numéros en tout). En choisissant son numéro, il y dépose la\nsomme qu'il souhaite miser.",
            "La roulette est constituée de 50 cases allant naturellement de 0 à 49. Les numéros pairs sont de couleur noire, les \nnuméros impairs sont de couleur rouge.",
            "Le croupier lance la roulette, lâche la bille et quand la roulette s'arrête, relève le numéro \nde la case dans laquelle la bille s'est arrêtée")
    print("\nLe numéro sur lequel s'est arrêtée la bille est, naturellement, le numéro gagnant.\n")
    print(" 1er cas---- Si le numéro gagnant est celui sur lequel le joueur a misé (probabilité de 1/50, plutôt faible), le croupier lui remet 3 fois la somme misée."
            ,"\n 2eme cas----Sinon, le croupier regarde si le numéro misé par le joueur est de la même couleur que le numéro gagnant \n\t\t(s'ils sont tous les deux pairs ou tous les deux impairs).",
            " Si c'est le cas, le croupier lui remet 50 % de la somme misée. ")
    print(" 3eme cas----Si ce n'est aucun de ces deux cas, le joueur perd sa mise.")
    print("\t\t---------------------------------START------------------------------\n")

#fonctions


def number():
    global i
    global number_user
    global n
    n = randrange(0, 49)
    a = 0
    while a == 0:
        number_user = input("\nVeuillez miser sur un numéro entre 0 et 49: ")
        #if the user doesn't put in a number:
        try:
            number_user = int(number_user)
            a = 1
            if number_user < 0 or number_user > 49:
                print("***SEULEMENT UN nombre entre 0 et 49")
                a = 0
        except:
            print("XXXXXXX----Veuillez saisir un nombre----XXXXXX")
    if number_user == n:
        i = 1
    elif (number_user % 2) == (n % 2):
        i = 2
    else:
        i = 0


def money(argent):
    print("\n\t\t***     Vous avez actuellement", user_money, "$     ***")
    global somme_mise
    a = 0
    while a == 0:
        somme_mise = input("\nCombien voulez vous miser:  ")
        try:
            somme_mise = int(somme_mise)
            a = 1
            if somme_mise < 0 or somme_mise > argent:
                print("***Misez correctement")
                a = 0
        except:
            print("XXXXXXX----Veuillez saisir un nombre----XXXXXX")

    print("Vous venez de miser", somme_mise, "$ sur le numéro ", number_user)


def gamble():
    global user_money
    number()
    money(user_money)
    print()
    print("Le numéro sur lequel s'est arrêtée la bille est {} ".format(n).center(80, '-'))
    if i == 1:
        user_money += somme_mise*3
        print("\t\t===Vous avez gagné ", somme_mise*3, "$ 🎉😂===")
        print("Votre somme en total est de", user_money, "$")
    elif i == 2:
        user_money += ceil(somme_mise/2)
        print("\t\t>>>Vous avez gagné ",ceil(somme_mise/2) , "$")
        print("Votre somme en total est de", user_money, "$")
    else:
        user_money -= somme_mise
        print("\t\t>>>Vous avez pedu, votre somme est maintenant de ", user_money, "$")
    if user_money <= 0:
        print("Vous n'avez plus assez d'argent pour miser\n\t\t ---Merci d'avoir jouer---")
    else:
        continuer = str(input("Entrez Q pour quitter avec votre somme actuelle, ou appuyez sur n'importe quoi pour continuer de miser"))
        if continuer == "Q" or continuer == "q":
            print("\t\t=====================MERCI D'AVOIR JOUER, vous partez avec une somme de", user_money, "$ ===================================")
        else:
             gamble()


#------------------------Commencement du jeux---------------------------
gamble()




