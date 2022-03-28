
# monitor width and height
WIDTH, HEIGHT = 800, 480

FPS = 50

image_x, image_y = -WIDTH, HEIGHT // 4

cameraFeed = []
cameraFeedWidth = 800
cameraFeedHeight = 480
cameraFeedX = 0
cameraFeedY = 0

pwd = ''
method = 'face'
# # string list for text file
# TXT = []
# FONTSIZE = 32
#
# formerFontX = 0
# formerFontY = 0
# formerFontWidth = 0
# formerFontHeight = 0

# buttonWidth = 64
# buttonHeight = 24

# header when TCP communicating, contains the length of message
HEADER = 64

# my index in server (for example: me - 0 opponent - 1)
net_index = 0

# received message from server
net_content = '!'

# how many client has connected to the server
client_count = 0
