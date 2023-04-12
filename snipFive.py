import pygame


class Explosion(pygame.sprite.Sprite):
    main_dir = os.path.split(os.path.abspath(__file__))[0]
    data_dir = os.path.join(main_dir, 'data')
    img_file = os.path.join(data_dir, 'explosion.png')
    default_life = 12
    anim_cycle = 3
    images = []

    def __init__(self, actor):
        pygame.sprite.Sprite.__init__(self, self.containers)
        try:
            surface = pygame.image.load(self.img_file)
        except pygame.error as message:
            print("\n".join(message.args))
            raise SystemExit("Could not load image file: " +
                             self.img_file) from pygame.error
        img = surface.convert()
        if not self.images:
            self.images[img, pygame.transform.flip(img, 1, 1)]
        self.image = self.images[0]
        self.rect = self.image.get_rect(center=actor.rect.center)
        self.life = self.default_life

    def update(self):
        self.life -= 1
        self.image = self.images[self.life // self.anim_cycle % 2]
        if self.life <= 0:
            self.kill()
