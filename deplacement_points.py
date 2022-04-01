# Dans la suite, l'indice i désigne les instants de mesures (les lignes de résultats), l'indice j désigne
# -les différents points que ce soit les points de référence ou les points d'étude, l'indice k désigne
# -les 3 ou 4 coordonnées (x,y,z,G), l'indice l désigne les 6 mesures d'un point en Hz,Vt,Dp et double
# -retournement
# Une matrice 3D par exemple de type A_i_j_k correspond à l'instant i, au point j et à la coordonnée k
# Une matrice 2D par exemple de type Ai_j_k à un instant i donné correspond au point j et à la coordonnée k


import numpy as np
import csv
import sys
import datetime

# filepath = r"C:\Users\User\Desktop\pythonTien\O01E01_STA3_RawData.dat"      # Localisation du fichier des données
# filepath_coor_init = r"C:\Users\User\Desktop\pythonTien\O01E01_STA3_coor_init.dat"
# nom = "O01E01_STA3"
# nb_point_ref = 5                                   # Nombre de points de référence
# posi_ref = [1,2,3,4,5]                              # Position des points de référence
# nb_point_tot = 48                                  # Nombre total de points (points de référence compris)
# ligne_0 = 5                                         # Première ligne de données (instant initial)
# colonne_0 = 11                                      # Première colonne de données de position des points
# sigma_D = 500E-6                      # Précision de la mesure de distance (en mètre)-0.5mm
# sigma_V = 2.36E-6                   # Précision de la mesure d'angle verticale (en radian)-0.5 seconde
# sigma_H = 2.36E-6                    # Précision de la mesure d'angle horizontale (en radian)
# inst_init = datetime.datetime(2019, 4, 20, 0, 0, 0)
# inst_fin = datetime.datetime(2019, 5, 3, 23, 59, 59)


# filepath = r"C:\Users\User\Desktop\pythonTien\L16_103P_STA2_RawData.dat"    # Localisation du fichier des données
# filepath_coor_init = r"C:\Users\User\Desktop\pythonTien\O0103P_STA2_coor_init.dat"
# nom = "O0103P_STA2"
# nb_point_ref = 5                                    # Nombre de points de référence
# posi_ref = [1,2,3,4,5]                              # Position des points de référence
# nb_point_tot = 17                                   # Nombre total de points (points de référence compris)
# ligne_0 = 5                                         # Première ligne de données (instant initial)
# colonne_0 = 11                                      # Première colonne de données de position des points
# sigma_D = 500E-6                      # Précision de la mesure de distance (en mètre)-0.5mm
# sigma_V = 2.36E-6                   # Précision de la mesure d'angle verticale (en radian)-0.5 seconde
# sigma_H = 2.36E-6                    # Précision de la mesure d'angle horizontale (en radian)
# inst_init = datetime.datetime(2019, 5, 17, 0, 0, 0)
# inst_fin = datetime.datetime(2019, 5, 19, 23, 59, 59)


# filepath = r"C:\Users\User\Desktop\pythonTien\L16_102P_STA1_RawData.dat"    # Localisation du fichier des données
# filepath_coor_init = r"C:\Users\User\Desktop\pythonTien\O0102P_STA1_coor_init.dat"
# nom = "O0102P_STA1"
# nb_point_ref = 4                                    # Nombre de points de référence
# posi_ref = [1,4,20,19]                              # Position des points de référence
# nb_point_tot = 20                                   # Nombre total de points (points de référence compris)
# ligne_0 = 5                                         # Première ligne de données (instant initial)
# colonne_0 = 11                                      # Première colonne de données de position des points
# sigma_D = 500E-6                      # Précision de la mesure de distance (en mètre)-0.5mm
# sigma_V = 2.36E-6                   # Précision de la mesure d'angle verticale (en radian)-0.5 seconde
# sigma_H = 2.36E-6                    # Précision de la mesure d'angle horizontale (en radian)
# inst_init = datetime.datetime(2019, 4, 26, 0, 0, 0)
# inst_fin = datetime.datetime(2019, 5, 10, 23, 59, 59)


