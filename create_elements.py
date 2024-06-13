import pygame

from config import windowHeight, windowWidth
from config import white
from config import button_y_pos, button_padding

from __init__ import font



def add_padding(original_rect, padding:int = 20):
    padded_rect = pygame.Rect(0, 0, original_rect.width + 2*padding, original_rect.height + 2*padding)
    padded_rect.center = original_rect.center
    return padded_rect




# Put into a list so animation can loop through each index - optimises better
character_images = [
    pygame.image.load("sprites/AdamsCar/idle_1.png").convert_alpha(),
    pygame.image.load("sprites/AdamsCar/idle_2.png").convert_alpha(),
    pygame.image.load("sprites/AdamsCar/idle_3.png").convert_alpha(),
    pygame.image.load("sprites/AdamsCar/idle_4.png").convert_alpha(),
    pygame.image.load("sprites/AdamsCar/idle_5.png").convert_alpha(),
    pygame.image.load("sprites/AdamsCar/idle_6.png").convert_alpha(),
]



background_image = pygame.image.load("images/bg.jpg").convert()
background_image = pygame.transform.scale(background_image, (windowWidth, windowHeight))


mainButtonsWidth = 100
mainButtonsHeight = 50

mainButtonsX = 100
mainButtonsY = 600

feedButton = pygame.image.load("UI/mainButtons/feed.png").convert_alpha()
feedButton = pygame.transform.scale(feedButton, (mainButtonsWidth, mainButtonsHeight))
feedButtonRect = feedButton.get_rect(topleft=(100, mainButtonsY))


feedButtonHover = pygame.image.load("UI/mainButtons/feedHover.png").convert_alpha()
feedButtonHover = pygame.transform.scale(feedButtonHover, (mainButtonsWidth, mainButtonsHeight))

feedButtonClicked = pygame.image.load("UI/mainButtons/feedClicked.png").convert_alpha()
feedButtonClicked = pygame.transform.scale(feedButtonClicked, (mainButtonsWidth, mainButtonsHeight))




playButton = pygame.image.load("UI/mainButtons/play.png").convert_alpha()
playButton = pygame.transform.scale(playButton, (mainButtonsWidth, mainButtonsHeight))
playButtonRect = playButton.get_rect(topleft=(350, mainButtonsY))


playButtonHover = pygame.image.load("UI/mainButtons/playHover.png").convert_alpha()
playButtonHover = pygame.transform.scale(playButtonHover, (mainButtonsWidth, mainButtonsHeight))

playButtonClicked = pygame.image.load("UI/mainButtons/playClicked.png").convert_alpha()
playButtonClicked = pygame.transform.scale(playButtonClicked, (mainButtonsWidth, mainButtonsHeight))




cleanButton = pygame.image.load("UI/mainButtons/clean.png").convert_alpha()
cleanButton = pygame.transform.scale(cleanButton, (mainButtonsWidth, mainButtonsHeight))
cleanButtonRect = cleanButton.get_rect(topleft=(650, mainButtonsY))

cleanButtonHover = pygame.image.load("UI/mainButtons/cleanHover.png").convert_alpha()
cleanButtonHover = pygame.transform.scale(cleanButtonHover, (mainButtonsWidth, mainButtonsHeight))

cleanButtonClicked = pygame.image.load("UI/mainButtons/cleanClicked.png").convert_alpha()
cleanButtonClicked = pygame.transform.scale(cleanButtonClicked, (mainButtonsWidth, mainButtonsHeight))




foodMenuOptionsX = 100
foodMenuOptionsY = 500


foodMenuOptionsWidth = 100
foodMenuOptionsHeight = 25


# For food menu outline, adjust the height accordingly
foodMenuOutline = pygame.image.load("UI/Menus/food/foodMenuOutline.png").convert_alpha()
foodMenuOutline = pygame.transform.scale(foodMenuOutline, (101, 125)) 

foodMenuTitle = pygame.image.load("UI/Menus/food/foodMenuTitle.png").convert_alpha()
foodMenuTitle = pygame.transform.scale(foodMenuTitle, (100, 25))

foodMenuClose = pygame.image.load("UI/Menus/food/closeMenu.png").convert_alpha()
foodMenuClose = pygame.transform.scale(foodMenuClose, (20, 20))
foodMenuCloseRect = foodMenuClose.get_rect(topleft=(foodMenuOptionsX + 100, foodMenuOptionsY - 25))

# Pasta Option
foodMenuOptionPasta = pygame.image.load("UI/Menus/food/pastaOption.png").convert_alpha()
foodMenuOptionPasta = pygame.transform.scale(foodMenuOptionPasta, (foodMenuOptionsWidth, foodMenuOptionsHeight))
foodMenuOptionPastaRect = foodMenuOptionPasta.get_rect(topleft=(foodMenuOptionsX, foodMenuOptionsY))
foodMenuOptionPastaHover = pygame.image.load("UI/Menus/food/pastaOptionHover.png").convert_alpha()
foodMenuOptionPastaHover = pygame.transform.scale(foodMenuOptionPastaHover, (foodMenuOptionsWidth, foodMenuOptionsHeight))
foodMenuOptionPastaClicked = pygame.image.load("UI/Menus/food/pastaOptionClicked.png").convert_alpha()
foodMenuOptionPastaClicked = pygame.transform.scale(foodMenuOptionPastaClicked, (foodMenuOptionsWidth, foodMenuOptionsHeight))

