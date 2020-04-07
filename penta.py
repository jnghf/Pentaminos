#!/usr/bin/env python3
# -*- coding: utf-8 -*-

""" Recherche récursive de placement de PENTAMINOS 
                04/01/2019

    XMAX, YMAX : taille de la figure
    Pour une meilleure efficacité de l'algorithme,
    XMAX doit être inférieur à YMAX

    Adapter les pièces utilisées dans la procédure
    crea_pieces() en commentant les pièces non 
    utilisées.
    Nb pieces * 5  doit être égal à XMAX * YMAX

    12 pentas :  3*20  4*15 5*12  6*10
    11 pentas :  5*11
    10 pentas :  5*10
     9 pentas :  5*9  3*15
     8 pentas :  5*8 4*10
     7 pentas :  5*7 
     6 pentas :  5*6 3*10
     5 pentas :  5*5
     4 pentas :  5*4
"""

XMAX = 5
YMAX = 11

""" Définition des  12 pentaminos 
    piece[0] : Type du pentamino(1 à 12)
    piece[1] : Définition des placements possibles de 
               la pièce (dx/dy) par rapport à l'origine
    piece[2] : False/non utilisée True/utilisée
"""

""" 
                X X X X X
"""
piece1 = [1, [[[0, 1], [0, 2], [0, 3], [0, 4]],
              [[1, 0], [2, 0], [3, 0], [4, 0]]], False]

""" 
                X X X X
                X
"""
piece2 = [2, [[[0, 1], [0, 2], [0, 3], [1, 3]],
              [[1, 0], [1, 1], [1, 2], [1, 3]],
              [[1, 0], [2, 0], [3, -1], [3, 0]],
              [[0, 1], [1, 0], [2, 0], [3, 0]],
              [[1, -3], [1, -2], [1, -1], [1, 0]],
              [[1, 0], [2, 0], [3, 0], [3, 1]],
              [[1, 0], [0, 1], [0, 2], [0, 3]],
              [[0, 1], [1, 1], [2, 1], [3, 1]]], False]

""" 
                X X X X
                  X
"""
piece3 = [3, [[[0, 1], [0, 2], [0, 3], [1, 2]],
              [[1, -1], [1, 0], [1, 1], [1, 2]],
              [[1, 0], [2, -1], [2, 0], [3, 0]],
              [[1, 0], [1, 1], [2, 0], [3, 0]],
              [[1, -2], [1, -1], [1, 0], [1, 1]],
              [[1, -1], [1, 0], [2, 0], [3, 0]],
              [[1, 0], [2, 0], [2, 1], [3, 0]],
              [[0, 1], [0, 2], [0, 3], [1, 1]]], False]

""" 
                X X X 
                    x X
"""
piece4 = [4, [[[0, 1], [0, 2], [1, 2], [1, 3]],
              [[1, 0], [2, -1], [2, 0], [3, -1]],
              [[0, 1], [1, 1], [1, 2], [1, 3]],
              [[1, -1], [1, 0], [2, -1], [3, -1]],
              [[1, 0], [1, 1], [2, 1], [3, 1]],
              [[0, 1], [1, -2], [1, -1], [1, 0]],
              [[1, 0], [2, 0], [2, 1], [3, 1]],
              [[0, 1], [0, 2], [1, -1], [1, 0]]], False]

""" 
                X X X 
                X
                X
"""
piece5 = [5, [[[0, 1], [0, 2], [1, 0], [2, 0]],
              [[0, 1], [0, 2], [1, 2], [2, 2]],
              [[1, 0], [2, -2], [2, -1], [2, 0]],
              [[1, 0], [2, 0], [2, 1], [2, 2]]], False]

""" 
                X X X 
                X X
"""
piece6 = [6, [[[0, 1], [0, 2], [1, 0], [1, 1]],
              [[0, 1], [1, 0], [1, 1], [2, 1]],
              [[0, 1], [1, -1], [1, 0], [1, 1]],
              [[1, 0], [1, 1], [2, 0], [2, 1]],
              [[1, -1], [1, 0], [2, -1], [2, 0]],
              [[0, 1], [1, 0], [1, 1], [1, 2]],
              [[0, 1], [1, 0], [1, 1], [2, 0]],
              [[0, 1], [0, 2], [1, 1], [1, 2]]], False]

""" 
                X X X 
                X   X
"""
piece7 = [7, [[[0, 1], [0, 2], [1, 0], [1, 2]],
              [[0, 1], [1, 1], [2, 0], [2, 1]],
              [[0, 2], [1, 0], [1, 1], [1, 2]],
              [[0, 1], [1, 0], [2, 0], [2, 1]]], False]

""" 
                X X 
                  X
                  X X
"""
piece8 = [8, [[[0, 1], [1, 1], [2, 1], [2, 2]],
              [[1, -2], [1, -1], [1, 0], [2, -2]],
              [[1, 0], [1, 1], [1, 2], [2, 2]],
              [[0, 1], [1, 0], [2, -1], [2, 0]]], False]