filepath = r"PATH\TO\TEST_RAW_DATA\TEST_STA1_RawData.dat"  # Localisation du fichier des données
filepath_coor_init = r"PATH\TO\COOR_INIT\TEST_coor_init.dat"
nom = "TEST_STA1"
nb_point_ref = 4  # Nombre de points de référence
posi_ref = [1, 2, 48, 49]  # Position des points de référence
nb_point_tot = 49  # Nombre total de points (points de référence compris)
ligne_0 = 5  # Première ligne de données (instant initial)
colonne_0 = 11  # Première colonne de données de position des points
sigma_D = 500E-6  # Précision de la mesure de distance (en mètre)-0.5mm
sigma_V = 2.36E-6  # Précision de la mesure d'angle verticale (en radian)-0.5 seconde
sigma_H = 2.36E-6  # Précision de la mesure d'angle horizontale (en radian)
inst_init = datetime.datetime(2018, 5, 8, 0, 0, 0)
inst_fin = datetime.datetime(2019, 5, 9, 23, 59, 59)

if nb_point_ref != len(posi_ref):
    print("Vérifier le nombre de points de référence!")
    sys.exit()

nb_point_etude = nb_point_tot - nb_point_ref  # Nombre de points d'étude
posi_etude = [i for i in range(1, nb_point_tot + 1) if not i in posi_ref]  # Position des points d'étude

ligne_0 = ligne_0 - 1  # Position dans la liste python
colonne_0 = colonne_0 - 1  # Position dans la liste python
posi_ref = [p_ref - 1 for p_ref in posi_ref]  # Position dans la liste python
posi_etude = [p_etude - 1 for p_etude in posi_etude]  # Position dans la liste python


def instant(line):
    return datetime.datetime.strptime(line[0][1:-1], '%Y-%m-%d %H:%M:%S')


def lines(filepath, nb_point_tot, inst_init, inst_fin):  # Lire le fichier de donnees, supprimer la redondance
    lines = [line.rstrip('\n') for line in
             open(filepath)]  # -et le transeformer en une liste des listes des chaines de caractères
    lines = lines[ligne_0:len(lines)]
    lines = list(set(lines))
    for i in range(len(lines)):
        lines[i] = lines[i].split(',')
        if len(lines[i]) != colonne_0 + 6 * nb_point_tot:
            print("Le nombre total de points n'est pas correct!")
            sys.exit()
    lines.sort(key=lambda line: instant(line))
    lines = [line for line in lines if (instant(line) >= inst_init) & (instant(line) <= inst_fin)]
    return lines


def points_ref_i_j_l(lines):  # Construire une matrice 3D des résultats de mesure
    points_ref_i_j_l = np.zeros(
        (len(lines), nb_point_ref, 6))  # -pour les points de référence à partir de la liste des données
    for i in range(len(lines)):
        for j in range(nb_point_ref):
            for l in range(6):
                points_ref_i_j_l[i][j][l] = float(lines[i][colonne_0 + l * nb_point_tot + posi_ref[j]])
    return points_ref_i_j_l


def points_etude_i_j_l(lines):  # Construire une matrice 3D des résultats de mesure
    points_etude_i_j_l = np.zeros(
        (len(lines), nb_point_etude, 6))  # -pour les points d'étude à partir de la liste des données
    for i in range(len(lines)):
        for j in range(nb_point_etude):
            for l in range(6):
                points_etude_i_j_l[i][j][l] = float(lines[i][colonne_0 + l * nb_point_tot + posi_etude[j]])
    return points_etude_i_j_l


def taux_visee_i(points_etude_i_j_l):  # Construire une matrice 1D de taux visée à partir
    taux_visee_i = np.zeros(
        len(points_etude_i_j_l))  # -de la matrice 3D des résultats de mesure pour les points d'étude
    for i in range(len(points_etude_i_j_l)):
        points_etudei_j_l = points_etude_i_j_l[i]
        for j in range(len(points_etudei_j_l)):
            if sum(points_etudei_j_l[j]) > 0:
                taux_visee_i[i] = taux_visee_i[i] + 100 / len(points_etudei_j_l)
    return taux_visee_i


