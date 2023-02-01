import re
from hashlib import sha256

print('''------------------
Votre mot de passe doit contenir au moins 8 caractères, 
minimum une majuscule et une minuscule, minimum 1 chiffre
et au moins un caractère spécial
------------------''')

alerte = 0
mdp = input("Entrez un mot de passe valide: ")
if len(mdp) < 8:
    print("Le mot de passe n'est pas assez long")
    alerte = 1
if not re.search ('[A-Z]', mdp):
    print("Le mot de passe ne possède pas de majuscule")
    alerte = 1
if not re.search ('[a-z]', mdp):
    print("Le mot de passe ne possède pas de minuscule")
    alerte = 1
if not re.search ('[0-9]', mdp):
    print("Le mot de passe ne possède pas de chiffre")
    alerte = 1
if not re.search ('[!@#$%^&*+_]', mdp):
    print("Le mot de passe ne possède pas de symbole")
    alerte = 1

if (alerte == 0):
    print("Mot de passe valide")
    input_ = input('Votre mot de passe va être crypté. Appuyez sur entrée')
    print(sha256(input_.encode('utf-8')).hexdigest())
else:
    print("! Mot de passe invalide !")
