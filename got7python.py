import pygame
import random
import sys
import cv2
import math

# #########################################################################################
#                                                                                         #
#           GOT7 INSPIRED WINTER HEPTAGON GAME MADE BY CHOLORSPLASH                       #
#                                                                                         #
# #########################################################################################

"""
=====================================================
                      GAME CREDITS
=====================================================

Created by: Cholorsplash
Date: JANUARY 17/01/2025

Assets (characters, backgrounds, design): Entirely created by Cholorsplash.

Audio:
- The game sounds were mixed by Cholorsplash.
- Some music/sound effects are based on works by GOT7. These sounds are used solely for entertainment purposes and are non-commercial.

Purpose of the game:
This game was designed to entertain players. It is a personal, non-commercial project.
Always credit the creator when using the game


=====================================================
                     COPYRIGHT
=====================================================

This game and its assets (characters, sounds, backgrounds, etc.) are the property of Cholorsplash. 
Any reproduction, modification, or use without permission is prohibited.

The sounds inspired by GOT7 remain under the original copyright of their respective creators.
No financial profit is made from this project.

=====================================================
"""

## ////////////////////////// DEBUT DU CODE

# Initialize Pygame
pygame.init()

# ----------------------

# Video Introductif 
# Pour skip la video il faut appuyer sur [echap]

def jouer_video(video_path, audio_path):
    """Joue une vidéo avec son avant de démarrer le jeu."""
    # Charger la vidéo avec OpenCV
    cap = cv2.VideoCapture(video_path)
    if not cap.isOpened():
        print("Erreur : Impossible de lire la vidéo.")
        return

    # Charger le son avec pygame.mixer
    pygame.mixer.init()
    pygame.mixer.music.load(audio_path)
    pygame.mixer.music.play()

    # Jouer la vidéo
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:  # Fin de la vidéo
            break

        # Convertir les couleurs de BGR (OpenCV) à RGB (Pygame)
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        # Convertir l'image OpenCV en surface Pygame
        frame_surface = pygame.surfarray.make_surface(frame)
        frame_surface = pygame.transform.rotate(frame_surface, -90)  # Ajustement de l'orientation

        # Ajuster l'orientation de la vidéo si nécessaire
        frame_surface = pygame.transform.scale(frame_surface, (SCREEN_WIDTH, SCREEN_HEIGHT))
        frame_surface = pygame.transform.flip(frame_surface, True, False)  # Flip horizontalement

        # Afficher l'image dans Pygame
        screen.blit(frame_surface, (0, 0))
        pygame.display.flip()

        # Quitter la vidéo si l'utilisateur appuie sur Échap
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                cap.release()
                pygame.mixer.music.stop()
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                cap.release()
                pygame.mixer.music.stop()
                return

        pygame.time.Clock().tick(3000)  # Contrôler la fréquence d'images (3000 fps)

    # Fin de la vidéo, arrêter la musique
    cap.release()
    pygame.mixer.music.stop()


# ----------------------

# Menu principal

def menu_principal():
    """Affiche le menu principal avant de démarrer le jeu."""
    game_theme.set_volume(0.1)
    game_theme.play()
    while True:
        # screen.fill((255, 255, 255))  # Fond blanc
        screen.blit(menu, (0, 0))  # Optionnel : Afficher une image de fond
        
        # Afficher le titre
        font = pygame.font.Font(None, 72)
        # title_text = font.render("GOT7 Game", True, (0, 0, 0))
        #screen.blit(title_text, (SCREEN_WIDTH // 2 - title_text.get_width() // 2, 150))

        # Afficher les options du menu
        font_small = pygame.font.Font(None, 48)
        # play_text = font_small.render("Appuyez sur [Entrée] pour jouer", True, (0, 0, 0))
        # quit_text = font_small.render("Appuyez sur [Echap] pour quitter", True, (0, 0, 0))
        #screen.blit(play_text, (SCREEN_WIDTH // 2 - play_text.get_width() // 2, 300))
        #screen.blit(quit_text, (SCREEN_WIDTH // 2 - quit_text.get_width() // 2, 400))

        # Gestion des événements
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:  # Touche Entrée
                    return choisir_personnage() # Quitte le menu pour démarrer le jeu
                if event.key == pygame.K_ESCAPE:  # Touche Échap
                    pygame.quit()
                    sys.exit()

        pygame.display.flip()


