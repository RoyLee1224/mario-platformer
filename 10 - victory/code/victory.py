import pygame, sys
from pygame.locals import QUIT, KEYDOWN, K_ESCAPE
from PIL import Image
from pygame.image import load

class VictoryScreen:
    def __init__(self, screen,coins):
        self.screen = screen
        self.coins = coins
        self.running = True

        # Load the images
        self.v_img = pygame.image.load('../graphics/menu/letters/v.png').convert_alpha()
        self.i_img = pygame.image.load('../graphics/menu/letters/i.png').convert_alpha()
        self.c_img = pygame.image.load('../graphics/menu/letters/c.png').convert_alpha()
        self.t_img = pygame.image.load('../graphics/menu/letters/t.png').convert_alpha()
        self.o_img = pygame.image.load('../graphics/menu/letters/o.png').convert_alpha()
        self.r_img = pygame.image.load('../graphics/menu/letters/r.png').convert_alpha()
        self.y_img = pygame.image.load('../graphics/menu/letters/y.png').convert_alpha()

        # Scale the images
        scale_factor = 5  # Adjust this value to change the scaling of the images
        self.v_img = pygame.transform.scale(self.v_img, (
            self.v_img.get_width() * scale_factor, self.v_img.get_height() * scale_factor))
        self.i_img = pygame.transform.scale(self.i_img, (
            self.i_img.get_width() * scale_factor, self.i_img.get_height() * scale_factor))
        self.c_img = pygame.transform.scale(self.c_img, (
            self.c_img.get_width() * scale_factor, self.c_img.get_height() * scale_factor))
        self.t_img = pygame.transform.scale(self.t_img, (
            self.t_img.get_width() * scale_factor, self.t_img.get_height() * scale_factor))
        self.o_img = pygame.transform.scale(self.o_img, (
            self.o_img.get_width() * scale_factor, self.o_img.get_height() * scale_factor))
        self.r_img = pygame.transform.scale(self.r_img, (
            self.r_img.get_width() * scale_factor, self.r_img.get_height() * scale_factor))
        self.y_img = pygame.transform.scale(self.y_img, (
            self.y_img.get_width() * scale_factor, self.y_img.get_height() * scale_factor))

        # Set the position of the images
        self.spacing = 10 * scale_factor  # Change this to set the spacing between letters
        total_width = (
                              self.v_img.get_width() + self.i_img.get_width() + self.c_img.get_width() + self.t_img.get_width() + self.o_img.get_width() + self.r_img.get_width() + self.y_img.get_width()) + self.spacing * 6
        self.start_x = (self.screen.get_width() - total_width) // 2
        self.start_y = (self.screen.get_height() - self.v_img.get_height()) // 2

        try:
            from PIL import Image
            self.pil_installed = True
        except ImportError:
            self.pil_installed = False

        # background
        self.bg_image_path = '../graphics/menu/background.gif'
        self.bg_frames = self.load_gif_frames()
        self.frame_index = 0
        self.frame_counter = 0
        self.frame_delay = 5  # Change this value to control the GIF animation speed

        # cursor
        surf = load('../graphics/menu/mouse.png').convert_alpha()
        cursor = pygame.cursors.Cursor((0, 0), surf)
        pygame.mouse.set_cursor(cursor)

        self.font = pygame.font.Font('../graphics/ui/ARCADEPI.ttf', 30)

    def load_gif_frames(self):
        frames = []
        if self.pil_installed:
            gif = Image.open(self.bg_image_path)
            for frame_index in range(gif.n_frames):
                gif.seek(frame_index)
                frame_surface = pygame.image.fromstring(
                    gif.tobytes(), gif.size, gif.mode
                ).convert()

                # Scale the frame to fit the screen
                frame_surface = pygame.transform.scale(
                    frame_surface, (self.screen.get_width(), self.screen.get_height())
                )

                frames.append(frame_surface)
        else:  # No PIL installed, load a JPG instead
            jpg_path = '../graphics/menu/background.jpg'
            frame_surface = pygame.image.load(jpg_path).convert()
            frame_surface = pygame.transform.scale(
                frame_surface, (self.screen.get_width(), self.screen.get_height())
            )
            frames.append(frame_surface)

        return frames

    def show_coins(self):
        font = pygame.font.Font(None, 36)
        text = font.render(f"Coins: {self.coins}", True, '#33323d')
        text_rect = text.get_rect(center=(self.screen.get_width() // 2, self.screen.get_height() // 2 + 100))
        self.screen.blit(text, text_rect)

    def run(self):
        while self.running:
            self.frame_counter += 1
            if self.frame_counter >= self.frame_delay:
                self.frame_counter = 0
                if self.frame_index == len(self.bg_frames) - 1:
                    pygame.time.delay(200)  # Add a delay after the last frame, you can adjust this value
                self.frame_index = (self.frame_index + 1) % len(self.bg_frames)

            self.screen.blit(self.bg_frames[self.frame_index], (0, 0))

            # Draw the 'VICTORY' text using the loaded images
            x = self.start_x
            self.screen.blit(self.v_img, (x, self.start_y))
            x += self.v_img.get_width() + self.spacing
            self.screen.blit(self.i_img, (x, self.start_y))
            x += self.i_img.get_width() + self.spacing
            self.screen.blit(self.c_img, (x, self.start_y))
            x += self.c_img.get_width() + self.spacing
            self.screen.blit(self.t_img, (x, self.start_y))
            x += self.t_img.get_width() + self.spacing
            self.screen.blit(self.o_img, (x, self.start_y))
            x += self.o_img.get_width() + self.spacing
            self.screen.blit(self.r_img, (x, self.start_y))
            x += self.r_img.get_width() + self.spacing
            self.screen.blit(self.y_img, (x, self.start_y))

            self.show_coins()
            coin_amount_surf = self.font.render(str(self.coins), False, (255, 255, 255))
            self.screen.blit(coin_amount_surf, (100, 100))

            for event in pygame.event.get():
                if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                    self.running = False  # 結束遊戲畫面

            pygame.display.update()
            pygame.time.Clock().tick(60)

        # 遊戲畫面結束後的清理工作
        pygame.quit()
        sys.exit()
