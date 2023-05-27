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
nbart=0
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
        sKey="{:02d}".format(nbart)+"A1"
        dZotero[sKey]="{:02d}".format(nbaut)
               
def addK1( sLine ):
        dataline = sLine[3:]
        sKey="{:02d}".format(nbart)+"K1"+"{:02d}".format(nbtag)
        dZotero[sKey]=ClearVirgule(dataline.rstrip())
        sKey="{:02d}".format(nbart)+"K1"
        dZotero[sKey]="{:02d}".format(nbtag)
#
#   Ouvrir des fichiers
#
fZotero = open(sNomfic, encoding='utf8')
fT1 = open("T1.csv","w")
fA1 = open("A1.csv","w")
fK1 = open("K1.csv","w")

for line in fZotero:

    if  line[0:2] == "RT": 
        if nbart == 0:
            nbart=1
        else:
            nbart=nbart+1
        nbaut=1 
        nbtag=1
        addRT( line )

    if  line[0:2] == "T1":
        addT1( line )

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
dZotero["T1"]="{:02d}".format(nbart)

print( dZotero )

#
#   Restitution des Titres
#
fT1.write("Id,Label,RT,YR,LA\n")

iNbArti = int(dZotero["T1"])
i=1
while i < iNbArti+1:
    try:
        sLabel = dZotero[str(i).zfill(2)+"T1"]
    except:
        sLabel = "neant"
    try:
        sRT = dZotero[str(i).zfill(2)+"RT"]
    except:
        sRT = "neant"
    try: 
        sYR = dZotero[str(i).zfill(2)+"YR"]
    except:
         sYR = "0000"
    try:
        sLA = dZotero[str(i).zfill(2)+"LA"]
    except:
        sLA = "??"
    fT1.write(str(i).zfill(2)+ "," + sLabel + "," + sRT + "," + sYR + "," + sLA + "\n" )
    i = i +1  

fT1.close()

#
#   Restitution des auteurs
#
fA1.write("Id,Label\n")
iNbArti = int(dZotero["T1"])
i=1
a1=1
while i < iNbArti+1:
    nA1 = dZotero[str(i).zfill(2)+"A1"]
    a = 1
    while a < int(nA1):
        sA1 = dZotero[str(i).zfill(2)+"A1"+str(a).zfill(2)]
        fA1.write(str(a1).zfill(2)+ "," + sA1 + "\n" )
        a = a + 1
        a1 = a1 + 1  

    i = i + 1
    
fA1.close()

#
#   Restitution des tags
#
fK1.write("Id,Label\n")
iNbArti = int(dZotero["T1"])
i=1
k1=1
while i < iNbArti+1:
    try:
        nK1 = dZotero[str(i).zfill(2)+"K1"]
    except:
        nK1 = 0
    k = 1
    while k < int(nK1):
        sK1 = dZotero[str(i).zfill(2)+"K1"+str(k).zfill(2)]
        fK1.write(str(k1).zfill(2)+ "," + sK1 + "\n" )
        k = k + 1
        k1 = k1 + 1  

    i = i + 1
    
fK1.close()
#
#   Fin
#