# ----------------------

# Config Screen

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("GOT7 game : Title Track Python")

winter_back = pygame.image.load('back-winter-version.png')
winter_back = pygame.transform.scale(winter_back, (SCREEN_WIDTH, SCREEN_HEIGHT))

# menu principal 
menu = pygame.image.load('menuprinc.png')
menu = pygame.transform.scale(menu, (SCREEN_WIDTH, SCREEN_HEIGHT))

# ----------------------

# Load sounds
game_theme = pygame.mixer.Sound("eclipse8bit.wav")
level_up_sound_30 = pygame.mixer.Sound("easy_level.wav")
poison_hit_sound = pygame.mixer.Sound("namja(1).wav")
booster_hit_sound = pygame.mixer.Sound("fly(1).wav")
booster_hit_sound.set_volume(0.4)
game_over_sound = pygame.mixer.Sound("out.wav")
game_over_sound.set_volume(1.0)
heptagon_collect = pygame.mixer.Sound("coins.wav")
heptagon_collect.set_volume(0.3)
live_hit_sound = pygame.mixer.Sound("hardcarry(1).wav")
slow_hit_sound = pygame.mixer.Sound("palapapa.wav")

# --

ahgase_twit = pygame.mixer.Sound("twitter(1).wav")
jb = pygame.mixer.Sound("darling.wav")
mk = pygame.mixer.Sound("outofthedoor.wav")
js = pygame.mixer.Sound("smooth.wav")
jy = pygame.mixer.Sound("her.wav")
yj = pygame.mixer.Sound("yj.wav")
bb = pygame.mixer.Sound("tidalwave.wav")
yg = pygame.mixer.Sound("yg.wav")



# ----------------------

# choix les personnages 

def choisir_personnage():
    """Affiche l'écran de sélection de personnage et retourne le choix du joueur."""
    menu_choix = pygame.image.load("menuchoix.png")
    menu_choix = pygame.transform.scale(menu_choix, (SCREEN_WIDTH, SCREEN_HEIGHT))  # Adapter à la taille de l'écran


    # Charger les images des personnages
    # ahgase
    ahgase = pygame.image.load('ahgase-python.png')
    ahgase = pygame.transform.scale(ahgase,(60,60))

    # got7 members
    # jayb
    jayb = pygame.image.load('jayb2.png')
    jayb = pygame.transform.scale(jayb, (60, 60))

    # mark
    mark = pygame.image.load('mark.png')
    mark = pygame.transform.scale(mark, (60, 60))

    # mark
    jackson = pygame.image.load('jackson.png')
    jackson = pygame.transform.scale(jackson, (60, 60))

    # mark
    jinyoung = pygame.image.load('jinyoung.png')
    jinyoung = pygame.transform.scale(jinyoung, (60, 60))

    # mark
    ars = pygame.image.load('ars.png')
    ars = pygame.transform.scale(ars, (60, 60))

    # bambam
    bambam = pygame.image.load('bam.png')
    bambam = pygame.transform.scale(bambam, (60, 60))

    # yugyeom
    yugyeom = pygame.image.load('yugyeom.png')
    yugyeom = pygame.transform.scale(yugyeom, (60, 60))

    # Positions des personnages à l'écran
    # Positions fixes des personnages (comme dans l'image fournie)
    pos_jayb = (165, 310)    # Position de JayB
    pos_mark = (300, 310)    # Position de Mark
    pos_jackson = (400, 310) # Position de Jackson
    pos_jinyoung = (510, 310) # Position de Jinyoung
    pos_ars = (165, 460)     # Position de Youngjae
    pos_bambam = (300, 460)  # Position de Bambam
    pos_yugyeom = (400, 460) # Position de Yugyeom
    pos_ahgase = (510, 460)  # Position d'Ahgase

    choix = None  # Stockera le choix du joueur

    while choix is None:
        screen.blit(menu_choix, (0, 0))  # Fond blanc

        # Afficher les personnages
        screen.blit(jayb, pos_jayb)
        screen.blit(mark, pos_mark)
        screen.blit(jackson, pos_jackson)
        screen.blit(jinyoung, pos_jinyoung)
        screen.blit(ars, pos_ars)
        screen.blit(bambam, pos_bambam)
        screen.blit(yugyeom, pos_yugyeom)
        screen.blit(ahgase, pos_ahgase)

        # Vérifier les événements
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    choix = jayb
                    jb.play()
                elif event.key == pygame.K_2:
                    choix = mark
                    mk.play()
                elif event.key == pygame.K_3:
                    choix = jackson
                    js.play()
                elif event.key == pygame.K_4:
                    choix = jinyoung
                    jy.play()
                elif event.key == pygame.K_5:
                    choix = ars
                    yj.play()
                elif event.key == pygame.K_6:
                    choix = bambam
                    bb.play()
                elif event.key == pygame.K_7:
                    choix = yugyeom
                    yg.play()
                elif event.key == pygame.K_8:
                    choix = ahgase
                    ahgase_twit.play()

        # Mettre à jour l'écran
        pygame.display.flip()

    return choix  # Retourne l'image du personnage choisi