""" 
                  X
                X X X X
                X
"""
piece9 = [9, [[[1, -2], [1, -1], [1, 0], [2, -1]],
              [[1, -1], [1, 0], [2, 0], [2, 1]],
              [[1, -1], [1, 0], [1, 1], [2, -1]],
              [[1, -1], [1, 0], [1, 1], [2, 1]],
              [[1, 0], [1, 1], [2, -1], [2, 0]],
              [[1, 0], [1, 1], [1, 2], [2, 1]],
              [[0, 1], [1, -1], [1, 0], [2, 0]],
              [[0, 1], [1, 1], [1, 2], [2, 1]]], False]

""" 
                X X X 
                  X
                  X
"""
piece10 = [10, [[[0, 1], [0, 2], [1, 1], [2, 1]],
                [[1, -2], [1, -1], [1, 0], [2, 0]],
                [[1, 0], [2, -1], [2, 0], [2, 1]],
                [[1, 0], [1, 1], [1, 2], [2, 0]]], False]

""" 
                X X
                  X X
                    X
"""
piece11 = [11, [[[0, 1], [0, 2], [1, 2], [2, 2]],
                [[1, -1], [1, 0], [2, -2], [2, -1]],
                [[1, 0], [1, 1], [2, 1], [2, 2]],
                [[0, 1], [1, -1], [1, 0], [2, -1]]], False]

""" 
                  X
                X X X 
                  X
"""
piece12 = [12, [[[1, -1], [1, 0], [1, 1], [2, 0]]], False]


""" Pieces disponibles pour la recherche
    Commenter les lignes des pentas non demandés """


def crea_pieces():
    pieces = []

    pieces.append(piece1)
    pieces.append(piece2)
    pieces.append(piece3)
    pieces.append(piece4)
    pieces.append(piece5)
    pieces.append(piece6)
    pieces.append(piece7)
    pieces.append(piece8)
    pieces.append(piece9)
    pieces.append(piece10)
    # pieces.append(piece11)
    pieces.append(piece12)

    return pieces


""" Création du plateau. 
    Les bords sont définis par -1 """


def crea_tab():
    tab = [[0 for x in range(XMAX + 2)] for y in range(YMAX + 2)]
    for y in range(YMAX + 2):
        for x in range(XMAX + 2):
            if (x == 0 or x == XMAX+1 or y == 0 or y == YMAX+1):
                tab[y][x] = -1
    return tab


""" Affichage de la solution trouvée
    x/y sont inversés pour un affichage
    plus lisible à l'écran """


def aff_tab():
    for x in range(XMAX + 2):
        for y in range(YMAX + 2):
            if tab[y][x] == -1:
                print(" - ", end='')
            elif tab[y][x] < 10:
                print(' 0' + str(tab[y][x]), end='')
            else:
                print(' ' + str(tab[y][x]), end='')
        print('\n')


""" Recherche 1ère position libre """


def pos_libre():
    pos = [-1, -1]
    for y in range(1, YMAX + 1):
        for x in range(1, XMAX + 1):
            if tab[y][x] == 0:
                pos = [y, x]
                return pos
    return pos


""" Annuler un enregistrement de pièce """


def annul_piece(num, piece):
    for y in range(1, YMAX + 1):
        for x in range(XMAX + 1):
            if tab[y][x] == num:
                tab[y][x] = 0
    # annuler memo piece
    pieces[piece][2] = False


""" Enregistrement d'une pièce
        - num: type de penta
        - piece: index penta dans pieces
        - forme: suivant orientation penta
        - x/y : position de base du penta """


def enreg(num, piece, forme, y, x):
    tab[y][x] = num
    for i in range(4):
        dy = pieces[piece][1][forme][i][0]
        dx = pieces[piece][1][forme][i][1]
        tab[y + dy][x + dx] = num
    # memo piece
    pieces[piece][2] = True


""" Placement possible ?
    du penta à la position x/y """


def possible(piece, forme, y, x):
    for i in range(4):
        dy = pieces[piece][1][forme][i][0]
        dx = pieces[piece][1][forme][i][1]
        if ((x + dx) > XMAX or (x+dx) < 1 or (y+dy) < 1 or (y+dy) > YMAX):
            return False
        if tab[y + dy][x + dx] != 0:
            return False
    return True


""" Recherche récursive de placement des pentaminos """


def rech():
    libre = pos_libre()
    if libre[0] != -1:  # première case libre
        for piece in range(len(pieces)):
            if pieces[piece][2] == False:
                for forme in range(len(pieces[piece][1])):
                    if possible(piece, forme, libre[0], libre[1]):
                        enreg(pieces[piece][0], piece,
                              forme, libre[0], libre[1])
                        rech()  # Récursion
                        annul_piece(pieces[piece][0], piece)
    else:
        print("\nPremière solution trouvée de ", XMAX, "X", YMAX)
        aff_tab()
        exit()


pieces = crea_pieces()
tab = crea_tab()

rech()
aff_tab()
