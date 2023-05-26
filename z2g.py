#!/usr/bin/env python3
import sys
if len(sys.argv) < 2:
    print("Z2G.py <nom_fichier.txt> (export Zotero RefWorks Tagged)",file=sys.stderr)
    exit(1)


nomfic = sys.argv[1]
#print(nomfic)

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
def addT1( sLine ):
        dataline = sLine[3:]
        sKey="{:02d}".format(nbart)+"T1"
        dZotero[sKey]=dataline.rstrip()

def addRT( sLine ):
        dataline = sLine[3:]
        sKey="{:02d}".format(nbart)+"RT"
        dZotero[sKey]=dataline.rstrip()   

def addYR( sLine ):
        dataline = sLine[3:]
        sKey="{:02d}".format(nbart)+"YR"
        dZotero[sKey]=dataline.rstrip()

def addLA( sLine ):
        dataline = sLine[3:]
        sKey="{:02d}".format(nbart)+"LA"
        dZotero[sKey]=dataline.rstrip()

def addA1( sLine ):
        dataline = sLine[3:]
        sKey="{:02d}".format(nbart)+"A1"+"{:02d}".format(nbaut)
        dZotero[sKey]=dataline.rstrip()

def addK1( sLine ):
        dataline = sLine[3:]
        sKey="{:02d}".format(nbart)+"K1"+"{:02d}".format(nbtag)
        dZotero[sKey]=dataline.rstrip()

#
#   Ouvrir le fichier en lecture seule
#
file = open(nomfic, encoding='utf8')

# utilisez readline() pour lire la première ligne
line = file.readline()

while line:
    # utilisez readline() pour lire la ligne suivante
    line = file.readline()
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

file.close()
#
#   Ajout nombre d'article
#
#sKey="{:02d}".format(nbart-1)+"A1"
#dZotero[sKey]="{:02d}".format(nbaut-1)

#sKey="{:02d}".format(nbart-1)+"K1"
#dZotero[sKey]="{:02d}".format(nbtag-1)

dZotero["T1"]="{:02d}".format(nbart-1)

print( dZotero )