def deplacement_station_k(points_ref0_j_l,
                          points_refi_j_l):  # Calculer le déplacement de la station (x,y,z,G) --> Matrice 1D de taille 4
    n = int(len(points_ref0_j_l))  # -à un instant par rapport à l'instant initial
    check_points_ref_j = [True] * nb_point_ref
    for j in range(nb_point_ref):
        check_points_ref0j = sum(points_ref0_j_l[j]) > 0  # Vérifier si les mesures initiales et à l'instant
        check_points_refij = sum(points_refi_j_l[j]) > 0  # -en question de chaque point de référence sont bonnes
        check_points_ref_j[j] = check_points_ref0j and check_points_refij  # On enlève un point si au moins un
    points_ref0_j_l = points_ref0_j_l[check_points_ref_j]  # -des deux mesures sont mauvaises
    points_refi_j_l = points_refi_j_l[check_points_ref_j]
    n = int(len(points_ref0_j_l))  # Nombre de points de reférence serviables
    if n < 3:  # Méthode des moindres carrés n'est pas très fiable si le nombre
        return np.array([-99999, -99999, -99999,
                         -99999])  # -de points de référence est trop faible, on ne calcul pas pour cet instant

    K = [[1. / sigma_D ** 2, 0, 0, 0, 0, 0],  # Matrice des poids (déterminée à un coefficient multiplicatif près)
         [0, 1. / sigma_V ** 2, 0, 0, 0, 0],
         # 6 observables pour un point à un instant donné (Dp,Vt,Hz,Dp_DR,Vt_DR,Hz_DR)
         [0, 0, 1. / sigma_H ** 2, 0, 0, 0],
         [0, 0, 0, 1. / sigma_D ** 2, 0, 0],
         [0, 0, 0, 0, 1. / sigma_V ** 2, 0],
         [0, 0, 0, 0, 0, 1. / sigma_H ** 2]
         ]

    alpha = np.pi / 200  # Coefficient de conversion gon-radian
    SMTPM = np.zeros((4, 4))  # Somme de MjT.P.Mj avec Mj la matrice 4x4 correspondant au point de référence j
    SMTPDF = np.zeros((4, 1))  # Somme de MjT.P.DFj avec DFj la différence entre deux résultats de mesure

    for j in range(n):
        H0 = alpha * points_ref0_j_l[j][
            0]  # Lecture de résultat de mesure initiale de l'angle horizontale et conversion en radian (du point j)
        Hi = alpha * points_refi_j_l[j][
            0]  # Lecture de résultat de mesure à l'instant i de l'angle horizontale et conversion en radian (du point j)
        V0 = alpha * points_ref0_j_l[j][
            1]  # Lecture de résultat de mesure initiale de l'angle verticale et conversion en radian (du point j)
        Vi = alpha * points_refi_j_l[j][1]
        D0 = points_ref0_j_l[j][2]
        Di = points_refi_j_l[j][2]
        H0_DR = alpha * points_ref0_j_l[j][
            3]  # Lecture de résultat en double retournement de mesure initiale de l'angle horizontale et conversion en radian (du point j)
        Hi_DR = alpha * points_refi_j_l[j][3]
        V0_DR = alpha * points_ref0_j_l[j][4]
        Vi_DR = alpha * points_refi_j_l[j][4]
        D0_DR = points_ref0_j_l[j][5]
        Di_DR = points_refi_j_l[j][5]
        err_colimat_moyen = 0
        for j1 in range(n):
            V01 = alpha * points_ref0_j_l[j1][1]
            Vi1 = alpha * points_refi_j_l[j1][1]
            V0_DR1 = alpha * points_ref0_j_l[j1][4]
            Vi_DR1 = alpha * points_refi_j_l[j1][4]
            err_colimat_moyen = err_colimat_moyen + 0.5 / n * (Vi1 - V01 + Vi_DR1 - V0_DR1)

        delta_Fj = [[Di - D0], [Vi - V0 - err_colimat_moyen], [Hi - H0], [Di_DR - D0_DR],
                    [Vi_DR - V0_DR - err_colimat_moyen], [
                        Hi_DR - H0_DR]]  # Différence entre les résultats de mesure initial et à l'instant de calcul du point j
        Mj = [[-np.sin(V0) * np.sin(H0), -np.sin(V0) * np.cos(H0), -np.cos(V0), 0],
              # Matrice des dérivées partielles des 6 observables
              [-np.cos(V0) * np.sin(H0) / D0, -np.cos(V0) * np.cos(H0) / D0, np.sin(V0) / D0, 0],
              # -par rapport aux 4 inconnus, appliqué au point j
              [-np.cos(H0) / (D0 * np.sin(V0)), np.sin(H0) / (D0 * np.sin(V0)), 0, -1.],
              [-np.sin(V0) * np.sin(H0), -np.sin(V0) * np.cos(H0), -np.cos(V0), 0],
              [np.cos(V0) * np.sin(H0) / D0, np.cos(V0) * np.cos(H0) / D0, -np.sin(V0) / D0, 0],
              [-np.cos(H0) / (D0 * np.sin(V0)), np.sin(H0) / (D0 * np.sin(V0)), 0, -1.],
              ]

        SMTPM = SMTPM + np.dot(np.dot(np.transpose(Mj), K), Mj)  # Somme de MjT.P.Mj de 0 à j
        SMTPDF = SMTPDF + np.dot(np.dot(np.transpose(Mj), K), delta_Fj)  # Somme de MjT.P.DFj de 0 à j

    U = np.dot(np.linalg.inv(SMTPM), SMTPDF)  # Solution des moindres carrés (x,y,z,G)
    dep_station_k = [0, 0, 0, 0]
    dep_station_k[0] = U[0][0]  # Ajout de coordonnées initiales
    dep_station_k[1] = U[1][0]
    dep_station_k[2] = U[2][0]
    dep_station_k[3] = U[3][0]
    return dep_station_k


