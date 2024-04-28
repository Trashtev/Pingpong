import pygame
pygame.init()
window = pygame.display.set_mode((500, 500))
img = pygame.image.load("Png.png")
bg = pygame.transform.scale()

fps = pygame.time.Clock()
game = True

class GameObject():
    def __init__(self, img, x, y, width, height):
        self.image = pygame.image.load(img)
        self.image = pygame.transform.scale(self.image, (width, height))
        self.hitbox = self.image.get_rect()
        self.hitbox.x = x
        self.hitbox.y = y
    def show(self):
        window.blit(self.image,(self.hitbox))
    


while game:
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            game = False

    window.blit(bg,(0, 0))

    pygame.display.update()
    fps.tick()