#
# X Jalon 1 : rechercher les arrêts selon une recherche
# X Jalon 2 : rechercher les terminus
# X Jalon 3 : rechercher les correspondances
# X Jalon 4 : rechercher si le départ et l'arrivée sont sur la même ligne
# X Jalon 5 : rechercher le ou les correspondance si le trajet test sur des lignes différentes
# X Jalon 6 : trajet sur la même ligne déterminer le sens depuis le départ 
# Jalon 7 : trajet sur ligne différentes déterminer le sens depuis le départ, vers l'arrêt de correspondance 
# X Jalon 8 : trajet sur même ligne, comptabiliser le nombre d'arrêts
# Jalon 9 : trajet sur lignes différentes, comptabiliser le nombre d'arrêts
# jalon 10 : Trajet sur des lignes différentes, comptabiliser le nombre de correspondances

import re

def rechercheArret(_lignes, _nomLignes, _arret):
  response = []
  numeroLigne = 0
  while numeroLigne < len(_lignes):
    numeroArret = 0
    while numeroArret < len(_lignes[numeroLigne]):
      if _lignes[numeroLigne][numeroArret] == _arret:
        response.append(_nomLignes[numeroLigne])
      numeroArret += 1
    numeroLigne += 1
  return response

def rechercheLigneCommun(_lignesDepart, _lignesArrivees):
  response = []
  i = 0
  while i < len(_lignesDepart):
    j = 0
    while j < len(_lignesArrivees):
      if _lignesDepart[i] == _lignesArrivees[j]:
        print("La ligne "+_lignesDepart[i] + " est une ligne en commun")
        response.append(_lignesDepart[i])
      j +=1
    i += 1
  return response

def rechercheIndexLigneCommun(_ligneCommun, _nomLigne):
  response = []
  i = 0
  while i < len(_nomLigne):
    if _ligneCommun[0] == _nomLigne[i]:
      response.append(i)
    i += 1
  return response

def rechercheTerminus(_indexLigneCommun, _depart, _arrivee, _listeLigne):
  ligne = _listeLigne[_indexLigneCommun[0]]
  i = 0
  indexDepart = ligne.index(_depart)
  indexArrivee = ligne.index(_arrivee)
  if indexDepart < indexArrivee :
    terminus = ligne[-1]
    indexActuel = indexDepart
    while indexArrivee > indexActuel:
      print("Arrêt : "+ligne[indexActuel+1])
      i+=1
      indexActuel += 1
  else:
    terminus = ligne[0]
    indexActuel = indexDepart
    while indexArrivee < indexActuel:
      print("Arrêt : "+ligne[indexActuel-1])
      indexActuel -= 1
      i+=1

  print("Terminus : "+terminus)
  print("Il y a ",i,"arrêt(s) sur votre parcours")

def rechercheIndex(_nomLigne, _arret):
  listeIndexLigne = []
  i = 0
  
  while i < len(_nomLigne):
    y = 0
    while y < len(_arret):
      if _nomLigne[i] == _arret[y]:
        listeIndexLigne.append(i)
      y += 1
    i += 1
  return listeIndexLigne

def nombreArret(_ligne, _depart, _arrivee, _listeLigne):
  ligne = _listeLigne[_ligne]
  i = 0
  indexDepart = ligne.index(_depart)
  indexArrivee = ligne.index(_arrivee)
  arret = []
  if indexDepart < indexArrivee :
    indexActuel = indexDepart
    while indexArrivee > indexActuel:
      arret.append(ligne[indexActuel+1])
      i+=1
      indexActuel += 1
  else:
    indexActuel = indexDepart
    while indexArrivee < indexActuel:
      arret.append(ligne[indexActuel-1])
      indexActuel -= 1
      i+=1
  return arret

def Terminus(_ligne, _depart, _arrivee, _listeLigne, _nomLigne):
  i = 0
  ligne = _listeLigne[_ligne]
  indexDepart = rechercheIndex(_nomLigne, _depart)
  indexArrivee = rechercheIndex(_nomLigne, _arrivee)
  if indexDepart < indexArrivee :
    terminus = ligne[-1]
  else:
    terminus = ligne[0]
  return terminus

def rechercheArretCorrespondance(_arret, _correspondance, _listeLigne, _nomLigne):
  correspondanceArret = []
  listeIndexLigne = rechercheIndex(_nomLigne, _arret)
  for indexLigne in listeIndexLigne:
    for arretLigne in _listeLigne[indexLigne]:
      for arretCorrespondance in _correspondance:
          if arretLigne == arretCorrespondance:
            if not arretLigne in correspondanceArret:
              correspondanceArret.append(arretLigne)
  return correspondanceArret

