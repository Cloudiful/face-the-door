import pygame
import data

pygame.init()

# define font style and size
font = pygame.font.Font('assets/luoli.ttf', data.FONTSIZE)
font_special = pygame.font.Font('assets/luoli.ttf', int(data.FONTSIZE * 1.5))

# define main windows framework
# set resolution
WIN = pygame.display.set_mode((data.WIDTH, data.HEIGHT), pygame.FULLSCREEN)
# set title
pygame.display.set_caption("Face Recognition Door Lock System")


def cvimage_to_pygame(image):
    """Convert cvimage into a pygame image"""
    return pygame.image.frombuffer(image.tostring(), image.shape[1::-1], "RGB")  # gives you (width, height) tuple,


# clear the scene
def clear_screen():
    WIN.fill((66, 66, 66))
    pygame.display.update()


def show_camera_feed():
    WIN.blit(cvimage_to_pygame(data.cameraFeed), (20, 120))  # convert cvimage to pygame surface
    pygame.display.update()


def show_title(title):
    textBack = pygame.draw.rect(WIN, (66, 66, 66), (0, 0, data.WIDTH, data.HEIGHT // 4))

    text = font.render(title, False, (200, 200, 200), (50, 50, 50))
    WIN.blit(text, (data.WIDTH // 2 - text.get_width() // 2, 20))

    pygame.display.update()
