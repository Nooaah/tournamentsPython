import numpy as np
from random import *

def inscripNom(tab):
    nb_joueur = input('vous souhaitez entrer combien de joueurs (un nombre pair svp) ? ')
    if int(nb_joueur)%2 != 0:
        return inscription(tab)
    else:
        for i in range (0,int(nb_joueur)):
            nom=input("entrer le nom du joueur : ")
            tab.append(nom)
        return tab

def modifNom(tab):
    i=0
    msg="aucun joueur avec ce nom"
    nom=input("quel est le nom du joueur que vous souhaitez modifier ? ")
    trouve=0
    while (trouve==0 and i<len(tab)):
        if(tab[i]==nom):
            new=input("quel est son nouveau nom  ? ")
            tab[i]=new
            trouve=1
        i=i+1
    if trouve==0:
        return msg
    else:
        return tab
def suppNom(tab):
    i=0
    msg="aucun joueur avec ce nom"
    nom=input("quel est le nom du joueur que vous souhaitez supprimer ? ")
    trouve=0
    while (trouve==0 and i<len(tab)):
        if(tab[i]==nom):
            del tab[i]
            trouve=1
        i=i+1
    if trouve==0:
        return msg
    else:
        return tab

def matchs(mat):
    j=1
    for i in range(len(tab)):
        n = randint(1,len(tab))
        if j%2!=0:
            mat([0],[j])
            j=j+1
        else:
            mat([j],[0])
            j=j+1
    return mat

#Main
if __name__=="__main__":
    tab=[]
    mat=np.array([],[])
    print(inscripNom(tab))
    print(suppNom(tab))
    print(modifNom(tab))
    print(matchs(mat))
