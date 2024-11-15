import pygame 

#Inicializar pygame

pygame.init()

#Configuramos la pantalla
screen = pygame.display.set_mode((800, 600)) #Definimos resolucion
pygame.display.set_caption("Space Invaders") #Definimos titulo

# Clase jugador
class Player:
    def __init__(self):
        self.image = pygame.image.load("nave.png") #Cargo imagen de jugador
        self.x = 370 #Posicion inicial x
        self.y = 480 #Posicion inicial y
        self.x_change = 0 #Cambio de posicion en x (Para movimiento)

    def draw(self):
        #Dibujar la nave en la posicion actual
        screen.blit(self.image, (self.x, self.y))

    def move(self):
        # Actualizar posicion en x
        self.x += self.x_change
        # limitar el movimiento dentro de los limites de la pantalla
        if self.x <= 0:
            self.x = 0 # Posicion en la que esta dentro de la pantalla
        elif self.x > 736: #Ancho de pantalla: 800 - ancho de figura: 64
            self.x = 736

    
    # Creamos la instancia del jugador

player = Player()
        

running = True #Bandera para el bucle infinito
while running: #Mientras running sea True, bucle infinito

    #Fondo de pantalla (negro)
    screen.fill((0, 0, 0)) #Tupla de 3 miembros

    # Dibujar al jugador:
    player.move()
    player.draw()

    # Detectar eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT: #mientras el evento sea igual a X
            running = False #Paramos el bucle

        # Detectar si se toca una tecla
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                player.x_change = -0.3
            elif event.key == pygame.K_d:
                player.x_change = 0.3
        
        # Detectar si se suelta la tecla
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_a or event.key == pygame.K_d:
                player.x_change = 0


    #Actualizar la pantalla
    pygame.display.flip()

pygame.quit() #Fin del juego