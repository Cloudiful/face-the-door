import pygame

# monitor width and height
WIDTH, HEIGHT = 800, 480

FPS = 25

image_x, image_y = -WIDTH, HEIGHT // 4

cameraFeed = []

# string list for text file
TXT = []
FONTSIZE = 25

# header when TCP communicating, contains the length of message
HEADER = 64

# my index in server (for example: me - 0 opponent - 1)
net_index = 0

# received message from server
net_content = '!'

# how many client has connected to the server
client_count = 0
