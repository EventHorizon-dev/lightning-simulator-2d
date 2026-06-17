import pygame
import random
import sys
pygame.init()
pygame.mixer.init()
#son_tonnerre=pygame.mixer.Sound("thunder3.mp3")#direct et bref
son_tonnerre=pygame.mixer.Sound("tonnerre.wav")#avec temps de retard
#son_tonnerre=pygame.mixer.Sound("tonnerre2.wav")#très cinématique, thriller


LARGEUR=800
HAUTEUR=600
fenetre = pygame.display.set_mode((LARGEUR, HAUTEUR), pygame.DOUBLEBUF | pygame.HWSURFACE)#créer la fenêtre

def generer_tronc():
    segments=[]#on crée la liste dans laquelle on va enregistrer nos segments
    x=400
    y=0
    while y < 600:#tant que l'éclair n'a pas atteint le bas de l'écran
        prochain_y=y+random.randint(5,15)#on calcule le point suivant vers le bas
        prochain_x = x + random.randint(-10, 10)#on calcule le point suivant sur la gauche ou la droite
        segments.append(((x, y), (prochain_x, prochain_y)))#on ajoute le segment qu'on vient de créer dans la liste
        if random.randint(1,100)<=5:
            nouvelle_branche=generer_branches(prochain_x, prochain_y)
            segments.extend(nouvelle_branche)
        x=prochain_x
        y=prochain_y
    return segments#on envoie la liste de tous les segments au reste programme

def generer_branches(x_depart,y_depart):
    segments_branches=[]
    x=x_depart
    y=y_depart
    y_maximum=y_depart+random.randint(40,180) #pour que la branche s'arrête au bout d'un moment
    poussee=random.choice([-8, 8])
    while y < y_maximum:
        prochain_y=y+random.randint(5, 15)
        prochain_x=x + random.randint(-10, 10)+poussee#pour que les branches zigzaguent plus que la principale
        segments_branches.append(((x, y), (prochain_x, prochain_y)))
        x=prochain_x
        y=prochain_y
    return segments_branches

temps_debut_flash = 0
duree_du_flash = 0
mon_eclair=generer_tronc()
doit_afficher=False#sert d'interrupteur

running=True
clock = pygame.time.Clock()
while running:



    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running=False
        elif event.type == pygame.KEYDOWN:#si l'événement est "appui sur une touche"
            if event.key == pygame.K_SPACE:#si l'événement est "appui sur la touche espace"
                mon_eclair=generer_tronc()
                doit_afficher=True
                temps_debut_flash = pygame.time.get_ticks()
                duree_du_flash = 500
                son_tonnerre.play()


    temps_actuel = pygame.time.get_ticks()

    if doit_afficher and (temps_actuel - temps_debut_flash < duree_du_flash):
        #fenetre.fill((160, 190, 230))
        fenetre.fill((110, 120, 170))
        #fenetre.fill((200, 215, 235))
        pass


    else:
        fenetre.fill((0,0,0))
        doit_afficher=False
        pass

    if doit_afficher:
        for segment in mon_eclair:
            pygame.draw.line(fenetre,(180, 210, 255),segment[0], segment[1], 2)#pour chaque segment, on dessine une ligne

    pygame.display.flip()

# 2. On fige le jeu pendant 50 millisecondes pour que l'œil voie le flash
    clock.tick(60)


pygame.quit()
sys.exit()#faire en sorte que la fenêtre reste et coder le bouton croix popur pouvoir quitter la fenêtre