# ----------------------

# les notes de musique

note_color = (40, 169, 40) # vert foncé
note_width = 15
note_height = 15
# note_speed = 2

notes = []

# Notes empoisonées
poison_note_color = (255, 0, 0) # rouge
poison_notes = []

# Notes booster
booster_note_color = (0, 0, 255) # bleu
booster_notes = []

# Notes booster vie
live_note_color = (252, 126, 206) # couleur
live_notes = []

# Notes booster slow
def get_multicolor_color():
    """Renvoie une couleur changeante dynamiquement pour créer un effet arc-en-ciel."""
    time = pygame.time.get_ticks() / 1000  # Temps en secondes (évolue en continu)
    cycle_speed = 2  # Contrôle la vitesse du changement de couleur (augmente pour ralentir)

    # Cycle sinusoidal pour l'effet arc-en-ciel
    red = int((math.sin(time * cycle_speed) + 1) * 127.5)
    green = int((math.sin(time * cycle_speed + 2 * math.pi / 3) + 1) * 127.5)
    blue = int((math.sin(time * cycle_speed + 4 * math.pi / 3) + 1) * 127.5)
    return (red, green, blue)

slow_notes = []


def generate_note():
    x = random.randint(0, SCREEN_WIDTH - note_width)
    y = 0
    return [x, y]

# ----------------------

## Sauvegarde des scores

def save_score(score):
    """Sauvegarde le score dans un fichier texte."""
    with open("scores.txt", "a") as file:
        file.write(f"{score}\n")

def get_top_scores():
    """Récupère les meilleurs scores depuis le fichier texte."""
    try:
        with open("scores.txt", "r") as file:
            scores = [int(line.strip()) for line in file.readlines()]
        scores.sort(reverse=True)
        return scores[:3]  # Retourne les 5 meilleurs scores
    except FileNotFoundError:
        return []