def rechercheTerminusCorrespondance(_correspondance, _listeLigne, _nomLigne, _depart, _arrivee, _listeLignesDepart, _listeLignesArrivee):
  listeLigneDepart = rechercheIndex(_nomLigne, _listeLignesDepart)
  listeLigneArrivee = rechercheIndex(_nomLigne, _listeLignesArrivee)
  listeArretDepartCorrespondance = []
  listeArretArriveeCorrespondance = []
  listefinalArret = []
  listeTerminusDepart = []
  listeTerminusArrivee = []
  terminusDepart = []
  terminusArrivee = []
  resultat = []
  i = 0
  while i < len(listeLigneDepart):
    for unitcorrespondance in _correspondance:
      if unitcorrespondance in _listeLigne[listeLigneDepart[i]]:
        listeArretDepartCorrespondance.append(nombreArret(listeLigneDepart[i], _depart, unitcorrespondance, _listeLigne))
        listeTerminusDepart.append(Terminus(listeLigneDepart[i], _depart, unitcorrespondance, _listeLigne, _nomLigne))
    i += 1
  print("Le terminus",listeTerminusDepart)
  i = 0
  while i < len(listeLigneArrivee):
    for unitcorrespondance in _correspondance:
      if unitcorrespondance in _listeLigne[listeLigneArrivee[i]]:
        listeArretArriveeCorrespondance.append(nombreArret(listeLigneArrivee[i], unitcorrespondance, _arrivee, _listeLigne))
        listeTerminusArrivee.append(Terminus(listeLigneArrivee[i], unitcorrespondance, _arrivee, _listeLigne, _nomLigne))
    i += 1

  i = 0
  while i < len(listeArretArriveeCorrespondance):
    resultat = [*listeArretDepartCorrespondance[i], *listeArretArriveeCorrespondance[i]]
    listefinalArret.append(resultat)
    i+=1

  i = 0
  y = 0
  listefinalArretOpti = []
  while i < len(listefinalArret):
    if len(listefinalArretOpti) == 0:
      listefinalArretOpti = listefinalArret[i]
      terminusDepart = listeTerminusDepart[i]
      terminusArrivee = listeTerminusArrivee[i]
      y=i
    if len(listefinalArretOpti) > len(listefinalArret[i]):
      listefinalArretOpti = listefinalArret[i]
      terminusDepart = listeTerminusDepart[i]
      terminusArrivee = listeTerminusArrivee[i]
      y=i
    i += 1
  i = 1

  ligneDepart = ligneParTerminus(terminusDepart, NomLigne, ListeLigne)
  ligneArrivee = ligneParTerminus(terminusArrivee, NomLigne, ListeLigne)
  print("Prenez le",ligneDepart,"direction",terminusDepart)
  for arret in listefinalArretOpti:
    if arret == _correspondance[y] :
      print('Correspondance : Prenez ensuite',ligneArrivee,'direction', terminusArrivee)
    print("Arrêt n°",i,":",arret)
    i+=1
  
  
  return

def ligneParTerminus(_terminus, _nomLigne, _listeLigne):
  i= 0 
  ligneResponse = []
  for ligne in _listeLigne:
    if _terminus in ligne:

      indexTerminus = ligne.index(_terminus)
      if indexTerminus == -1 or indexTerminus == 0:
        ligneResponse = _nomLigne[i]

    i +=1
  return ligneResponse

TronconPrincipalTramA = [
  "Le Haillan Rostand",
  "Les Pins",
  "Frères Robinson",
  "Hôtel de Ville Mérignac",
  "Pin Galant",
  "Mérignac Centre",
  "Lycées de Mérignac",
  "Quatre Chemins",
  "Pierre Mendès-France",
  "Alfred de Vigny",
  "Fontaine d'Arlac",
  "Peychotte",
  "François Mitterrand",
  "Saint-Augustin",
  "Hôpital Pellegrin",
  "Stade Chaban-Delmas",
  "Gaviniès",
  "Hôtel de Police",
  "Saint-Bruno - Hôtel de Région",
  "Mériadeck",
  "Palais de Justice",
  "Hôtel de Ville",
  "Sainte-Catherine",
  "Place du Palais",
  "Porte de Bourgogne",
  "Stalingrad",
  "Jardin botanique",
  "Thiers - Benauge",
  "Galin",
  "Jean Jaurès",
  "Cenon Gare",
  "Carnot - Mairie de Cenon",
  "Buttinière",
]