# Carrot Option
foodMenuOptionCarrot = pygame.image.load("UI/Menus/food/carrotOption.png").convert_alpha()
foodMenuOptionCarrot = pygame.transform.scale(foodMenuOptionCarrot, (foodMenuOptionsWidth, foodMenuOptionsHeight))
foodMenuOptionCarrotRect = foodMenuOptionCarrot.get_rect(topleft=(foodMenuOptionsX, foodMenuOptionsY + 25))
foodMenuOptionCarrotHover = pygame.image.load("UI/Menus/food/carrotOptionHover.png").convert_alpha()
foodMenuOptionCarrotHover = pygame.transform.scale(foodMenuOptionCarrotHover, (foodMenuOptionsWidth, foodMenuOptionsHeight))
foodMenuOptionCarrotClicked = pygame.image.load("UI/Menus/food/carrotOptionClicked.png").convert_alpha()
foodMenuOptionCarrotClicked = pygame.transform.scale(foodMenuOptionCarrotClicked, (foodMenuOptionsWidth, foodMenuOptionsHeight))

# Apple Option
foodMenuOptionApple = pygame.image.load("UI/Menus/food/appleOption.png").convert_alpha()
foodMenuOptionApple = pygame.transform.scale(foodMenuOptionApple, (foodMenuOptionsWidth, foodMenuOptionsHeight))
foodMenuOptionAppleRect = foodMenuOptionApple.get_rect(topleft=(foodMenuOptionsX, foodMenuOptionsY + 25 + 25))
foodMenuOptionAppleHover = pygame.image.load("UI/Menus/food/appleOptionHover.png").convert_alpha()
foodMenuOptionAppleHover = pygame.transform.scale(foodMenuOptionAppleHover, (foodMenuOptionsWidth, foodMenuOptionsHeight))
foodMenuOptionAppleClicked = pygame.image.load("UI/Menus/food/appleOptionClicked.png").convert_alpha()
foodMenuOptionAppleClicked = pygame.transform.scale(foodMenuOptionAppleClicked, (foodMenuOptionsWidth, foodMenuOptionsHeight))

# Cake Option
foodMenuOptionCake = pygame.image.load("UI/Menus/food/cakeOption.png").convert_alpha()
foodMenuOptionCake = pygame.transform.scale(foodMenuOptionCake, (foodMenuOptionsWidth, foodMenuOptionsHeight))
foodMenuOptionCakeRect = foodMenuOptionCake.get_rect(topleft=(foodMenuOptionsX, foodMenuOptionsY + 25 + 25 + 25))
foodMenuOptionCakeHover = pygame.image.load("UI/Menus/food/cakeOptionHover.png").convert_alpha()
foodMenuOptionCakeHover = pygame.transform.scale(foodMenuOptionCakeHover, (foodMenuOptionsWidth, foodMenuOptionsHeight))
foodMenuOptionCakeClicked = pygame.image.load("UI/Menus/food/cakeOptionClicked.png").convert_alpha()
foodMenuOptionCakeClicked = pygame.transform.scale(foodMenuOptionCakeClicked, (foodMenuOptionsWidth, foodMenuOptionsHeight))




string = pygame.image.load("UI/Accessories/string.png").convert_alpha()
string = pygame.transform.scale(string, (10, 400))

ball = pygame.image.load("UI/Accessories/ball.png").convert_alpha()
ball = pygame.transform.scale(ball, (50, 50))
ballRect = ball.get_rect(topleft=(windowWidth - 50, 400))




















play_button_text = font.render("Play", True, white)
feed_button_text = font.render("Feed", True, white)
other_button_text = font.render("Other", True, white)
hunger_button_text = font.render("Hunger", True, white)


feedBtnRect = feed_button_text.get_rect(centerx=(windowWidth // 5))
otherBtnRect = play_button_text.get_rect(centerx=(windowWidth // 5) * 3)
playBtnRect = play_button_text.get_rect(centerx=(windowWidth // 5) * 2)
HungerBtnRect = hunger_button_text.get_rect(centerx=(windowWidth // 5) * 4)


feedBtnRect.bottom = button_y_pos
otherBtnRect.bottom = button_y_pos
playBtnRect.bottom = button_y_pos
HungerBtnRect.bottom = button_y_pos



feed_rect = add_padding(feedBtnRect, button_padding)
other_rect = add_padding(otherBtnRect, button_padding)
play_rect = add_padding(playBtnRect, button_padding)