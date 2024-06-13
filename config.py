import pygame




# Pygame app
windowHeight = 700
windowWidth = 900
frame_index = 0
running = True
fps = 60

# Custom events (timers)
everySec = pygame.USEREVENT + 1
everyFourSeconds = pygame.USEREVENT + 2
everyFourthOfASec = pygame.USEREVENT + 3

# colours
white = (255, 255, 255)
gray = (128, 128, 128)
yellow = (255, 255, 0)
orange = (255, 165, 0)
green = (0, 255, 0)
red = (255, 0, 0)
black = (0, 0, 0)

button_colour = (100, 100, 100)

# Action buttons
button_width = 100
button_height = 30
button_y_pos = windowHeight - button_height - 10
button_padding = 10


# Bar
bar_width = 150
bar_height = 23
barBorderWidth = 5

# hunger
maxHunger = 100
curHunger = 75
hungerBarX = 10
hungerBarY = 100

# hunger
maxHappiness = 100
curHappiness = 75
happinessBarX = 10
happinessBarY = 100