def display_top_scores():
    """Affiche les meilleurs scores à l'écran."""
    top_scores = get_top_scores()
    font = pygame.font.Font(None, 36)
    y_offset = SCREEN_HEIGHT // 2 + 115
    for i, score in enumerate(top_scores):
        score_text = font.render(f"{i + 1}. {score}", True, (0, 0, 0))
        screen.blit(score_text, (SCREEN_WIDTH // 2 - score_text.get_width() // 2, y_offset))
        y_offset += 40

# ----------------------

# boucle principale

# -------------

# la difficulté du jeu

level = 1
score_per_level = 20

NOTE_FREQUENCY = 90
POISON_NOTE_FREQUENCY = 200
BOOSTER_NOTE_FREQUENCY = 300
SLOW_NOTE_FREQUENCY = 400
slow_effect_time = 0
poison_speed = 3

def adjust_speed(score):
    """Ajuste la vitesse des notes et des notes empoisonnées en fonction du score."""
    global slow_effect_time
    base_freq = NOTE_FREQUENCY
    max_speed = 1 
    increment_per_level = 1

    # on ralenti le jeu si le booster slow est actif
    if slow_effect_time > 0:
        slow_effect_time -= 1
        current_max_speed = max_speed + (score // score_per_level) * increment_per_level
        return current_max_speed - 1

    return max_speed + (score // score_per_level) * increment_per_level

def adjust_frequency(level):
    """Ajuste la fréquence des notes et des notes empoisonnées en fonction du niveau."""
    global NOTE_FREQUENCY, POISON_NOTE_FREQUENCY
    if level >= 3:
        NOTE_FREQUENCY = max(5, 100 // (level - 2))  # Augmente la fréquence des notes normales
        POISON_NOTE_FREQUENCY = max(10, 200 // (level - 2))  # Augmente la fréquence des notes empoisonnées


def check_level(score):
    """ met a jour le niveau par palier de 10 """
    global level
    new_level = (score // score_per_level) + 1
    if new_level > level:
        level_up_sound_30.play()
    level = new_level

def update_notes(notes, poison_notes):
    global note_speed
    note_speed = adjust_speed(score)
    for note in notes:
        note[1] += note_speed
    for poison_note in poison_notes:
        poison_note[1] += note_speed
    return notes, poison_notes

def update_booster_notes(booster_notes):
    """Met à jour les positions des notes booster."""
    for note in booster_notes:
        note[1] += 8  # Vitesse élevée pour les notes booster
    return [note for note in booster_notes if note[1] < SCREEN_HEIGHT]  # Garder les notes à l'écran


# ----------------------


lives = 3 # nombre de vies

# on joue la video d'introduction

jouer_video("intro-video.mp4", "intro-video.mp3")
perso_choisi = menu_principal() # choix du personnage parmis les membres de GOT7


# ----------------------

# le personnage

# Green = (0, 255, 0)

snake_width = 20
snake_height = 20
snake_x = SCREEN_WIDTH // 2
snake_y = SCREEN_HEIGHT - perso_choisi.get_height()
# snake_y = SCREEN_HEIGHT - ahgase.get_height()
# pygame.draw.rect(screen, Green, (snake_x, snake_y, snake_width, snake_height))

# ----------------------

# le control du personnage

def controlkey(x):
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        x -= 5
    if keys[pygame.K_RIGHT]:
        x += 5
    if x < 0:
        x = 0
    if x > SCREEN_WIDTH - perso_choisi.get_width():
        x = SCREEN_WIDTH - perso_choisi.get_width()
    return x

# ------------------------

## les différentes collisions de notes

def check_collision(notes, snake_x, snake_y, is_poison= False):
    """Vérifie les collisions avec les notes et les notes empoisonée."""
    global score, lives
    marge = 5
    for note in notes[:]:
        if snake_x - marge < note[0] < snake_x + perso_choisi.get_width() + marge and (snake_y - marge < note[1] < snake_y + perso_choisi.get_height() + marge):
            notes.remove(note)
            if is_poison:
                lives -=1
                if lives >= 1 : poison_hit_sound.play()
                if lives == 0: 
                    game_over_sound.play()
                    game_over(score)
                    reset_game()
            else:     
                score += 1
                heptagon_collect.play()

# --------------------

def check_collision_booster(booster_notes, snake_x, snake_y):
    """Vérifie les collisions avec les notes booster."""
    global score
    new_booster_notes = []
    for note in booster_notes:
        if snake_x < note[0] + note_width and snake_x + perso_choisi.get_width() > note[0] and \
           snake_y < note[1] + note_height and snake_y + perso_choisi.get_height() > note[1]:
            booster_notes.remove(note)
            score += 2  # Augmenter le score de +2
            booster_hit_sound.play()
        else:
            new_booster_notes.append(note)
    return new_booster_notes

def check_collision_lives(live_notes, snake_x, snake_y):
    """Vérifie les collisions avec les notes booster."""
    global lives
    new_life_notes = []
    for note in live_notes:
        if snake_x < note[0] + note_width and snake_x + perso_choisi.get_width() > note[0] and \
           snake_y < note[1] + note_height and snake_y + perso_choisi.get_height() > note[1]:
            live_notes.remove(note)
            if lives < 3:
                lives += 1  # Augmenter la vie de +1
                live_hit_sound.play()
        else:
            new_life_notes.append(note)
    return new_life_notes

def check_collision_slow(slow_notes, snake_x, snake_y):
    """Vérifie les collisions avec les notes booster."""
    global slow_effect_time
    new_slow_notes = []
    for note in slow_notes:
        if snake_x < note[0] + note_width and snake_x + perso_choisi.get_width() > note[0] and \
           snake_y < note[1] + note_height and snake_y + perso_choisi.get_height() > note[1]:
            slow_notes.remove(note)
            slow_effect_time = 600
            slow_hit_sound.play()
        else:
            new_slow_notes.append(note)
    return new_slow_notes

# --------------------

def reset_game():
    """Réinitialise les variables du jeu pour rejouer."""
    global score, lives, level, notes, poison_notes, booster_notes #snake_x, 
    #snake_y
    score = 0
    lives = 3
    level = 1
    notes = []
    poison_notes = []
    booster_notes = []
    #snake_x = SCREEN_WIDTH // 2  # Recentrer le personnage
    #snake_y = SCREEN_HEIGHT - 50


# --------------------

running = True
is_paused = False # pour mettre pause au jeux
clock = pygame.time.Clock()
score = 0
level = 1

# ------------------------
## Game over

def game_over(score):
    """Affiche l'écran de fin et quitte le jeu."""
    save_score(score)
    font = pygame.font.Font(None, 72)
    text = font.render("GAME OVER", True, (0, 0, 0))
    screen.blit(text, (SCREEN_WIDTH // 2 - 150, SCREEN_HEIGHT // 2 - 50))
    
    # Afficher le score final
    score_text = font.render(f"Score: {score}", True, (0, 0, 0))
    screen.blit(score_text, (SCREEN_WIDTH // 2 - 150, SCREEN_HEIGHT // 2 + 50))
    
    display_top_scores()

    # Afficher les instructions pour rejouer ou quitter
    small_font = pygame.font.Font(None, 36)
    retry_text = small_font.render("Press R to Retry or Q to Quit", True, (0, 0, 0))
    screen.blit(retry_text, (SCREEN_WIDTH // 2 - 150, SCREEN_HEIGHT // 2 + 250))

    
    pygame.display.flip()

    # Boucle pour attendre une action
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:  # Rejouer
                    return True
                elif event.key == pygame.K_q:  # Quitter
                    pygame.quit()
                    sys.exit()
    #pygame.time.wait(3000)
    #pygame.quit()
    #sys.exit()

# ------------------------
## la boucle de jeux
game_theme.stop()
while running:
    # screen.fill((255, 255, 255))  # Fond blanc
    # Afficher l'image de fond

    while lives > 0:

        screen.blit(winter_back, (0, 0))

        # Gestion des événements
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                lives = 0
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    is_paused = not is_paused

        if not is_paused:

            # Générer une note
            if random.randint(1, NOTE_FREQUENCY) == 1:
                notes.append(generate_note())

            # Générer une note empoisonnée dès 0 de score
            if score >= 0 and  random.randint(1, POISON_NOTE_FREQUENCY) == 1:
                poison_notes.append(generate_note())
            
            # Générer un booster si on a atteint 30 de score
            if score >= 30 and random.randint(1, BOOSTER_NOTE_FREQUENCY) == 1:
                booster_notes.append(generate_note())

            # Générer un booster vie si on a atteint 50 de score
            if score >= 50 and random.randint(1, BOOSTER_NOTE_FREQUENCY) == 1:
                live_notes.append(generate_note())
            
            # Generer un booster de vitesse si on atteint 70 de score
            if score >= 70 and random.randint(1, SLOW_NOTE_FREQUENCY) == 1:
                slow_notes.append(generate_note())
            

            notes, poison_notes = update_notes(notes, poison_notes)
            booster_notes = update_booster_notes(booster_notes)
            live_notes = update_booster_notes(live_notes)
            slow_notes = update_booster_notes(slow_notes)

            check_collision(notes, snake_x, snake_y)
            check_collision(poison_notes, snake_x, snake_y, is_poison=True)
            check_collision_booster(booster_notes, snake_x, snake_y)
            check_collision_lives(live_notes, snake_x, snake_y)
            check_collision_slow(slow_notes,snake_x, snake_y)

            # Vérifier et mettre à jour le niveau
            check_level(score)
            adjust_frequency(level) # ajuste la fréquence des notes 

            # déplacement du serpent
            snake_x = controlkey(x=snake_x)

            # Dessiner le serpent
            # pygame.draw.rect(screen, Green, (snake_x, snake_y, snake_width, snake_height))
            screen.blit(perso_choisi, (snake_x, snake_y))

        slow_note_color = get_multicolor_color() # couleur 

        # Dessiner les notes
        for note in notes:
            pygame.draw.rect(screen, note_color, (note[0], note[1], note_width, note_height))
        for poison_note in poison_notes:
            pygame.draw.rect(screen, poison_note_color, (poison_note[0],poison_note[1], note_width, note_height))
        for booster_note in booster_notes:
            pygame.draw.rect(screen, booster_note_color, (booster_note[0], booster_note[1], note_width, note_height))
        for live_note in live_notes:
            pygame.draw.rect(screen, live_note_color, (live_note[0], live_note[1], note_width, note_height))
        for slow_note in slow_notes:
            pygame.draw.rect(screen, slow_note_color, (slow_note[0], slow_note[1], note_width, note_height))

        # Score 
        font = pygame.font.Font(None, 36)
        score_text = font.render(f"{score}", True, (0, 0, 0))
        screen.blit(score_text, (110, 50))

        # Level
        level_text = font.render(f"{level}", True, (0, 0, 0))
        screen.blit(level_text, (665, 50) )

        # afficher les vies
        lives_text = font.render(f"Lives: {lives}", True, (0, 0, 0))
        screen.blit(lives_text, (630, 110))

        # Compte à rebours booster slow
        if slow_effect_time > 0:
            font = pygame.font.Font(None, 36)
            slow_text = font.render(f"Slow Effect: {slow_effect_time // 60} s", True, (255, 0, 0))
            screen.blit(slow_text, (SCREEN_WIDTH // 2 - 100, 20))



        # ------------------------

        if is_paused :
            font = pygame.font.Font(None, 74)
            text = font.render("Pause", True, (255, 255, 255))
            screen.blit(text, (SCREEN_WIDTH // 2 - text.get_width() // 2, SCREEN_HEIGHT // 2 - text.get_height() // 2))

        # ------------------------

        # Mettre à jour l'écran
        pygame.display.flip()
        clock.tick(60)  # 60 frames par seconde

    if not game_over(score):
        running = False

pygame.quit()

## ////////////////////////// FIN DU CODE