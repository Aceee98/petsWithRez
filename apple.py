import pygame, random


#               Import variables from config file

# button variables
from config import button_height, button_padding, button_width, button_y_pos, button_colour

# Window/pygame variables
from config import windowHeight, windowWidth, fps, running, frame_index

# Custom events
from config import everySec, everyFourSeconds, everyFourthOfASec

# Colour variables
from config import yellow, red, gray, green, black, white

# Bar variables
from config import bar_height, bar_width, barBorderWidth

# Hunger variables
from config import curHunger, maxHunger, hungerBarX, hungerBarY

# Happiness variables
from config import curHappiness, maxHappiness, happinessBarX, happinessBarY



from create_elements import background_image, character_images
from create_elements import feed_button_text, play_button_text, other_button_text
from create_elements import feed_rect, play_rect, other_rect

from create_elements import feedBtnRect, otherBtnRect, playBtnRect
from create_elements import feedButton, playButton, cleanButton


from create_elements import feedButtonHover, playButtonHover, cleanButtonHover

from create_elements import feedButtonClicked, playButtonClicked, cleanButtonClicked

from create_elements import feedButtonRect, playButtonRect, cleanButtonRect

from create_elements import foodMenuOutline, foodMenuTitle, foodMenuOptionsY, foodMenuOptionsX, foodMenuClose, foodMenuCloseRect

from create_elements import foodMenuOptionPasta, foodMenuOptionPastaRect, foodMenuOptionPastaClicked, foodMenuOptionPastaHover
from create_elements import foodMenuOptionCarrot, foodMenuOptionCarrotRect, foodMenuOptionCarrotClicked, foodMenuOptionCarrotHover
from create_elements import foodMenuOptionApple, foodMenuOptionAppleRect, foodMenuOptionAppleClicked, foodMenuOptionAppleHover
from create_elements import foodMenuOptionCake, foodMenuOptionCakeRect, foodMenuOptionCakeClicked, foodMenuOptionCakeHover

from create_elements import string, ball


from __init__ import screen, font, clock


def draw_bar(screen, hunger_value, bar_type:str, x, y):
  if bar_type == "hunger":
      bar_colour = red
  elif bar_type == "happiness":
      bar_colour = yellow
  green_bar_width = int(hunger_value / maxHunger * bar_width)
  pygame.draw.rect(screen, black, (x - barBorderWidth // 2, y - barBorderWidth // 2,
                                  bar_width + barBorderWidth, bar_height + barBorderWidth), border_radius=5)
  pygame.draw.rect(screen, bar_colour, (x, y, bar_width, bar_height), border_radius=5)
  pygame.draw.rect(screen, green, (x, y, green_bar_width, bar_height), border_radius=5)



def drawFoodBox():
    # pygame.draw.rect(screen, white, (100, 435, 150, 195), border_radius=10)

    # pygame.draw.rect(screen, gray, (100, 435, 150, 65), border_radius=10)
    # pygame.draw.rect(screen, black, (100, 435, 150, 65), 5, border_radius=10)

    # pygame.draw.rect(screen, gray, (100, 435+65, 150, 65), border_radius=10)
    # pygame.draw.rect(screen, black, (100, 435+65, 150, 65), 5, border_radius=10)

    # pygame.draw.rect(screen, gray, (100, 435+65+65, 150, 65), border_radius=10)
    # pygame.draw.rect(screen, black, (100, 435+65+65, 150, 65), 5, border_radius=10)

    # pygame.draw.rect(screen, black, (100, 435, 150, 195), 5, border_radius=10)
    pass





pygame.time.set_timer(everySec, 1000)
pygame.time.set_timer(everyFourSeconds, 4000)
pygame.time.set_timer(everyFourthOfASec, 300)





background_image = pygame.image.load("images/bg.jpg").convert()
menuButton = pygame.image.load("images/Buttons/menuButton.png").convert_alpha()
menuButtonRect = menuButton.get_rect(topleft=(windowWidth - 70, 20))

background_image = pygame.transform.scale(background_image, (windowWidth, windowHeight))
menuButton = pygame.transform.scale(menuButton, (50, 50))


