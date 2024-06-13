### imports

# Internal
import os, time, random

# External
import pygame
import pygame.font 


# INITIALISATIONS 
pygame.font.init()  

# Variables

# Colours
BLACK = (0, 0, 0)
LIGHT_PINK = (255, 182, 193)
RED = (255, 0, 0)
WHITE = (255, 255, 255)
ORANGE = (255, 165, 0)


# Window/Config
WIDTH = 600
HEIGHT = 600

def create_padded_rect(original_rect, padding:int = 10):
    padded_rect = pygame.Rect(0, 0, original_rect.width + 2*padding, original_rect.height + 2*padding)
    padded_rect.center = original_rect.center
    return padded_rect

# Screen elements 

# Hunger bar
hunger={
  "max": 100,
  "current": 100,
  "bar":{
    "meatSize": 20,
    "pos": 50,
    "width": 400,
    "height": 20,
  }
}

hungerMax = 100
hungerCurrent = 50
hungerBarMeatSize = 20
hungerBarWidth = 400
hungerBarHeight = 20
hungerBarPositionX = 30
hungerBarPositionY = 200


hungerBar = hunger["bar"]



feedButtonWidth = 100
feedButtonHeight = 20
feedButtonRadius = 10
feedButtonX = 100
feedButtonY = 400

BUTTON_MARGIN = 100

font = pygame.font.Font(None, 32)


pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.RESIZABLE)
pygame.display.set_caption("Custom Background and Character")


# bg 
background = pygame.image.load("images/bg.jpg")
if not background:
  print("Error: Background image not found at 'a/a'")
  quit()

background = pygame.transform.scale(background, (WIDTH, HEIGHT))

# hunger bar

meat_image = pygame.image.load("images/meat.PNG")
if not meat_image:
  print("Error: Meat image not found!")
  quit()

meat_width = meat_image.get_width()
meat_height = meat_image.get_height()


meat_image = pygame.transform.scale(meat_image, (hungerBarMeatSize, hungerBarMeatSize))



# pet 

character = pygame.image.load("sprites/AdamsCar.PNG")
if not character:
  print("Error: Character sprite not found at 'characters/AdamsCar.PNG'")
  quit()

characterSize = 250

character = pygame.transform.scale(character, (characterSize, characterSize))

character_width = character.get_width()
character_height = character.get_height()

def center_character():
  global character, screen, character_width, character_height
  x_pos = 200#(WIDTH - character_width) // 2
  y_pos = (HEIGHT - character_height) // 2
  screen.blit(character, (x_pos, y_pos))


running = True 
hunger = hunger["max"]


while running:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False
    if event.type == pygame.MOUSEBUTTONDOWN:
      mouse_x, mouse_y = pygame.mouse.get_pos()
      if BUTTON_MARGIN < mouse_x < BUTTON_MARGIN + feedButtonWidth and \
         BUTTON_MARGIN < mouse_y < BUTTON_MARGIN + feedButtonHeight:
        clicked = True
    if event.type == pygame.MOUSEBUTTONUP:
      if clicked:

        print("Hello world!")
        clicked = False 

  screen.fill(BLACK)




  screen.blit(background, (0, 0))
  if character:
    center_character() 


  pygame.draw.rect(screen, LIGHT_PINK, 
                  (feedButtonX, feedButtonY, feedButtonWidth, feedButtonHeight), 
                  border_radius=feedButtonRadius)


  text_surface = font.render("Feed", True, BLACK)
  text_x = (feedButtonWidth - text_surface.get_width()) // 2 + feedButtonX
  text_y = (feedButtonHeight - text_surface.get_height()) // 2 + feedButtonY
  screen.blit(text_surface, (text_x, text_y))

  # hunger bar
  #pygame.draw.rect(screen, ORANGE, (20, hungerBarPositionX, hungerBarPositionY, feedButtonWidth, feedButtonHeight), border_radius=10)
  pygame.draw.rect(screen, ORANGE, (hungerBarPositionX, hungerBarPositionY, feedButtonWidth, feedButtonHeight), border_radius=10)

  fill_width = int((hunger / 100 ) * feedButtonWidth)
  #pygame.draw.rect(screen, RED, (20, hungerBarPositionX, hungerBarPositionY, fill_width, feedButtonHeight), border_radius=5)
  pygame.draw.rect(screen, RED, (hungerBarPositionX, hungerBarPositionY, fill_width, feedButtonHeight), border_radius=5)

  screen.blit(meat_image, (hungerBarPositionX, hungerBarPositionY))






  pygame.display.flip()

pygame.quit()
