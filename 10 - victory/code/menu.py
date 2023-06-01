import pygame, sys
from PIL import Image
from pygame.image import load

class MainMenu:
    def __init__(self, screen):
        self.screen = screen
        self.running = True

        # Load the images
        self.s_img = pygame.image.load('../graphics/menu/letters/s.png').convert_alpha()
        self.t_img = pygame.image.load('../graphics/menu/letters/t.png').convert_alpha()
        self.a_img = pygame.image.load('../graphics/menu/letters/a.png').convert_alpha()
        self.r_img = pygame.image.load('../graphics/menu/letters/r.png').convert_alpha()

        # Scale the images
        scale_factor = 5  # Adjust this value to change the scaling of the images
        self.s_img = pygame.transform.scale(self.s_img, (
        self.s_img.get_width() * scale_factor, self.s_img.get_height() * scale_factor))
        self.t_img = pygame.transform.scale(self.t_img, (
        self.t_img.get_width() * scale_factor, self.t_img.get_height() * scale_factor))
        self.a_img = pygame.transform.scale(self.a_img, (
        self.a_img.get_width() * scale_factor, self.a_img.get_height() * scale_factor))
        self.r_img = pygame.transform.scale(self.r_img, (
        self.r_img.get_width() * scale_factor, self.r_img.get_height() * scale_factor))

        # Set the position of the images
        self.spacing = 10 * scale_factor  # Change this to set the spacing between letters
        total_width = (
                                  self.s_img.get_width() + self.t_img.get_width() + self.a_img.get_width() + self.r_img.get_width() + self.t_img.get_width()) + self.spacing * 4
        self.start_x = (self.screen.get_width() - total_width) // 2
        self.start_y = (self.screen.get_height() - self.s_img.get_height()) // 2

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

        # 操作說明
        self.font = pygame.font.Font('../graphics/ui/ARCADEPI.ttf', 30)
        self.text_color = (255, 255, 255)
        self.text_surface = pygame.Surface((500, 50), pygame.SRCALPHA)  # Adjust size as needed
        self.alpha = 128
        self.alpha_var = 3

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

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:  # Start the game by pressing Space
                    self.running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  # Left mouse button
                    mouse_x, mouse_y = pygame.mouse.get_pos()
                    start_rect = pygame.Rect(self.start_x, self.start_y,
                                             self.s_img.get_width() * 2 + self.t_img.get_width() * 2 + self.a_img.get_width() + self.r_img.get_width() + self.spacing * 4,
                                             self.s_img.get_height())
                    if start_rect.collidepoint(mouse_x, mouse_y):
                        self.running = False

    def run(self):
        while self.running:
            self.frame_counter += 1
            if self.frame_counter >= self.frame_delay:
                self.frame_counter = 0
                if self.frame_index == len(self.bg_frames) - 1:
                    pygame.time.delay(200)  # Add a delay after the last frame, you can adjust this value
                self.frame_index = (self.frame_index + 1) % len(self.bg_frames)

            self.screen.blit(self.bg_frames[self.frame_index], (0, 0))

            # Draw the 'START' text using the loaded images
            x = self.start_x
            self.screen.blit(self.s_img, (x, self.start_y))
            x += self.s_img.get_width() + self.spacing
            self.screen.blit(self.t_img, (x, self.start_y))
            x += self.t_img.get_width() + self.spacing
            self.screen.blit(self.a_img, (x, self.start_y))
            x += self.a_img.get_width() + self.spacing
            self.screen.blit(self.r_img, (x, self.start_y))
            x += self.r_img.get_width() + self.spacing
            self.screen.blit(self.t_img, (x, self.start_y))

            self.handle_events()

            # 操作說明呼吸效果
            self.alpha += self.alpha_var
            if self.alpha >= 255 or self.alpha <= 0:
                self.alpha_var *= -1

            # Clear the text surface
            self.text_surface.fill((0, 0, 0, 0))  # Fill with fully transparent color
            # Render the text
            text = self.font.render('Press space to start', True, self.text_color)
            # Blit the text onto the text surface
            self.text_surface.blit(text, (0, 0))  # Adjust position as needed
            # Set the alpha of the text surface and blit it onto the screen
            self.text_surface.set_alpha(self.alpha)
            self.screen.blit(self.text_surface, (400,600))

            pygame.display.update()
            pygame.time.Clock().tick(60)

