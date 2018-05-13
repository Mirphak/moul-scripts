# -*- coding: utf-8 -*-

from Plasma import *

"""
Voil�. Cela fonctionne parfaitement.
J'utilise un fichier Divers.ListeGUID qui reprend les GUID des �ges qui m'int�ressent. 
Tous mes �ges magiques commencent par MB et tous mes �ges du Tresor magique, par T

L'id�e est la suivante: 
Je regarde toutes les 15 secondes o� se trouve le bot.
S'il n'est pas dans un �ge magique, alors je l'envoie automatiquement vers MBCity.
Avec 15 secondes c'est suffisant car, 
si on envoie le bot dans un �ge interdit, 
il va juste avoir le temps d'a�rriver la mais va �tre directement renvoy� � MBCIty. 

Tu peux aussi essayer de r�duire ce temps, en fonction de la vitesse de ton PC.

La commande Sendbotto est une routine qui envoie le bot dans un �ge de GUID d�termin�. 
Tu poss�des certainement un �quivalent � cette routine.
"""

class SurveyBotAge:
    def __init__(self):
        self._idbot = 0
    def start(self,idbot=0):
        self._idbot = idbot
        self.onAlarm()
    def WhereIsBot(self): # verifie que le bot est bien dans un age magique inclu dans Divers.ListeGUID
        global verifplayers
        global cleanage
        tempNode = ptVaultPlayerInfoNode()
        tempNode.playerSetID(self._idbot)
        magicage = ""
        try:
            Info = ptVault().findNode(tempNode).upcastToPlayerInfoNode()
            if Info.playerIsOnline():
                ageGUID = Info.playerGetAgeGuid()
            else:
                ageGUID = ""
        except:
            ageGUID = ""
        if ageGUID != "":
            for cle, valeur in Divers.ListeGUID.items():
                if ageGUID == valeur[2] and cle.startswith('MB'):
                    return # le bot est bien dans un age magique
        #le bot n'est pas dans un age magique, on l'envoie a MBHood

        #le bot n'est pas dans un age magique. On le renvoie a MBCity
        PtSetAlarm (0,SendBotTo("MBCity",self._idbot),1)
    def onAlarm (self,param = 1):
        self.WhereIsBot()
        PtSetAlarm (15,self,1)# on verifie l'endroit ou le bot se trouve toutes les 15 secondes
SurveyBot = SurveyBotAge()
