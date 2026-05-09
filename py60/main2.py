import pygame

pygame.init()

l1 = 600

l2 = 600



tela = pygame.display.set_mode(size=(l1,l2))

# pygame.display.flip()

pygame.display.set_caption('ping pong')

velocidade = 20

rosa = 'pink'

x = 250
y = 250

largura = 10
altura = 10


while True:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()

    teclas = pygame.key.get_pressed()
    if teclas[pygame.K_DOWN]:
        y += velocidade
    if teclas[pygame.K_UP]:
        y -= velocidade
    if teclas[pygame.K_LEFT]:
        x -= velocidade
    if teclas[pygame.K_RIGHT]:
        x += velocidade
    tela.fill(('blue'))
    pygame.draw.rect(tela,rosa,(x,y,largura,altura))
    pygame.display.flip()
    pygame.time.Clock().tick(30)
