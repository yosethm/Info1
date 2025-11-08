import pygame

pygame.init()


ANCHO = 800
ALTO = 600
TITULO = "Etapa 1"

ventana = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption(TITULO)

COLOR_FONDO = (20, 20, 40)  # azul oscuro 

FPS = 60
reloj = pygame.time.Clock()


ejecutando = True
while ejecutando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            ejecutando = False

    ventana.fill(COLOR_FONDO)

    pygame.display.flip()

    reloj.tick(FPS)

pygame.quit()
