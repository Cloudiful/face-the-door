# coding=utf8
import pygame
import data

pygame.init()
clock = pygame.time.Clock()
# define font style and size
font = pygame.font.Font('assets/cute.ttf', data.FONTSIZE)

# define main windows' framework
# set resolution
screen = pygame.display.set_mode((data.WIDTH, data.HEIGHT), pygame.FULLSCREEN)  # type: pygame.Surface
# set title
pygame.display.set_caption("Face Recognition Door Lock System")
# hide the mouse
# pygame.mouse.set_visible(False)

background_group = pygame.sprite.Group()
front_group = pygame.sprite.Group()


def cvimage_to_pygame(image):
    """Convert cvimage into a pygame image"""
    return pygame.image.frombuffer(image.tostring(), image.shape[1::-1], "RGB")  # gives you (width, height) tuple,


# clear screen
def clear_screen():
    screen.fill((66, 66, 66))
    background_group.empty()
    front_group.empty()
    pygame.display.flip()


# draw screen in correct order
def draw_screen():
    pygame.display.flip()
    background_group.draw(screen)
    front_group.draw(screen)


class Title(pygame.sprite.Sprite):
    def __init__(self, title, x=data.WIDTH // 2, y=40, size=32, align="center"):
        super().__init__()
        fontTemp = pygame.font.Font('assets/cute.ttf', size)
        self.image = fontTemp.render(title, False, (200, 200, 200), (50, 50, 50))  # type: pygame.Surface
        self.rect = self.image.get_rect()
        if align == 'center':
            self.rect.center = [x, y]
        elif align == 'midleft':
            self.rect.midleft = [x, y]
        data.formerFontWidth = self.image.get_width()
        data.formerFontHeight = self.image.get_height()
        data.formerFontX = data.WIDTH // 2 - self.image.get_width() // 2
        data.formerFontY = 40
        front_group.add(self)


# def show_title(title):

#     text = font.render(title, False, (200, 200, 200), (50, 50, 50))  # type: pygame.Surface
#     screen.blit(text, (data.WIDTH // 2 - text.get_width() // 2, 20))


class Text(pygame.sprite.Sprite):
    def __init__(self, text, x, y, size):
        super().__init__()
        fontTemp = pygame.font.Font('assets/cute.ttf', size)
        textR = fontTemp.render(text, False, data.BGCOLOR)
        self.image = textR  # type: pygame.Surface
        self.rect = self.image.get_rect()
        self.rect.center = [x, y]

    def draw(self):
        front_group.add(self)


# # x,y is the center of the text
# def show_text(text, x, y, size):
#     fontTemp = pygame.font.Font('assets/cute.ttf', size)
#     textR = fontTemp.render(text, False, (200, 200, 200))
#     screen.blit(textR, (x - textR.get_width() // 2, y - textR.get_height() // 2))
#     new_text = Text(text, x, y, size)
#     front_group.add(new_text)
#     print(new_text)


class CameraFeed(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = cvimage_to_pygame(data.cameraFeed)
        self.image = pygame.transform.scale(self.image, [data.cameraFeedWidth, data.cameraFeedHeight])
        self.rect = self.image.get_rect()

    def show_camera_feed(self):
        background_group.empty()
        background_group.add(self)


class Button(pygame.sprite.Sprite):
    def __init__(self, x, y, size="square"):
        super().__init__()
        if size == "square":
            self.image = pygame.image.load('assets/button_square.png')
            self.image = pygame.transform.scale(self.image, [100, 100])
        elif size == "long":
            self.image = pygame.image.load('assets/button_long.png')
            self.image = pygame.transform.scale(self.image, [400, 100])

        self.rect = self.image.get_rect()
        self.rect.center = [x, y]

    def draw(self):
        front_group.add(self)

    def detected(self, pos):
        action = False

        # check mouseover and click conditions
        if self.rect.collidepoint(pos):
            action = True

        return action
