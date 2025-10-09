import pygame
 
# Inizializza pygame 
pygame.init()
 
 
# TODO 1: crea la finestra di gioco (es. 800x600)
LARGHEZZA=800
ALTEZZA=600
win = pygame.display.set_mode((800, 600)) 
pygame.display.set_caption("Gioco con pygame.Rect")
 
 
# Colori utili 
WHITE = (255, 255, 255) 
BLACK = (0, 0, 0) 
RED = (255, 0, 0) 
GREEN = (0, 255, 0)
 
 
# TODO 2: crea il giocatore come oggetto pygame.Rect 
# (usa quattro valori: x, y, larghezza, altezza) 
player= pygame.Rect(50,250,40,40)#creo oggetto giocatore
 
 

# TODO 3: crea il rettangolo obiettivo (quello verde) 
# goal = ... 
goal = pygame.Rect(600,250,100,100)
 
 
# TODO 4: crea una lista con uno o due muri come pygame.Rect 
# walls = [ ... ]
wall=pygame.Rect(300,150,20,300)
 
# Velocità del giocatore
 
vel = 5 
clock = pygame.time.Clock() 
run = True 
won = False
 
 
while run: 
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: 
            run = False
 
 
    # TODO 5: leggi i tasti premuti 
    keys = pygame.key.get_pressed()
 
 
    # TODO 6: muovi il giocatore modificando player.x e player.y 
    # ricordati di controllare le collisioni con i muri usando colliderect() 
    if keys[pygame.K_LEFT]:
        if player.x-vel>=0:
            player.x -= vel
    if keys[pygame.K_RIGHT]:
        if player.x+player.w+vel<=LARGHEZZA:
            player.x += vel
        if player.colliderect(wall):
            player.x -=vel
            
    if keys[pygame.K_UP]:
        if player.y-vel>=0:
            player.y -=vel
 
 
    # TODO 7: controlla se il giocatore tocca il rettangolo verde (goal) 
    # usa colliderect() per verificare la vittoria 
    # if player.colliderect(goal): 
    #     ...
 if player.colliderect(goal):
     
 
    # Disegno a schermo 
    win.fill(WHITE)
 
 
    # TODO 8: disegna il giocatore, il traguardo e i muri
    pygame.draw.rect(win, RED, player)
    pygame.draw.rect(win, GREEN, goal)
    pygame.draw.rect(win, BLACK, wall)

    pygame.display.update() 
    clock.tick(60)
 
pygame.quit()