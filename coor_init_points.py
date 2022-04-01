# -*- coding: utf-8 -*-

import numpy as np
import sys
import datetime

# filepath = r"C:\Users\User\Desktop\pythonTien\TEST_STA3_RawData.dat"      # Localisation du fichier des données
# nom = "O01E01_STA3"
# nb_point_tot = 48                                  # Nombre total de points (points de référence compris)
# ligne_0 = 5                                         # Première ligne de données (instant initial)
# colonne_0 = 11                                      # Première colonne de données de position des points
# sigma_D = 500E-6                      # Précision de la mesure de distance (en mètre)-0.5mm
# sigma_V = 2.36E-6                   # Précision de la mesure d'angle verticale (en radian)-0.5 seconde
# sigma_H = 2.36E-6                    # Précision de la mesure d'angle horizontale (en radian)


filepath = r"PATH\TO\RAWDATA"  # Localisation du fichier des données
nom = "TEST_STA1"
nb_point_tot = 49  # Nombre total de points (points de référence compris)
ligne_0 = 5  # Première ligne de données (instant initial)
colonne_0 = 11  # Première colonne de données de position des points

ligne_0 = ligne_0 - 1  # Position dans la liste python
colonne_0 = colonne_0 - 1  # Position dans la liste python


def lines(filepath, nb_point_tot):  # Lire le fichier de donnees, supprimer la redondance
    lines = [line.rstrip('\n') for line in
             open(filepath)]  # -et le transeformer en une liste des listes des chaines de caractères
    lines = lines[ligne_0:len(lines)]
    lines = list(set(lines))
    for i in range(len(lines)):
        lines[i] = lines[i].split(',')
        if len(lines[i]) != colonne_0 + 6 * nb_point_tot:
            print("Le nombre total de points n'est pas correct!")
            sys.exit()
    lines.sort(key=lambda line: datetime.datetime.strptime(line[0][1:-1], '%Y-%m-%d %H:%M:%S'))
    return lines


def points_i_j_l(lines):  # Construire une matrice 3D des résultats de mesure
    points_i_j_l = np.zeros(
        (len(lines), nb_point_tot, 6))  # -pour les points de référence à partir de la liste des données
    for i in range(len(lines)):
        for j in range(nb_point_tot):
            for l in range(6):
                points_i_j_l[i][j][l] = float(lines[i][colonne_0 + l * nb_point_tot + j])
    return points_i_j_l


def position_initiale_k(points_i_j_l, j):  # Calculer la position initiale du point j d'étude --> Matrice 1D de taille 3
    posi_init_k = np.array([-99999., -99999., -99999.])
    for i in range(len(points_i_j_l)):
        Hij0 = points_i_j_l[i][j][0]
        Vij1 = points_i_j_l[i][j][1]
        Dij2 = float(points_i_j_l[i][j][2])
        Hij0_DR = points_i_j_l[i][j][3]
        Vij1_DR = points_i_j_l[i][j][4]
        Dij2_DR = points_i_j_l[i][j][5]

        if sum(np.array([Hij0, Hij0_DR, Vij1, Vij1_DR, Dij2, Dij2_DR])) > 0:
            alpha = np.pi / 200
            posi_init_k[0] = 0.5 * (
                        Dij2 * np.sin(alpha * Vij1) * np.sin(alpha * Hij0) + Dij2_DR * np.sin(alpha * Vij1_DR) * np.sin(
                    alpha * Hij0_DR))
            posi_init_k[1] = 0.5 * (
                        Dij2 * np.sin(alpha * Vij1) * np.cos(alpha * Hij0) + Dij2_DR * np.sin(alpha * Vij1_DR) * np.cos(
                    alpha * Hij0_DR))
            posi_init_k[2] = 0.5 * (Dij2 * np.cos(alpha * Vij1) + Dij2_DR * np.cos(alpha * Vij1_DR))
            return posi_init_k
    return posi_init_k


l = lines(filepath, nb_point_tot)
p_i_j_l = points_i_j_l(l)

fichier = open(nom + '_coor_init.dat', 'w')
for j in range(nb_point_tot):
    posi_init_k = position_initiale_k(p_i_j_l, j)
    fichier.write(
        "MPO_" + "%0.3d" % (j + 1) + ":" + "%0.5f" % posi_init_k[0] + "," + "%0.5f" % posi_init_k[1] + "," + "%0.5f" %
        posi_init_k[2] + "," + "\n")
fichier.close()