def deplacement_station_i_k(points_ref_i_j_l,
                            filepath_coor_init):  # Calculer le déplacement de la station à tout moment --> Matrice 2D
    dep_station_i_k = np.zeros((len(points_ref_i_j_l), 4))
    points_ref0_j_l = np.array([[-99999.] * 6] * nb_point_ref)
    posi_init_j_k = position_initiale_j_k(filepath_coor_init)
    for j in range(nb_point_ref):
        posi_initj_k = posi_init_j_k[posi_ref[j]]
        points_ref0_j_l[j][2] = (posi_initj_k[0] ** 2 + posi_initj_k[1] ** 2 + posi_initj_k[2] ** 2) ** 0.5
        points_ref0_j_l[j][0] = 100 - 200. / np.pi * np.arctan(posi_initj_k[1] / posi_initj_k[0]) + 100 * (
                    1 - np.sign(posi_initj_k[0]))
        points_ref0_j_l[j][1] = 100 - 200. / np.pi * np.arcsin(posi_initj_k[2] / points_ref0_j_l[j][2])
        points_ref0_j_l[j][3] = (points_ref0_j_l[j][0] + 200) % 400
        points_ref0_j_l[j][4] = 400 - points_ref0_j_l[j][1]
        points_ref0_j_l[j][5] = points_ref0_j_l[j][2]
    for i in range(len(points_ref_i_j_l)):
        points_refi_j_l = points_ref_i_j_l[i]
        dep_station_k = deplacement_station_k(points_ref0_j_l, points_refi_j_l)
        for k in range(4):
            dep_station_i_k[i][k] = dep_station_k[k]
    return dep_station_i_k


def position_initiale_j_k(
        filepath_coor_init):  # Caculer la position initiale de l'ensemble des points d'étude --> Matrice 2D
    posi_init_j_k = np.zeros((nb_point_tot, 3))
    lines = [line.rstrip('\n') for line in
             open(filepath_coor_init)]  # -et le transeformer en une liste des listes des chaines de caractères
    for j in range(nb_point_tot):
        line = lines[j].split(':')
        if int(line[0][4:]) == j + 1:
            posi_initj_k = line[1].split(',')
            for k in range(3):
                posi_init_j_k[j][k] = float(posi_initj_k[k])
        else:
            print("Vérifier les coordonnées initiales!")
            sys.exit()
    return posi_init_j_k


