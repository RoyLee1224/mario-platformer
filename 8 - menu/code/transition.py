import pygame

class Transition:
    def __init__(self, screen_width, screen_height):
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.scale = 0.1
        self.scale_increment = 0.05
        self.delay = 35
        self.transition_surf = pygame.Surface((self.screen_width, self.screen_height))
        self.mask_img = pygame.image.load('../graphics/character/hat.png').convert_alpha()

    def run_transition(self, screen):
        while self.scale <= 1:
            self.transition_surf.fill((0, 0, 0))
            scaled_mask_img = pygame.transform.scale(self.mask_img, (
            int(self.screen_width * self.scale), int(self.screen_height * self.scale)))
            self.transition_surf.blit(scaled_mask_img, ((self.screen_width - scaled_mask_img.get_width()) // 2,
                                                        (self.screen_height - scaled_mask_img.get_height()) // 2))
            screen.blit(self.transition_surf, (0, 0))
            pygame.display.update()
            pygame.time.wait(self.delay)
            self.scale += self.scale_increment

        while self.scale >= 0:
            self.transition_surf.fill((0, 0, 0))
            scaled_mask_img = pygame.transform.scale(self.mask_img, (
            int(self.screen_width * self.scale), int(self.screen_height * self.scale)))
            self.transition_surf.blit(scaled_mask_img, ((self.screen_width - scaled_mask_img.get_width()) // 2,
                                                        (self.screen_height - scaled_mask_img.get_height()) // 2))
            screen.blit(self.transition_surf, (0, 0))
            pygame.display.update()
            pygame.time.wait(self.delay)
            self.scale -= self.scale_increment
