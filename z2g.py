#!/usr/bin/env python3
import sys
if len(sys.argv) < 2:
    print("Z2G.py <nom_fichier.txt> (export Zotero RefWorks Tagged)",file=sys.stderr)
    exit(1)

sNomfic = sys.argv[1]

#
#   Initialisation varaible globale
#
dZotero= {}
nbart=1
nbaut=1
nbtag=1

#
#   s/programme
#
def ClearVirgule( sTheString ):
    sResult = sTheString.replace(',',' ')
    return( sResult )

def addT1( sLine ):
        dataline = sLine[3:]
        sKey="{:02d}".format(nbart)+"T1"
        dZotero[sKey]=ClearVirgule(dataline.rstrip())

def addRT( sLine ):
        dataline = sLine[3:]
        sKey="{:02d}".format(nbart)+"RT"
        dZotero[sKey]=ClearVirgule(dataline.rstrip())

def addYR( sLine ):
        dataline = sLine[3:]
        sKey="{:02d}".format(nbart)+"YR"
        dZotero[sKey]=ClearVirgule(dataline.rstrip())

def addLA( sLine ):
        dataline = sLine[3:]
        sKey="{:02d}".format(nbart)+"LA"
        dZotero[sKey]=ClearVirgule(dataline.rstrip())

def addA1( sLine ):
        dataline = sLine[3:]
        sKey="{:02d}".format(nbart)+"A1"+"{:02d}".format(nbaut)
        dZotero[sKey]=ClearVirgule(dataline.rstrip())

def addK1( sLine ):
        dataline = sLine[3:]
        sKey="{:02d}".format(nbart)+"K1"+"{:02d}".format(nbtag)
        dZotero[sKey]=ClearVirgule(dataline.rstrip())

#
#   Ouvrir des fichiers
#
fZotero = open(sNomfic, encoding='utf8')
fT1 = open("Titre.csv","w")

# utilisez readline() pour lire la première ligne
line = fZotero.readline()

while line:
    # utilisez readline() pour lire la ligne suivante
    line = fZotero.readline()
    if  line[0:2] == "T1":
        addT1( line )
        nbart=nbart+1
        nbaut=1 
        nbtag=1
        
    if  line[0:2] == "RT":
        addRT( line )

    if  line[0:2] == "YR":
        addYR( line )

    if  line[0:2] == "LA":
        addLA( line )

    if  line[0:2] == "A1":
        addA1( line )
        nbaut=nbaut+1

    if  line[0:2] == "K1":
        addK1( line )
        nbtag=nbtag+1

fZotero.close()

#
#   Ajout nombre d'article
#
dZotero["T1"]="{:02d}".format(nbart-1)

#print( dZotero )

#
#   Restitution
#
fT1.write("Id,Label,RT,YR,LA\n")

iNbArti = int(dZotero["T1"])
print( "Nombre article = ", iNbArti)
i=1
while i < iNbArti+1:
    try:
        sLabel = dZotero[str(i).zfill(2)+"T1"]
    except:
        sLabel = "vide"
    try:
        sRT = dZotero[str(i).zfill(2)+"RT"]
    except:
        sRT = "vide"
    try: 
        sYR = dZotero[str(i).zfill(2)+"YR"]
    except:
         sYR = "vide"
    try:
        sLA = dZotero[str(i).zfill(2)+"LA"]
    except:
        sLA = "vide"
    fT1.write(str(i).zfill(2)+ "," + sLabel + "," + sRT + "," + sYR + "," + sLA + "\n" )
    i = i +1  

fT1.close()
#
#   Fin
#