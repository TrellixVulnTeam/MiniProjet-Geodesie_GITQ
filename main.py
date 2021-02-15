from geo_to_cartesiennes import *
from Ellepsoide_parametres import *
from probDirect_probIndirect import *
from Calcul_surface import *
from Calcul_latitudes import *
from longueur_arcs import *
from Cartesiennes_to_Geo import *
from Rayons_courbure import *
from principalPage1 import Ui_MainWindow
import sys
from PyQt5.QtWidgets import QMainWindow, QApplication
from math import *
import ast


class MyMainwindow:
    def __init__(self):
        self.main_win = QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.main_win)
        # write code(calling functions)
        # pour se deplacer entre les déffirentes pages a partir de la page d'accueil
        self.ui.stackedWidget.setCurrentWidget(self.ui.HP)

        self.ui.pushButton1_2.clicked.connect(self.showpage1_1)
        self.ui.pushButton1.clicked.connect(self.showpage1)
        self.ui.pushButton2.clicked.connect(self.showpage2)
        self.ui.pushButton2_2.clicked.connect(self.showpage3)

        self.ui.pushButton3.clicked.connect(self.showpage4)
        self.ui.pushButton4.clicked.connect(self.showpage5)
        self.ui.pushButton5.clicked.connect(self.showpage6)

        # code ajouté pour améliorer le front-end

        # La page d'accueil
        self.ui.pushButton1_2.setStyleSheet("border :5px solid ;"
                                            "border-top-color :purple; "
                                            "border-left-color :fuchsia;"
                                            "border-right-color :fuchsia;"
                                            "border-bottom-color : purple;"
                                            "background-color: aquamarine")
        self.ui.pushButton1.setStyleSheet("border :5px solid ;"
                                          "border-top-color :purple; "
                                          "border-left-color :fuchsia;"
                                          "border-right-color :fuchsia;"
                                          "border-bottom-color : purple;"
                                          "background-color:aquamarine")
        self.ui.pushButton2.setStyleSheet("border :5px solid ;"
                                          "border-top-color :purple; "
                                          "border-left-color :fuchsia;"
                                          "border-right-color :fuchsia;"
                                          "border-bottom-color : purple;"
                                          "background-color:aquamarine")
        self.ui.pushButton2_2.setStyleSheet("border :5px solid ;"
                                            "border-top-color :purple; "
                                            "border-left-color :fuchsia;"
                                            "border-right-color :fuchsia;"
                                            "border-bottom-color : purple;"
                                            "background-color: aquamarine")
        self.ui.pushButton3.setStyleSheet("border :5px solid ;"
                                          "border-top-color :purple; "
                                          "border-left-color :fuchsia;"
                                          "border-right-color :fuchsia;"
                                          "border-bottom-color : purple;"
                                          "background-color: aquamarine")
        self.ui.pushButton4.setStyleSheet("border :5px solid ;"
                                          "border-top-color :purple; "
                                          "border-left-color :fuchsia;"
                                          "border-right-color :fuchsia;"
                                          "border-bottom-color : purple;"
                                          "background-color: aquamarine")
        self.ui.pushButton5.setStyleSheet("border :5px solid ;"
                                          "border-top-color :purple; "
                                          "border-left-color :fuchsia;"
                                          "border-right-color :fuchsia;"
                                          "border-bottom-color : purple;"
                                          "background-color: aquamarine")

        self.ui.PB_hp2_2.setStyleSheet(
            "selection-background-color: blue;border-width:0;border-style:outset")
        self.ui.PB_hp1.setStyleSheet(
            "selection-background-color: blue;border-width:0;border-style:outset")
        self.ui.PB_hp2.setStyleSheet(
            "selection-background-color: blue;border-width:0;border-style:outset")
        self.ui.PB_hp3.setStyleSheet(
            "selection-background-color: blue;border-width:0;border-style:outset")

        self.ui.PB_hp4_2.setStyleSheet(
            "selection-background-color: blue;border-width:0;border-style:outset")
        self.ui.PB_hp5.setStyleSheet(
            "selection-background-color: blue;border-width:0;border-style:outset")
        self.ui.PB_hp6.setStyleSheet(
            "selection-background-color: blue;border-width:0;border-style:outset")
        self.ui.PB_hp7.setStyleSheet(
            "selection-background-color: blue;border-width:0;border-style:outset")
        self.ui.PB_hp8.setStyleSheet(
            "selection-background-color: blue;border-width:0;border-style:outset")
        self.ui.PB_hp9.setStyleSheet(
            "selection-background-color: blue;border-width:0;border-style:outset")

        # ****************************************
        # La page du parametres de l'éllipsoide
        self.ui.cond1.setStyleSheet(
            "color: red; selection-background-color: blue;border-width:0;border-style:outset")
        self.ui.PB_parameters.setStyleSheet("border :5px solid ;"
                                            "border-top-color : red; "
                                            "border-left-color :yellow;"
                                            "border-right-color :yellow;"
                                            "border-bottom-color : red;"
                                            "background-color: lime")
        self.ui.label_29.setStyleSheet("border-color: black")
        # ***********************************

        # La page de transformations de coordonnées
        self.ui.cond2.setStyleSheet(
            "color: red; selection-background-color: blue;border-width:0;border-style:outset")

        self.ui.cond3.setStyleSheet(
            "color: red; selection-background-color: blue;border-width:0;border-style:outset")
        self.ui.PB_trans2.setStyleSheet("border :5px solid ;"
                                        "border-top-color : red; "
                                        "border-left-color :yellow;"
                                        "border-right-color :yellow;"
                                        "border-bottom-color : red;"
                                        "background-color: lime")
        self.ui.PB_trans1.setStyleSheet("border :5px solid ;"
                                        "border-top-color : red; "
                                        "border-left-color :yellow;"
                                        "border-right-color :yellow;"
                                        "border-bottom-color : red;"
                                        "background-color: lime")
        # **************************************
        # La page de rayons de courbures
        self.ui.cond4.setStyleSheet(
            "color: red; selection-background-color: blue;border-width:0;border-style:outset")
        self.ui.PB_rayon.setStyleSheet("border :5px solid ;"
                                       "border-top-color : red; "
                                       "border-left-color :yellow;"
                                       "border-right-color :yellow;"
                                       "border-bottom-color : red;"
                                       "background-color: lime")
        # **************************************
        # La page de latitudes

        self.ui.cond6.setStyleSheet(
            "color: red; selection-background-color: blue;border-width:0;border-style:outset")

        self.ui.PB_beta_phi.setStyleSheet("border :5px solid ;"
                                          "border-top-color : red; "
                                          "border-left-color :yellow;"
                                          "border-right-color :yellow;"
                                          "border-bottom-color : red;"
                                          "background-color: lime")
        self.ui.PB_beta_psi.setStyleSheet("border :5px solid ;"
                                          "border-top-color : red; "
                                          "border-left-color :yellow;"
                                          "border-right-color :yellow;"
                                          "border-bottom-color : red;"
                                          "background-color: lime")
        self.ui.PB_psi_phi.setStyleSheet("border :5px solid ;"
                                         "border-top-color : red; "
                                         "border-left-color :yellow;"
                                         "border-right-color :yellow;"
                                         "border-bottom-color : red;"
                                         "background-color: lime")
        # ***************************************
        # La page de longuers d'arcs
        self.ui.cond7.setStyleSheet(
            "color: red; selection-background-color: blue;border-width:0;border-style:outset")

        self.ui.cond8.setStyleSheet(
            "color: red; selection-background-color: blue;border-width:0;border-style:outset")
        self.ui.PB_arc_parallele.setStyleSheet("border :5px solid ;"
                                               "border-top-color : red; "
                                               "border-left-color :yellow;"
                                               "border-right-color :yellow;"
                                               "border-bottom-color : red;"
                                               "background-color: lime")
        self.ui.PB_arc_meridien.setStyleSheet("border :5px solid ;"
                                              "border-top-color : red; "
                                              "border-left-color :yellow;"
                                              "border-right-color :yellow;"
                                              "border-bottom-color : red;"
                                              "background-color: lime")
        # ****************************************

        # La page du probleme direct et indirect
        self.ui.cond9.setStyleSheet(
            "color: red; selection-background-color: blue;border-width:0;border-style:outset")

        self.ui.cond10.setStyleSheet(
            "color: red; selection-background-color: blue;border-width:0;border-style:outset")
        self.ui.PB_probDirect.setStyleSheet("border :5px solid ;"
                                            "border-top-color : red; "
                                            "border-left-color :yellow;"
                                            "border-right-color :yellow;"
                                            "border-bottom-color : red;"
                                            "background-color: lime")
        self.ui.PB_probIndirect.setStyleSheet("border :5px solid ;"
                                              "border-top-color : red; "
                                              "border-left-color :yellow;"
                                              "border-right-color :yellow;"
                                              "border-bottom-color : red;"
                                              "background-color: lime")
        self.ui.label_121.setStyleSheet("border :5px solid ;"
                                        "border-top-color : purple; "
                                        "border-left-color :fuchsia;"
                                        "border-right-color :fuchsia;"
                                        "border-bottom-color : purple;")
        self.ui.label_130.setStyleSheet("border :5px solid ;"
                                        "border-top-color : purple; "
                                        "border-left-color :fuchsia;"
                                        "border-right-color :fuchsia;"
                                        "border-bottom-color : purple;")
        # *****************************************

        # La page du calcul de surface
        self.ui.cond11.setStyleSheet(
            "color: red; selection-background-color: blue;border-width:0;border-style:outset")
        self.ui.PB_surface.setStyleSheet("border :5px solid ;"
                                         "border-top-color : red; "
                                         "border-left-color :yellow;"
                                         "border-right-color :yellow;"
                                         "border-bottom-color : red;"
                                         "background-color: lime")
        # ******************************************
        # La fin du code ajouté pour améliorer le front-end

        # les lignes suivantes pour retourner a la page d'accueil a partir d'autres pages
        self.ui.PB_hp2_2.clicked.connect(self.show_hp)

        self.ui.PB_hp1.clicked.connect(self.show_hp)
        self.ui.PB_hp2.clicked.connect(self.show_hp)
        self.ui.PB_hp3.clicked.connect(self.show_hp)
        #self.ui.PB_hp4.clicked.connect(self.show_hp)
        self.ui.PB_hp4_2.clicked.connect(self.show_hp)
        self.ui.PB_hp5.clicked.connect(self.show_hp)
        self.ui.PB_hp6.clicked.connect(self.show_hp)
        self.ui.PB_hp7.clicked.connect(self.show_hp)
        self.ui.PB_hp8.clicked.connect(self.show_hp)
        self.ui.PB_hp9.clicked.connect(self.show_hp)
        # self.ui.PB_hp10.clicked.connect(self.show_hp)

        # pour lier le botton avec la fonction qui permet de calculer les parametres de l'ellipsoide
        self.ui.PB_parameters.clicked.connect(self.parametres_ellepsoide)
        # *******************************************************************************************

        # pour lier le botton convertir avec les fonctions
        self.ui.PB_trans1.clicked.connect(self.trans1)
        self.ui.PB_trans2.clicked.connect(self.trans2)
        # ************************************************

        # pour lier le botton avec la fonction qui calcule le rayon de courbure
        self.ui.PB_rayon.clicked.connect(self.rayon_courbure)
        # **********************************************************************

        # Pour lier le botton avec la fct qui calcule les latitudes
        #self.ui.PB_latitude.clicked.connect(self.calculate_latitudes)
        self.ui.PB_beta_psi.clicked.connect(self.calculate_beta_psi)
        self.ui.PB_beta_phi.clicked.connect(self.calculate_beta_phi)
        self.ui.PB_psi_phi.clicked.connect(self.calculate_psi_phi)
        # **********************************************************

        # pour lier le botton avec les fcts qui calculent les longueurs d'arcs
        self.ui.PB_arc_meridien.clicked.connect(self.arc_meridien)
        self.ui.PB_arc_parallele.clicked.connect(self.arc_parallele)
        # ********************************************************************

        # Pour lier le botton avec la fct qui calcule la surface
        self.ui.PB_surface.clicked.connect(self.calcul_surface)
        # *******************************************************

        # Pour lier le botton avec la fct qui calcule le probleme direct
        self.ui.PB_probDirect.clicked.connect(self.probleme_direct)
        # ***************************************************************

        # Pour lier le botton avec la fct qui calcule le probleme indirect
        self.ui.PB_probIndirect.clicked.connect(self.probleme_indirect)
        # *****************************************************************
        # end of code(calling functions)

    def show(self):
        self.main_win.show()

    # start code (fonctions)
    # ici on définit les fonctions de déplacements
    def showpage1_1(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.page1_1)

    def showpage1(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.page_1)

    def showpage2(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.page_2)

    def showpage3(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.page_3)

    def showpage4(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.page_4)

    def showpage5(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.page_5)

    def showpage6(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.page_6)

    def backto_hp(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.HP)

    # on va creer une fonction pour retourner a la page d'accueil
    def show_hp(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.HP)

    # end of code(functions)

    # ****************************input functios********************************

    # Transformations des coordonnees cartésiennes vers les coordonnees géographiques
    def trans1(self):
        self.ui.cond2.setText('')
        if (len(self.ui.a_trans1.text()) == 0 or len(self.ui.f_trans1.text()) == 0 or len(self.ui.X_trans1.text()) == 0
                or len(self.ui.a_trans1.text()) == 0 or len(self.ui.a_trans1.text()) == 0
                or len(self.ui.Z_trans1.text()) == 0 or len(self.ui.epsilon_trans1.text()) == 0):

            self.ui.cond2.setText("Il faut remplir tous les champs!")
        else:
            inv_f = ast.literal_eval(self.ui.f_trans1.text())
            a = ast.literal_eval(self.ui.a_trans1.text())
            x = ast.literal_eval(self.ui.X_trans1.text())
            y = ast.literal_eval(self.ui.Y_trans1.text())
            z = ast.literal_eval(self.ui.Z_trans1.text())
            epsilon = ast.literal_eval(self.ui.epsilon_trans1.text())
            # cartesian2geo(x, y, z, a, inv_f)
            phi, lam, h = cartesian2geo(x, y, z, a, inv_f, epsilon)
            self.ui.phi_trans1.setText(str(round(phi, 6)))
            self.ui.lam_tran1.setText(str(round(lam, 6)))
            self.ui.h_trans1.setText(str(round(h, 6)))

    def trans2(self):
        self.ui.cond3.setText('')
        if (len(self.ui.a_trans2.text()) == 0 or len(self.ui.f_trans2.text()) == 0
                or len(self.ui.phi_trans2.text()) == 0 or len(self.ui.lam_trans2.text()) == 0
                or len(self.ui.h_trans2.text()) == 0):
            self.ui.cond3.setText("Il faut remplir tous les champs!")
        else:
            inv_f = ast.literal_eval(self.ui.f_trans2.text())
            a = ast.literal_eval(self.ui.a_trans2.text())
            phi = ast.literal_eval(self.ui.phi_trans2.text())
            lam = ast.literal_eval(self.ui.lam_trans2.text())
            h = ast.literal_eval(self.ui.h_trans2.text())
            x, y, z = Geo2Cartesian(phi, lam, h, a, inv_f)
            self.ui.x_trans2.setText(str(round(x, 6)))
            self.ui.y_trans2.setText(str(round(y, 6)))
            self.ui.z_trans2.setText(str(round(z, 6)))

    def rayon_courbure(self):
        self.ui.cond4.setText('')
        if (len(self.ui.a_rayon.text()) == 0 or len(self.ui.invf_rayon.text()) == 0 or len(
                self.ui.phi_rayon.text()) == 0
                or len(self.ui.alpha_rayon.text()) == 0):
            self.ui.cond4.setText("Il faut remplir tous les champs!")
        else:
            inv_f = ast.literal_eval(self.ui.invf_rayon.text())
            a = ast.literal_eval(self.ui.a_rayon.text())
            phi = ast.literal_eval(self.ui.phi_rayon.text())
            alpha = ast.literal_eval(self.ui.alpha_rayon.text())
            m, n, r_alpha = curvature_radius(a, inv_f, phi, alpha)
            # r_alpha = rayon_alpha(m, n, alpha)
            self.ui.M_rayon.setText(str(round(m, 6)))
            self.ui.N_rayon.setText(str(round(n, 6)))
            self.ui.Ralpha_rayon.setText(str(round(r_alpha, 10)))

    def parametres_ellepsoide(self):

        self.ui.cond1.setText('')
        if len(self.ui.a_parametres.text()) == 0 or len(self.ui.invf_parametres.text()) == 0:
            self.ui.cond1.setText("Il faut remplir tous les champs!")
        else:
            inv_f = ast.literal_eval(self.ui.invf_parametres.text())
            a = ast.literal_eval(self.ui.a_parametres.text())

            e_squared, e_prime_squared, alpha, c, b = ellipsoid_parameters_all(a, inv_f)
            self.ui.e_squared.setText(str(round(e_squared, 4)))
            self.ui.e_prime_squared.setText(str(round(e_prime_squared, 4)))
            self.ui.alpha.setText(str(round(alpha, 4)))
            self.ui.c_pole.setText(str(round(c, 4)))
            self.ui.b_parameters.setText(str(round(b, 4)))

    def calculate_beta_psi(self):

        self.ui.cond6.setText('')
        if len(self.ui.a_1.text()) == 0 or len(self.ui.invf_1.text()) == 0 \
                or len(self.ui.phi_1.text()) == 0:
            self.ui.cond6.setText("Il faut remplir tous les champs nécessaires!")
        else:
            inv_f = ast.literal_eval(self.ui.invf_1.text())
            a = ast.literal_eval(self.ui.a_1.text())
            phi = ast.literal_eval(self.ui.phi_1.text())
            beta, psi = calculate_psi_beta(a, inv_f, phi)
            self.ui.beta_1.setText(str(round(beta, 6)))
            self.ui.psi_1.setText(str(round(psi, 6)))

    def calculate_beta_phi(self):
        self.ui.cond6.setText('')
        if len(self.ui.a_1.text()) == 0 or len(self.ui.invf_1.text()) == 0 \
                or len(self.ui.psi_2.text()) == 0:
            self.ui.cond6.setText("Il faut remplir tous les champs nécessaires!")
        else:
            inv_f = ast.literal_eval(self.ui.invf_1.text())
            a = ast.literal_eval(self.ui.a_1.text())
            psi = ast.literal_eval(self.ui.psi_2.text())
            phi, beta = calculate_beta_phi(a, inv_f, psi)
            self.ui.beta_2.setText(str(round(beta, 6)))
            self.ui.phi_2.setText(str(round(phi, 6)))

    def calculate_psi_phi(self):
        self.ui.cond6.setText('')
        if len(self.ui.a_1.text()) == 0 or len(self.ui.invf_1.text()) == 0 \
                or len(self.ui.beta_3.text()) == 0:
            self.ui.cond6.setText("Il faut remplir tous les champs nécessaires!")
        else:
            inv_f = ast.literal_eval(self.ui.invf_1.text())
            a = ast.literal_eval(self.ui.a_1.text())
            beta = ast.literal_eval(self.ui.beta_3.text())
            phi, psi = calculate_phi_psi(a, inv_f, beta)
            self.ui.phi_3.setText(str(round(phi, 6)))
            self.ui.psi_3.setText(str(round(psi, 6)))

    def arc_meridien(self):
        self.ui.cond7.setText('')
        if len(self.ui.a_arc_meridien.text()) == 0 or len(self.ui.invf_arc_meridien.text()) == 0 \
                or len(self.ui.phi1_arc_meridien.text()) == 0 or len(self.ui.phi2_arc_meridien.text()) == 0:
            self.ui.cond7.setText("Il faut remplir tous les champs nécessaires!")
        else:
            inv_f = ast.literal_eval(self.ui.invf_arc_meridien.text())
            a = ast.literal_eval(self.ui.a_arc_meridien.text())
            phi1 = ast.literal_eval(self.ui.phi1_arc_meridien.text())
            phi2 = ast.literal_eval(self.ui.phi2_arc_meridien.text())
            s = long_arc_meridian(phi1, phi2, a, inv_f)
            self.ui.arc_meridien.setText(str(round(s, 6)))

    def arc_parallele(self):
        self.ui.cond8.setText('')
        if len(self.ui.a_arc_para.text()) == 0 or len(self.ui.invf_arc_para.text()) == 0 \
                or len(self.ui.lam1_arc_para.text()) == 0 or len(self.ui.lam2_arc_para.text()) == 0 \
                or len(self.ui.phi_arc_para.text()) == 0:
            self.ui.cond8.setText("Il faut remplir tous les champs nécessaires!")
        else:
            inv_f = ast.literal_eval(self.ui.invf_arc_para.text())
            a = ast.literal_eval(self.ui.a_arc_para.text())
            lam1 = ast.literal_eval(self.ui.lam1_arc_para.text())
            lam2 = ast.literal_eval(self.ui.lam2_arc_para.text())
            phi = ast.literal_eval(self.ui.phi_arc_para.text())
            l = long_arc_parallele(phi, lam1, lam2, a, inv_f)
            self.ui.arc_parallele.setText(str(round(l, 6)))

    def calcul_surface(self):
        self.ui.cond11.setText('')
        if len(self.ui.a_surface.text()) == 0 or len(self.ui.invf_surface.text()) == 0 \
                or len(self.ui.lam1_surface.text()) == 0 or len(self.ui.lam2_surface.text()) == 0 \
                or len(self.ui.phi1_surface.text()) == 0 or len(self.ui.phi2_surface.text()) == 0:
            self.ui.cond11.setText("Il faut remplir tous les champs nécessaires!")
        else:
            inv_f = ast.literal_eval(self.ui.invf_surface.text())
            a = ast.literal_eval(self.ui.a_surface.text())
            lam1 = ast.literal_eval(self.ui.lam1_surface.text())
            lam2 = ast.literal_eval(self.ui.lam2_surface.text())
            phi1 = ast.literal_eval(self.ui.phi1_surface.text())
            phi2 = ast.literal_eval(self.ui.phi2_surface.text())
            s = calculate_area(lam1, lam2, phi1, phi2, a, inv_f)
            self.ui.s_surface.setText(str(round(s, 6)))

    def probleme_direct(self):
        self.ui.cond9.setText('')
        if len(self.ui.A12_pd.text()) == 0 or len(self.ui.R_pd.text()) == 0 \
                or len(self.ui.S_pd.text()) == 0 or len(self.ui.lam1_pd.text()) == 0 \
                or len(self.ui.phi1_pd.text()) == 0:
            self.ui.cond9.setText("Il faut remplir tous les champs nécessaires!")
        else:
            a12 = ast.literal_eval(self.ui.A12_pd.text())
            r = ast.literal_eval(self.ui.R_pd.text())
            s = ast.literal_eval(self.ui.S_pd.text())
            lam1 = ast.literal_eval(self.ui.lam1_pd.text())
            phi1 = ast.literal_eval(self.ui.phi1_pd.text())
            phi2, lam2, a21 = prob_direct(phi1, lam1, a12, s, r)
            self.ui.A21_pd.setText(str(round(a21, 4)))
            self.ui.lam2_pd.setText(str(round(lam2, 4)))
            self.ui.phi2_pd.setText(str(round(phi2, 4)))

    def probleme_indirect(self):
        self.ui.cond10.setText('')
        if len(self.ui.lam1_pi.text()) == 0 or len(self.ui.phi1_pi.text()) == 0 \
                or len(self.ui.lam2_pi.text()) == 0 or len(self.ui.phi2_pi.text()) == 0 \
                or len(self.ui.R_pi.text()) == 0:
            self.ui.cond10.setText("Il faut remplir tous les champs nécessaires!")
        else:
            lam1 = ast.literal_eval(self.ui.lam1_pi.text())
            phi1 = ast.literal_eval(self.ui.phi1_pi.text())
            lam2 = ast.literal_eval(self.ui.lam2_pi.text())
            phi2 = ast.literal_eval(self.ui.phi2_pi.text())
            r = ast.literal_eval(self.ui.R_pi.text())
            s, a12, a21 = prob_indirect(phi1, phi2, lam1, lam2, r)
            self.ui.S12_pi.setText(str(round(s, 4)))
            self.ui.A12_pi.setText(str(round(a12, 4)))
            self.ui.A21_pi.setText(str(round(a21, 4)))

    # ******************************************************************************


if __name__ == '__main__':
    app = QApplication(sys.argv)
    myWin = MyMainwindow()
    myWin.show()
    sys.exc_info()
    app.exec_()

