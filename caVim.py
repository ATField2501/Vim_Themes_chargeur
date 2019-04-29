#!/usr/bin/python3
# _*_ conding: utf8
#auteur:cagliostro <atfield2501@gmail.com

#### Script transformant le fichier de config de vim au niveau utilisateur pour changer de thème à la volée

import sys
import os

# Datas
chemin_vers_themes="~/Documents/Vim-Themes/"
chemin_vers_config="~/.vim/colors/caglioProfil.vim"

liste_themes=[]
commande=''


def detect():
    """
    Cette fonction à pour charge de detecter les themes présent dans le dossier conssacré
    """
    cible = os.popen('ls '+chemin_vers_themes)
    for e in cible.readlines():
        liste_themes.append(e)
    

def main(arg,liste_themes):
    """ Cette fonction détruit le lien symbolique présent dans le dossier de ressources colors pour en établire un nouveau en fonction de l'argument qui lui est transmit 
        le fichier .vimrc doit etre renseigné avec le nom du profil utiliser, ici caglioProfil
    """
    for i,e in enumerate(liste_themes):
        if arg == '-'+str(i+1):
            try:
                os.system('rm '+chemin_vers_config)
                e=e.rstrip('\n')
                commandefinal="ln -s ~/Documents/Vim-Themes/"+str(e)+" ~/.vim/colors/caglioProfil.vim"  
                os.system(commandefinal)
                print("Thème Vim changé pour {}".format(e))
            except Exception as e:
                print(e)

    if arg == '-h':
        print("* Transformant le thème de vim *")
        print("caVim -ls        - Affiche les thèmes présent")
        print("caVim -1         - Chargant le premier thème")

        
    if arg == '-ls':
        for i,e in enumerate(liste_themes):
            e=e.rstrip('\n')
            print(i+1,e)

detect()

try:
    os.system('ln -s ~/Documents/Vim-Themes/Tomorrow-Night.vim ~/.vim/colors/caglioProfil.vim >> /dev/null 2>&1')
except:
    pass

if len(sys.argv) == 1:
    arg= '-h'
    main(arg,liste_themes)
if len(sys.argv) == 2:
    arg=sys.argv[1]
    main(arg,liste_themes) 