class Character:
    def __init__(self):
        self.numOfCharacterImages = len(character_images)


        self.hunger = 50
        self.happiness = 50
        self.cleanliness = 50

        self.race = ""





    def feed(self, food:str = None):
        if not food:
            pass
        else:
            sustainance = self.getFoodSustainance(food)
            if self.hunger >= 100:
                self.hunger == 100
            else:
                self.hunger += sustainance
                if self.hunger > 100:
                    self.hunger = 100


    def getFoodSustainance(self, food:str):
        if character.race == "cat":
            if food == "cake":
                sustainance = 5
            elif food == "pasta":
                sustainance = 3
            elif food == "carrot":
                sustainance = 2
            elif food == "apple":
                sustainance = 10
        elif character.race == "dog":
            if food == "cake":
                sustainance = 1
            elif food == "pasta":
                sustainance = 5
            elif food == "carrot":
                sustainance = 2
            elif food == "apple":
                sustainance = 3
        else:
            if food == "cake":
                sustainance = 2
            elif food == "pasta":
                sustainance = 1
            elif food == "carrot":
                sustainance = 5
            elif food == "apple":
                sustainance = 3
        return sustainance


class UserInterface:
    def __init__(self, screen):
        self.screen = screen
        self.feedButton = feedButton
        self.playButton = playButton
        self.cleanButton = cleanButton

        self.feedButtonHover = feedButtonHover
        self.playButtonHover = playButtonHover
        self.cleanButtonHover = cleanButtonHover

        self.feedButtonClicked = feedButtonClicked
        self.playButtonClicked = playButtonClicked
        self.cleanButtonClicked = cleanButtonClicked

        self.feedButtonActive = self.feedButton
        self.playButtonActive = self.playButton
        self.cleanButtonActive = self.cleanButton

        self.pastaOptionActive = foodMenuOptionPasta
        self.carrotOptionActive = foodMenuOptionCarrot
        self.appleOptionActive = foodMenuOptionApple
        self.cakeOptionActive = foodMenuOptionCake

        self.showFoodOptions = False
        self.playing = False
        self.ballHeight = 200
        self.playingHeight = 0
        self.verticalDirection = 1
        self.ballFalling = False
        self.ballInteractable = True



    def updateFeedButton(self):
        if feedButtonRect.collidepoint(pygame.mouse.get_pos()):
            if pygame.mouse.get_pressed()[0]:
                self.feedButtonActive = self.feedButtonClicked
                self.showFoodOptions = True
            else:
                self.feedButtonActive = self.feedButtonHover
        else:
            self.feedButtonActive = self.feedButton
    
    def updatePlayButton(self):
        if playButtonRect.collidepoint(pygame.mouse.get_pos()):
            if pygame.mouse.get_pressed()[0]:
                self.playButtonActive = self.playButtonClicked
                self.playing = True
            else:
                self.playButtonActive = self.playButtonHover
        else:
            self.playButtonActive = self.playButton


    def updateCleanButton(self):
        if cleanButtonRect.collidepoint(pygame.mouse.get_pos()):
            if pygame.mouse.get_pressed()[0]:
                UI.cleanButtonActive = UI.cleanButtonClicked
            else:
                UI.cleanButtonActive = UI.cleanButtonHover
        else:
            UI.cleanButtonActive = UI.cleanButton
        

    def UpdatefoodMenu(self):
        if foodMenuOptionCarrotRect.collidepoint(pygame.mouse.get_pos()):
            if pygame.mouse.get_pressed()[0]:
                self.carrotOptionActive = foodMenuOptionCarrotClicked
                character.feed("carrot")
            else:
                self.carrotOptionActive = foodMenuOptionCarrotHover
        else:
            self.carrotOptionActive = foodMenuOptionCarrot

        if foodMenuOptionPastaRect.collidepoint(pygame.mouse.get_pos()):
            if pygame.mouse.get_pressed()[0]:
                self.pastaOptionActive = foodMenuOptionPastaClicked
                character.feed("pasta")
            else:
                self.pastaOptionActive = foodMenuOptionPastaHover
        else:
            self.pastaOptionActive = foodMenuOptionPasta


        if foodMenuOptionAppleRect.collidepoint(pygame.mouse.get_pos()):
            if pygame.mouse.get_pressed()[0]:
                self.appleOptionActive = foodMenuOptionAppleClicked
                character.feed("apple")
            else:
                self.appleOptionActive = foodMenuOptionAppleHover
        else:
            self.appleOptionActive = foodMenuOptionApple

        if foodMenuOptionCakeRect.collidepoint(pygame.mouse.get_pos()):
            if pygame.mouse.get_pressed()[0]:
                self.cakeOptionActive = foodMenuOptionCakeClicked
                character.feed("cake")
            else:
                self.cakeOptionActive = foodMenuOptionCakeHover

        else:
            
            self.cakeOptionActive = foodMenuOptionCake

        if foodMenuCloseRect.collidepoint(pygame.mouse.get_pos()):
            if pygame.mouse.get_pressed()[0]:
                self.showFoodOptions = False
            else:
                pass

    def playActivity(self):
        if self.playing:
            if self.ballInteractable:
                screen.blit(string, (450, self.ballHeight + self.playingHeight - 400))
            ball_rect = pygame.Rect(430, self.ballHeight + self.playingHeight, ball.get_width(), ball.get_height())
            screen.blit(ball, (430, self.ballHeight + self.playingHeight))
            self.playingHeight += self.verticalDirection
            if self.ballInteractable:
                if self.ballFalling:
                    self.verticalDirection = -1
                elif not self.ballFalling:
                    self.verticalDirection = 1
                
                if self.playingHeight == -50:
                    self.ballFalling = False
                elif self.playingHeight == 80:
                    self.ballFalling = True

           
            
        
            if ball_rect.collidepoint(pygame.mouse.get_pos()):  # Check if the mouse click occurred within the ball's area
                if pygame.mouse.get_pressed()[0]:
                    for i in range(50):
                        self.verticalDirection =  5
                        self.ballInteractable = False
                        print(self.playingHeight)
            
            if self.playingHeight > 500:
                print("Hi")
                self.playing = False
                self.ballHeight = 200
                self.playingHeight = 0
                self.ballInteractable = True
                self.ballFalling = False
                self.verticalDirection = 1
                    
        else:
            ...

    def PlayActivityFallingBall(self):
        if self.ballFalling:
            ...