def position_vs_station_i_j_k(dep_station_i_k,
                              points_etude_i_j_l):  # Caculer la position de l'ensemble des points d'étude par rapport
    posi_vs_station_i_j_k = np.zeros(
        (len(points_etude_i_j_l), nb_point_etude, 3))  # -à la station à l'instant i --> Matrice 3D
    for i in range(len(points_etude_i_j_l)):
        dep_stationi3 = dep_station_i_k[i][3]  # Angle de rotation de la station à l'instant i
        points_etudei_j_l = points_etude_i_j_l[i]
        for j in range(nb_point_etude):
            Hij0 = points_etudei_j_l[j][0]
            Vij1 = points_etudei_j_l[j][1]
            Dij2 = points_etudei_j_l[j][2]
            Hij0_DB = points_etudei_j_l[j][3]
            Vij1_DB = points_etudei_j_l[j][4]
            Dij2_DB = points_etudei_j_l[j][5]

            if sum([Hij0, Hij0_DB, Vij1, Vij1_DB, Dij2, Dij2_DB]) > 0:
                alpha = np.pi / 200
                posi_vs_station_i_j_k[i][j][0] = 0.5 * (
                            Dij2 * np.sin(alpha * Vij1) * np.sin(alpha * Hij0) + Dij2_DB * np.sin(
                        alpha * Vij1_DB) * np.sin(alpha * Hij0_DB)) + Dij2 * np.cos(alpha * Hij0) * np.sin(
                    alpha * Vij1) * dep_stationi3
                posi_vs_station_i_j_k[i][j][1] = 0.5 * (
                            Dij2 * np.sin(alpha * Vij1) * np.cos(alpha * Hij0) + Dij2_DB * np.sin(
                        alpha * Vij1_DB) * np.cos(alpha * Hij0_DB)) - Dij2 * np.sin(alpha * Hij0) * np.sin(
                    alpha * Vij1) * dep_stationi3
                posi_vs_station_i_j_k[i][j][2] = 0.5 * (Dij2 * np.cos(alpha * Vij1) + Dij2_DB * np.cos(alpha * Vij1_DB))
            else:
                posi_vs_station_i_j_k[i][j][0] = -99999
                posi_vs_station_i_j_k[i][j][1] = -99999
                posi_vs_station_i_j_k[i][j][2] = -99999
    return posi_vs_station_i_j_k


def position_i_j_k(dep_station_i_k,
                   points_etude_i_j_l):  # Calculer la position de l'ensemble des points d'étude à l'instant i -> Matrice 3D
    posi_i_j_k = np.zeros((len(dep_station_i_k), nb_point_etude, 3))
    posi_vs_station_i_j_k = position_vs_station_i_j_k(dep_station_i_k, points_etude_i_j_l)
    for i in range(len(posi_vs_station_i_j_k)):
        posi_stationi_k = dep_station_i_k[i]
        posi_vs_stationi_j_k = posi_vs_station_i_j_k[i]
        for j in range(nb_point_etude):
            posi_vs_stationij_k = posi_vs_stationi_j_k[j]
            for k in range(3):
                posi_vs_stationijk = posi_vs_stationij_k[k]
                posi_stationik = posi_stationi_k[k]
                if posi_vs_stationijk == -99999 or posi_stationik == -99999:
                    posi_i_j_k[i][j][k] = -99999
                else:
                    posi_i_j_k[i][j][k] = posi_vs_stationijk + posi_stationik
    return posi_i_j_k


def deplacement_relatif_i_j_k(dep_station_i_k, points_etude_i_j_l,
                              filepath_coor_init):  # Calculer le déplacement absolu de l'ensemble des points d'étude --> Matrice 3D
    dep_relatif_i_j_k = np.zeros((len(dep_station_i_k), nb_point_etude, 3))
    posi_init_j_k = position_initiale_j_k(filepath_coor_init)
    posi_i_j_k = position_i_j_k(dep_station_i_k, points_etude_i_j_l)
    for i in range(len(dep_station_i_k)):
        for j in range(nb_point_etude):
            for k in range(3):
                if posi_i_j_k[i][j][k] == -99999 or posi_init_j_k[posi_etude[j]][k] == -99999:
                    dep_relatif_i_j_k[i][j][k] = -99999
                else:
                    dep_relatif_i_j_k[i][j][k] = posi_i_j_k[i][j][k] - posi_init_j_k[posi_etude[j]][k]
    return dep_relatif_i_j_k