TronconPrincipalTramB = [
  "Berges de la Garonne",
  "Claveau",
  "Brandenburg",
  "New-York",
  "Rue Achard",
  "Bassins à Flot",
  "Les Hangars",
  "Cours du Médoc",
  "Chartrons",
  "CAPC (Musée d'Art Contemporain)",
  "Quinconces",
  "Grand Théâtre",
  "Gambetta",
  "Hôtel de Ville",
  "Musée d'Aquitaine", "Victoire", "Saint-Nicolas",
  "Bergonié",
  "Barrière Saint-Genès",
  "Roustaing",
  "Forum",
  "Peixotto",
  "Béthanie",
  "Arts et Métiers",
  "François Bordes",
  "Doyen Brus",
  "Montaigne-Montesquieu",
  "UNITEC",
  "Saige",
  "Bougnard",
]

TronconPrincipalTramC = [
  "Parc des Expositions",
  "Palais des Congrès",
  "Quarante Journaux",
  "Berges du lac",
  "Les Aubiers",
  "Place Ravezies-Le Bouscat",
  "Grand Parc",
  "Émile Counord",
  "Camille Godard",
  "Place Paul Doumer",
  "Jardin Public",
  "Quinconces",
  "Place de la Bourse",
  "Porte de Bourgogne",
  "Saint-Michel",
  "Sainte-Croix",
  "Tauzia",
  "Gare Saint-Jean",
  "Belcier",
  "Carle Vernet",
  "Bègles Terres Neuves",
  "La Belle Rose",
  "Stade Musard",
  "Calais – Centujean",
  "Gare de Bègles",
  "Parc de Mussonville",
  "Lycée Vaclav Havel"
]

TronconPrincipalTramD = [
  "Quinconces",
  "Charles Gruet",
  "Marie Brizard",
  "Barrière du Médoc",
  "Courbet",
  "Calypso",
  "Mairie du Bouscat",
  "Les Ecus",
  "Sainte-Germaine",
  "Hippodrome",
  "Le Sulky",
  "Toulouse Lautrec",
  "Picot",
  "Eysines Centre",
  "Les Sources",
  "Cantinolle"
]
NomLigne = ["TramA","TramB","TramC","TramD"]

ListeLigne = [TronconPrincipalTramA, TronconPrincipalTramB,TronconPrincipalTramC,TronconPrincipalTramD]

Correspondance = ["Quinconces", "Hôtel de Ville", "Porte de Bourgogne"]


# Recherche départ dans une ligne 
depart = input("Veuillez saisir l'arrêt de départ : ")
ListeLignesDepartTrouvees = rechercheArret(ListeLigne, NomLigne, depart)
print(ListeLignesDepartTrouvees)

# Recherche arrivé dans une ligne
arrivee = input("Veuillez saisir l'arrêt d'arrivé : ")
ListeLignesArriveeTrouvees = rechercheArret(ListeLigne, NomLigne, arrivee)
print(ListeLignesArriveeTrouvees)

# Recherche départ et arrivé sur une même ligne
LigneCommun = rechercheLigneCommun(ListeLignesDepartTrouvees, ListeLignesArriveeTrouvees)

# Recherche index de la ligne
arretCorrespondant = []
if LigneCommun :
  indexLigneCommun = rechercheIndexLigneCommun(LigneCommun, NomLigne)
else :
  listeArretCorrespondancedepart = rechercheArretCorrespondance(ListeLignesDepartTrouvees, Correspondance, ListeLigne, NomLigne)
  listeArretCorrespondancearrivee = rechercheArretCorrespondance(ListeLignesArriveeTrouvees, Correspondance, ListeLigne, NomLigne)
  for arretCorrespondancedepart in listeArretCorrespondancedepart:
    if arretCorrespondancedepart in listeArretCorrespondancearrivee:
      arretCorrespondant.append(arretCorrespondancedepart)
  print("Correspondance :",arretCorrespondant)

  
# Recherche terminus
if LigneCommun :
  rechercheTerminus(indexLigneCommun, depart, arrivee, ListeLigne)
else:
  rechercheTerminusCorrespondance(arretCorrespondant, ListeLigne, NomLigne, depart, arrivee, ListeLignesDepartTrouvees, ListeLignesArriveeTrouvees)