UI = UserInterface(screen)
character = Character()


def hunger_decrease(curHunger):
    if curHunger < 0:
        pass
    else:
        curHunger -= random.randint(1,3)
    return curHunger


character_images = [pygame.transform.scale(img, (250, 250)) for img in character_images]



def character_animation(frame_index):
    character_image = character_images[frame_index]
    character_center_x = windowWidth // 2 - character_image.get_width() // 2
    character_center_y = windowHeight // 2 - character_image.get_height() // 2
    screen.blit(character_image, (character_center_x, character_center_y + 50))



def blitMainButtons():
    screen.blit(UI.feedButtonActive, (100, 600))
    screen.blit(UI.playButtonActive, (350, 600))
    screen.blit(UI.cleanButtonActive, (650, 600))


def oldMainButtons():
    pygame.draw.rect(screen, button_colour, other_rect, border_radius=10)
    pygame.draw.rect(screen, button_colour, play_rect, border_radius=10)
    pygame.draw.rect(screen, button_colour, feed_rect, border_radius=10)
    
    # buttons
    screen.blit(feed_button_text, feedBtnRect)
    screen.blit(play_button_text, playBtnRect)
    screen.blit(other_button_text, otherBtnRect)


def foodMenuButtons():
    screen.blit(foodMenuOutline, (foodMenuOptionsX, foodMenuOptionsY - 25))
    screen.blit(foodMenuTitle, (foodMenuOptionsX, foodMenuOptionsY - 25))
    screen.blit(foodMenuClose, (foodMenuOptionsX + 100, foodMenuOptionsY - 25))

    screen.blit(UI.pastaOptionActive, (foodMenuOptionsX, foodMenuOptionsY))

    screen.blit(UI.carrotOptionActive, (foodMenuOptionsX, foodMenuOptionsY + 25))

    screen.blit(UI.appleOptionActive, (foodMenuOptionsX, foodMenuOptionsY + 25  + 25))

    screen.blit(UI.cakeOptionActive, (foodMenuOptionsX, foodMenuOptionsY + 25  + 25  + 25))    


# while this loops, the app stays on - when it stops, the app closes
while running:
    for event in pygame.event.get():
    # this just means if they click the x then the app actually closes lol
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if feed_rect.collidepoint(event.pos):
                pass
            
            
        elif event.type == everyFourSeconds:
            curHunger = hunger_decrease(curHunger)

        elif event.type == everyFourthOfASec:
            frame_index = (frame_index + 1) % character.numOfCharacterImages
        

        
        
    
    
                
                
    screen.blit(background_image, (0, 0))

    UI.updateFeedButton()
    UI.updatePlayButton()
    UI.updateCleanButton()

    UI.playActivity()


    blitMainButtons()


    if UI.showFoodOptions:
        UI.UpdatefoodMenu()
        foodMenuButtons()

    #oldMainButtons()


    character_animation(frame_index)


    draw_bar(screen, character.hunger, "hunger", hungerBarX, hungerBarY)


    screen.blit(menuButton, (windowWidth - 70, 20))



    drawFoodBox()

    pygame.display.flip()


    clock.tick(fps)

pygame.quit()