def ecrire_fichier(filepath):  # Ecrire le fichier de résultat de calcul
    l = lines(filepath, nb_point_tot, inst_init, inst_fin)
    p_ref_i_j_l = points_ref_i_j_l(l)
    p_etude_i_j_l = points_etude_i_j_l(l)
    t_visee_i = taux_visee_i(p_etude_i_j_l)
    dep_station_i_k = deplacement_station_i_k(p_ref_i_j_l, filepath_coor_init)
    posi_i_j_k = position_i_j_k(dep_station_i_k, p_etude_i_j_l)
    dep_relatif_i_j_k = deplacement_relatif_i_j_k(dep_station_i_k, p_etude_i_j_l, filepath_coor_init)

    liste2D = [[None for j in range(colonne_0 + 5 + 6 * nb_point_tot)] for i in range(len(l) + 1)]
    liste2D[0][0] = '"TIMESTAMP"'
    liste2D[0][1] = '"RECORD"'
    W0 = ["Temperature", "Pressure", "Humidity", "timerMesures", "TauxVisee", "TauxNonVisee", "LogOrientation",
          "StationTotal_X", "StationTotal_Xrelatif", "StationTotal_Y", "StationTotal_Yrelatif", "StationTotal_Z",
          "StationTotal_Zrelatif"]
    W1 = ["_X", "_Xrelatif", "_Y", "_Yrelatif", "_Z", "_Zrelatif"]
    W2 = '"' + nom + "_"
    W3 = "MPO_"

    colonne_0_out = 2 + len(W0)
    for m in range(len(W0)):
        liste2D[0][m + 2] = W2 + W0[m] + '"'
    for m in range(nb_point_tot):
        for n in range(6):
            liste2D[0][colonne_0_out + m * 6 + n] = W2 + W3 + "%0.3d" % (m + 1) + W1[n] + '"'

    for i in range(len(l)):
        li = l[i]
        for j in range(6):
            liste2D[i + 1][j] = li[j]
        liste2D[i + 1][6] = round(t_visee_i[i], ndigits=2)
        liste2D[i + 1][7] = round(100 - t_visee_i[i], ndigits=2)

        if dep_station_i_k[i][3] == -99999:
            liste2D[i + 1][8] = "NAN"
        else:
            liste2D[i + 1][8] = round((dep_station_i_k[i][3] * 200 / np.pi) % 400, ndigits=5)

        for k in range(3):
            if dep_station_i_k[i][k] == -99999:
                liste2D[i + 1][colonne_0_out - 6 + 2 * k] = "NAN"
                liste2D[i + 1][colonne_0_out - 5 + 2 * k] = "NAN"
            else:
                liste2D[i + 1][colonne_0_out - 6 + 2 * k] = round(dep_station_i_k[i][k], ndigits=5)
                liste2D[i + 1][colonne_0_out - 5 + 2 * k] = round(dep_station_i_k[i][k] * 1000, ndigits=5)

        for j in range(nb_point_ref):
            for m in range(6):
                liste2D[i + 1][colonne_0_out + posi_ref[j] * 6 + m] = "NAN"

        for j in range(nb_point_etude):
            for k in range(3):
                if posi_i_j_k[i][j][k] == -99999 or dep_relatif_i_j_k[i][j][k] == -99999:
                    liste2D[i + 1][colonne_0_out + posi_etude[j] * 6 + k * 2] = "NAN"
                    liste2D[i + 1][colonne_0_out + posi_etude[j] * 6 + k * 2 + 1] = "NAN"
                else:
                    liste2D[i + 1][colonne_0_out + posi_etude[j] * 6 + k * 2] = round(posi_i_j_k[i][j][k], ndigits=5)
                    liste2D[i + 1][colonne_0_out + posi_etude[j] * 6 + k * 2 + 1] = round(
                        dep_relatif_i_j_k[i][j][k] * 1000, ndigits=5)

    with open(nom + '_Resultat.dat', 'w', newline='') as file:
        writer = csv.writer(file, delimiter=',', quotechar="'", quoting=csv.QUOTE_MINIMAL)
        writer.writerow(
            ['"TOA5"', '"TEST2"', '"CR300"', '"15696"', '"CR300.Std.08.01"', '"CPU:TEST.CR300"',
             '"63891"', '"RawData"'])
        writer.writerows(liste2D)


ecrire_fichier(filepath)
