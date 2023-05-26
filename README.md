# z2g
Conversion Zotero vers Gephi

Le but de ce programme Python de permettre une extraction des données de Zotero à partir d'un export au formmat RefWorks Tagged (.TXT),
afin de géner des fichiers au format (.CSV) de node et de lien pour les auteurs et les tags.

Le programme est basé sur une extraction des données en entrée selon le format suivant:

	RF ...... (type de journal ou de revue)
	T1 ...... (Titre principal de l'article)
	A1 ...... (Auteur numero 1)
	An ...... (Auteur numero N)
	YR ...... (Année de l'article)
	LA ...... (Langue de l'article)
	K1 ...... (Tag numero 1
	Kn ...... (Tag numero N)

Puis le mettre dans un dictionnaire selon le format suivant:

	nnRF .....
	nnT1 .....
	nnA1aa .....
	nnYR .....
	nnLA .....
	nnK1kk ....
	T1 .... (nombre d'article nn de la base Zotero)

