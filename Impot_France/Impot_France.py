"""


Code by Orbital-Builder.
Aide : Github Copilot.
Aide : UDEMY - Jean-Philippe Parein. 
Version 1.0.


"""

print("Calcul de l'impôt sur le revenu 2025")
print("-------------------------------")

while True:
    salaire_net = input("Salaire total net? (annuel) ")
    try:
        salaire_net = float(salaire_net)
        
        revenu_imposable = salaire_net
        impots = 0

        # Barem de l'imposition 2025
        if revenu_imposable > 180294:
            impots += (revenu_imposable - 180294) * 0.45
            revenu_imposable = 180294
        if revenu_imposable > 83823:
            impots += (revenu_imposable - 83823) * 0.41
            revenu_imposable = 83823
        if revenu_imposable > 29315:
            impots += (revenu_imposable - 29315) * 0.30
            revenu_imposable = 29315
        if revenu_imposable > 11497:
            impots += (revenu_imposable - 11497) * 0.11

        salaire_net_apres_impot = salaire_net - impots
        impots = round(impots, 2)   
        salaire_net_apres_impot = round(salaire_net_apres_impot, 2)
    except ValueError:
        print("Merci de rentrer une valeur numérique")
    except ZeroDivisionError:
        print("Division par zéro non autorisée")
    else:
        print("____________________________________________")
        print(f"Vous allez payer un total de {impots}€ d'impôt sur le revenu en 2025")
        print("____________________________________________")
        print(f"Le salaire net après impôt est de {salaire_net_apres_impot}€")

    continuer = input("Voulez-vous faire un autre calcul ? (o/n) ").strip().lower()
    if continuer != 'o':
        break