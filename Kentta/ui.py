import pygame

class ui(pygame.sprite.Sprite):

    def __init__(self, alusta, screen):
        super().__init__()
        self.SCREEN = screen
        self.surf = pygame.Surface((20, 20))
        self.surf.fill("green")
        self.rect = self.surf.get_rect(center = (30-720, 10))
        self.alusta = alusta
        self.kello = pygame.time.Clock()
        self.kerrokset = pygame.sprite.LayeredUpdates()
        self.kerrokset.add(self)
        self.kerrokset.move_to_front(self)

    def paivitaUI(self):
        while True:
            pygame.draw.rect(self.SCREEN,"green",[1200,10,40,40]) 
            pygame.display.update(self)
            self.alusta.naytaLaskuri()
            self.kello.tick(60)