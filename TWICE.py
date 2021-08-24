"""Author : Mario Liao

   Date : 05/03/2019

   Description: This program is a module with all my sprites in it needed for me
   to create my game"""

import pygame
import random

class Player(pygame.sprite.Sprite):
    """This class defines the sprite for the player"""
    def __init__(self, screen, xStart, dxMultiplier):
        '''This initializer takes a screen as a parameter and creates a player
        sprite. By initializing the image and getting the sprite's rect attributes,
        we can control the image's direction'''
        # Call the parent __init__() method
        pygame.sprite.Sprite.__init__(self)

        # Define the image attributes for our player sprite

        # Using A Count Variable And A List, We Made A Moving Like Image, That Alternates Between 2 Images
        self.count = 3
        self.imageList = [pygame.image.load("Images/NayeonStand.png")] * 4 + [pygame.image.load("Images/NayeonForward.png")] * 4
        self.image = self.imageList[self.count]

        # Set the location of where our player sprite should start
        self.rect = self.image.get_rect()
        self.rect.centerx = xStart
        self.rect.centery = screen.get_height() / 2

        # Variables To Control The Direction Of Our Sprite
        self.dx = 5 * dxMultiplier
        self.dy = 0

        # Variables Created To Be Used Later On In The Methods
        self.up = False
        self.down = False
        self.yPlayer = 0
        self.window = screen
        self.keepMoving = False
        self.dxMultiplier = dxMultiplier

    def goUp(self, yPlayer):
        '''This method changes the direction of our sprite to go up by setting
        its y direction to a negative number'''
        self.dy = -25
        self.up = True
        self.yPlayer = yPlayer

    def goDown(self, yPlayer):
        '''This method changes the direction of our sprite to go up by setting
        its y direction to a positive number'''
        self.dy = 25
        self.down = True
        self.yPlayer = yPlayer

    def setImageList(self, playerName):
        '''This method changes the character of our sprite by changing our image
        list'''

        # Depending On What The playerName is inserted, the imageList will change accordingly
        if playerName == "Nayeon":
            self.imageList = [pygame.image.load("Images/NayeonStand.png")] * 4 \
                + [pygame.image.load("Images/NayeonForward.png")] * 4
        if playerName == "Jeongyeon":
            self.imageList = [pygame.image.load("Images/JeongyeonStand.png")] * \
                4 + [pygame.image.load("Images/JeongyeonForward.png")] * 4
        if playerName == "Momo":
            self.imageList = [pygame.image.load("Images/MomoStand.png")] * \
                4 + [pygame.image.load("Images/MomoForward.png")] * 4
        if playerName == "Sana":
            self.imageList = [pygame.image.load("Images/SanaStand.png")] * \
                4 + [pygame.image.load("Images/SanaForward.png")] * 4
        if playerName == "Jihyo":
            self.imageList = [pygame.image.load("Images/JihyoStand.png")] * \
                4 + [pygame.image.load("Images/JihyoForward.png")] * 4
        if playerName == "Mina":
            self.imageList = [pygame.image.load("Images/MinaStand.png")] * \
                4 + [pygame.image.load("Images/MinaForward.png")] * 4
        if playerName == "Dahyun":
            self.imageList = [pygame.image.load("Images/DahyunStand.png")] * \
                4 + [pygame.image.load("Images/DahyunForward.png")] * 4
        if playerName == "Chaeyoung":
            self.imageList = [pygame.image.load("Images/ChaeyoungStand.png")] * \
                4 + [pygame.image.load("Images/ChaeyoungForward.png")] * 4
        if playerName == "Tzuyu":
            self.imageList = [pygame.image.load("Images/TzuyuStand.png")] * \
                4 + [pygame.image.load("Images/TzuyuForward.png")] * 4
        if playerName == "NayeonFlash":
            self.imageList = [pygame.image.load("Images/NayeonStand.png")] * \
                2 + [pygame.image.load("Images/NayeonForward.png")] * 2 + \
                [pygame.image.load("Images/NayeonStandFlash.png")] * 2 + \
                [pygame.image.load("Images/NayeonForwardFlash.png")] * 2
        if playerName == "JeongyeonFlash":
            self.imageList = [pygame.image.load("Images/JeongyeonStand.png")] * \
                2 + [pygame.image.load("Images/JeongyeonForward.png")] * 2 + \
                [pygame.image.load("Images/JeongyeonStandFlash.png")] * 2 + \
                [pygame.image.load("Images/JeongyeonForwardFlash.png")] * 2
        if playerName == "MomoFlash":
            self.imageList = [pygame.image.load("Images/MomoStand.png")] * \
                2 + [pygame.image.load("Images/MomoForward.png")] * 2 + \
                [pygame.image.load("Images/MomoStandFlash.png")] * 2 + \
                [pygame.image.load("Images/MomoForwardFlash.png")] * 2
        if playerName == "SanaFlash":
            self.imageList = [pygame.image.load("Images/SanaStand.png")] * \
                2 + [pygame.image.load("Images/SanaForward.png")] * 2 + \
                [pygame.image.load("Images/SanaStandFlash.png")] * 2 + \
                [pygame.image.load("Images/SanaForwardFlash.png")] * 2
        if playerName == "JihyoFlash":
            self.imageList = [pygame.image.load("Images/JihyoStand.png")] * \
                2 + [pygame.image.load("Images/JihyoForward.png")] * 2 + \
                [pygame.image.load("Images/JihyoStandFlash.png")] * 2 + \
                [pygame.image.load("Images/JihyoForwardFlash.png")] * 2
        if playerName == "MinaFlash":
            self.imageList = [pygame.image.load("Images/MinaStand.png")] * \
                2 + [pygame.image.load("Images/MinaForward.png")] * 2 + \
                [pygame.image.load("Images/MinaStandFlash.png")] * 2 + \
                [pygame.image.load("Images/MinaForwardFlash.png")] * 2
        if playerName == "DahyunFlash":
            self.imageList = [pygame.image.load("Images/DahyunStand.png")] * \
                2 + [pygame.image.load("Images/DahyunForward.png")] * 2 + \
                [pygame.image.load("Images/DahyunStandFlash.png")] * 2 + \
                [pygame.image.load("Images/DahyunForwardFlash.png")] * 2
        if playerName == "ChaeyoungFlash":
            self.imageList = [pygame.image.load("Images/ChaeyoungStand.png")] * \
                2 + [pygame.image.load("Images/ChaeyoungForward.png")] * 2 + \
                [pygame.image.load("Images/ChaeyoungStandFlash.png")] * 2 + \
                [pygame.image.load("Images/ChaeyoungForwardFlash.png")] * 2
        if playerName == "TzuyuFlash":
            self.imageList = [pygame.image.load("Images/TzuyuStand.png")] * \
                2 + [pygame.image.load("Images/TzuyuForward.png")] * 2 + \
                [pygame.image.load("Images/TzuyuStandFlash.png")] * 2 + \
                [pygame.image.load("Images/TzuyuForwardFlash.png")] * 2

    def letKeepMoving(self):
        '''This is a method that changed the keepMoving instance variable
        to true to be used later on in the update method'''
        self.keepMoving = True

    def update(self):
        """This method will be called automatically and it will be used to reposition
        the player sprite"""

        # Causes The Player Sprite To Go Up Or Down Depending On The Value Of self.dy
        self.rect.top += self.dy

        # Causes The Player Sprite To Continuously Go Right
        self.rect.right += self.dx

        # Equation and Variables Used To Allow Image Alternating
        self.count += 1
        self.imageCount = self.count % 8
        self.image = self.imageList[self.imageCount]

        # Checks If The Player Sprite Has Hit The Center Of The Screen, and If Yes, Make The Player Stop Moving
        if self.dx == 5:
            if self.rect.centerx == (self.window.get_width() / 2) + 35:
                self.dx = 0
        else:
            if self.rect.centerx == (self.window.get_width() / 2) + 40:
                self.dx = 0

        # Checks If The Sprite Is Going Up
        if self.up:
            if self.rect.centery == self.yPlayer - 50:
                self.dy = 0

        # Checks If The Sprite Is Going Down
        if self.down:
            if self.rect.centery == self.yPlayer + 50:
                self.dy = 0

        # Lets The Sprite Continue Moving
        if self.keepMoving:
            self.dx = 5 * self.dxMultiplier

class MusicNote(pygame.sprite.Sprite):
    """This class defines the sprite for our Music Notes"""
    def __init__(self, x, y, noteColour, dxMultiplier):
        """This initializer takes an x and y location,and a integer value as
        parameters for this class. It uses these parameters to make a music note
        sprite that can have differentcolours and by initialzing the image and
        getting the sprite's rectattributes, this class controls the direction
        of our sprite too"""
        # Call the parent __init__() method
        pygame.sprite.Sprite.__init__(self)

        # Define the image attributes for our music sprite

        # By Using a List and a count variable, we are able to make a floating like music note
        self.count = 0

        self.noteColour = noteColour % 6

        # Depending on the value of the noteColour, we load in different colour notes
        if self.noteColour == 0:
            self.noteImages = [pygame.image.load("Images/PurpleMusicNoteFirst.png")] * 8 + \
                [pygame.image.load("Images/PurpleMusicNoteSecond.png")] * 8 + \
                [pygame.image.load("Images/PurpleMusicNoteThrid.png")] * 8 + \
                [pygame.image.load("Images/PurpleMusicNoteSecond.png")] * 8 + \
                [pygame.image.load("Images/PurpleMusicNoteFirst.png")] * 8

        if self.noteColour == 1:
            self.noteImages = [pygame.image.load("Images/PinkMusicNoteThrid.png")] * 8 + \
                [pygame.image.load("Images/PinkMusicNoteSecond.png")] * 8 + \
                [pygame.image.load("Images/PinkMusicNoteFirst.png")] * 8 + \
                [pygame.image.load("Images/PinkMusicNoteSecond.png")] * 8 + \
                [pygame.image.load("Images/PinkMusicNoteThrid.png")] * 8

        if self.noteColour == 2:
            self.noteImages = [pygame.image.load("Images/YellowMusicNoteFirst.png")] * 8 + \
                [pygame.image.load("Images/YellowMusicNoteSecond.png")] * 8 + \
                [pygame.image.load("Images/YellowMusicNoteThrid.png")] * 8 + \
                [pygame.image.load("Images/YellowMusicNoteSecond.png")] * 8 + \
                [pygame.image.load("Images/YellowMusicNoteFirst.png")] * 8

        if self.noteColour == 3:
            self.noteImages = [pygame.image.load("Images/GreenMusicNoteThrid.png")] * 8 + \
                [pygame.image.load("Images/GreenMusicNoteSecond.png")] * 8 + \
                [pygame.image.load("Images/GreenMusicNoteFirst.png")] * 8 + \
                [pygame.image.load("Images/GreenMusicNoteSecond.png")] * 8 + \
                [pygame.image.load("Images/GreenMusicNoteThrid.png")] * 8

        if self.noteColour == 4:
            self.noteImages = [pygame.image.load("Images/DiamondMusicNoteFirst.png")] * 8 + \
                [pygame.image.load("Images/DiamondMusicNoteSecond.png")] * 8 + \
                [pygame.image.load("Images/DiamondMusicNoteThrid.png")] * 8 + \
                [pygame.image.load("Images/DiamondMusicNoteSecond.png")] * 8 + \
                [pygame.image.load("Images/DiamondMusicNoteFirst.png")] * 8

        if self.noteColour == 5:
            self.noteImages = [pygame.image.load("Images/BlueMusicNoteThrid.png")] * 8 + \
                [pygame.image.load("Images/BlueMusicNoteSecond.png")] * 8 + \
                [pygame.image.load("Images/BlueMusicNoteFirst.png")] * 8 + \
                [pygame.image.load("Images/BlueMusicNoteSecond.png")] * 8 + \
                [pygame.image.load("Images/BlueMusicNoteThrid.png")] * 8


        self.image = self.noteImages[self.count]

        # Get the rect attributes of the sprite and use it to control the direction and starting point
        self.rect = self.image.get_rect()
        self.rect.left = x
        self.rect.centery = y
        self.dx = 7 * dxMultiplier
        self.killSelf = False

    def killItSelf(self):
        '''This method is used to kill the sprite in the update function'''
        self.killSelf = True

    def update(self):
        '''This method will be called automatically in order to reposition our
        sprite and to allow our sprite's image to change and alternate'''

        # Causes The Music Sprite To Continuously Go Left
        self.rect.right -= self.dx

        # Equation and Variables Used To Allow Image Alternating
        self.count += 1
        self.imageCount = self.count % 40
        self.image = self.noteImages[self.imageCount]

        # Checks If The Music Note Hits The End Of The Screen, If Yes Tell It To Delete Itself
        if self.rect.right <= 0:
            self.kill()

        # Tell The Sprite To Kill Itself
        if self.killSelf == True:
            self.kill()

class Beach(pygame.sprite.Sprite):
    """This class defines the sprite for our Beach Background"""
    def __init__(self, screen, dxMultiplier):
        """This initializer takes a screen as a parameter and by initializing the
        image and getting its rect attributes, this class creates a beach
        background that is infinite"""
        # Call the parent __init__() method
        pygame.sprite.Sprite.__init__(self)

        # Set the image and create a beach background
        self.image = pygame.image.load("Images/BeachNight.png")
        self.image = self.image.convert()

        # Get the rect attributes of the beach to control the direction of our sprite
        self.rect = self.image.get_rect()
        self.rect.left = 0
        self.rect.top = 0
        self.dx = -7 * dxMultiplier

        self.window = screen
        self.keepMoving = True

    def stopKeepMoving(self):
        '''This is a method that changed the keepMoving instance variable
        to false to be used later on in the update method'''
        self.keepMoving = False

    def update(self):
        """This method will be called automatically and it will be used to
        reposition our sprite along with helping create an infinite background"""
        self.rect.right += self.dx

        # Checks if the right side of our sprite hits the right screen edge, if yes, reset its position
        if self.rect.right <= self.window.get_width():
            self.rect.left = 0

        # Tells The Sprite To Stop Moving
        if self.keepMoving == False:
            self.dx = 0

class ScoreNames(pygame.sprite.Sprite):
    """This class defines the sprite for our Score Names"""
    def __init__(self):
        """This initializer loads a custom font and uses it create a white text
        to represent our score names"""
        # Call the parent __init__() method
        pygame.sprite.Sprite.__init__(self)

        # Load our custom font, and initialize our image and get its rect attributes to set its starting point
        self.font = pygame.font.Font("Font/8-BIT WONDER.ttf", 24)
        message = "MEMBER X            LIVES         NOTES          SCORE          TIME"
        self.image = self.font.render(message, True, (255, 255, 255))
        self.rect = self.image.get_rect()
        self.rect.left = 5
        self.rect.top = 5

class ScoreImages(pygame.sprite.Sprite):
    """This class defines the sprite for our Score Images"""
    def __init__(self, imageChoice):
        """This initializer loads in different images and uses it to create
        a more aesthetically pleasing score board. Takes in imageChoice as a
        parameter to tell the class which image it wants to create"""
        # Call the parent __init__() method
        pygame.sprite.Sprite.__init__(self)

        # Depending on which imageChoice is asked, certain images will be created with certain positions
        if imageChoice == 0:
            self.image = pygame.image.load("Images/MemberImage.png")
            self.rect = self.image.get_rect()
            self.rect.left = 213
            self.rect.top = 5

        if imageChoice == 1:
            self.image = pygame.image.load("Images/LivesImage.png")
            self.rect = self.image.get_rect()
            self.rect.left = 345
            self.rect.top = 35

        if imageChoice == 2:
            self.image = pygame.image.load("Images/MusicNoteImage.png")
            self.rect = self.image.get_rect()
            self.rect.left = 565
            self.rect.top = 35

        if imageChoice == 3:
            self.image = pygame.image.load("Images/TimeImage.png")
            self.rect = self.image.get_rect()
            self.rect.left = 1048
            self.rect.top = 35

        if imageChoice == 4:
            self.image = pygame.image.load("Images/TWICEImage.png")
            self.rect = self.image.get_rect()
            self.rect.left = 1190
            self.rect.top = 3

class ScoreKeeper(pygame.sprite.Sprite):
    """This class defines the label sprite to display the information of our
    player, lives left, notes gotten, score gained, and time"""
    def __init__(self, player, livesLeft, scoreChoice, dxMultiplier):
        """This initializer takes in a string and two integers as parameters,
        and uses them to update the information of our game. It also takes
        in a score choice parameter to help tell us which score holder it wants
        us to create"""
        # Call the parent __init__() method
        pygame.sprite.Sprite.__init__(self)

        # Create mutiple instance variables to control using methods
        self.player = player
        self.lives = livesLeft
        self.notes = 0
        self.score = 0
        self.time = 0
        self.actualTime = 0
        self.scoreChoice = scoreChoice
        self.countTime = 0
        self.countImage = 1
        self.dxMultiplier = dxMultiplier
        self.isHidden = "Off"
        self.isDoubleTime = "Off"

        # Load our custom font
        self.font = pygame.font.Font("Font/8-BIT WONDER.ttf", 24)
        self.introFont = pygame.font.Font("Font/8-BIT WONDER.ttf", 36)
        self.controlFont = pygame.font.Font("Font/8-BIT WONDER.ttf", 20)

    def setPlayer(self, newCharacter):
        """This is a mutator method and it takes in a new character parameter
        and uses it to change the player instance variable"""
        self.player = newCharacter

    def loseLife(self):
        """This method changes the instance variable to lose one life each time
        it is called"""
        self.lives -=1

    def gainNotePoints(self):
        """This method add points to our music instance variable"""
        self.notes += 1

    def gainScorePoints(self):
        """This method add points to our score instance variable"""
        self.score += 21

    def getTime(self):
        """The method returns the value of our time instance variable"""
        return self.actualTime

    def update(self):
        """This method takes our information from our instance variables and
        uses it to create our text for our score keeper in game and will
        always update the text each time our instance variable changes"""

        # Depending on which score choice is given, it will create a certain score holder
        if self.scoreChoice == "player":
            message = str(self.player)
            self.image = self.font.render(message, True, (255, 255, 255))
            self.rect = self.image.get_rect()
            self.rect.right = 243
            self.rect.top = 32
        if self.scoreChoice == "lives":
            message = "X" + str(self.lives)
            self.image = self.font.render(message, True, (255, 255, 255))
            self.rect = self.image.get_rect()
            self.rect.left = 378
            self.rect.top = 32
        if self.scoreChoice == "musicNote":
            message = "X" + str(self.notes)
            self.image = self.font.render(message, True, (255, 255, 255))
            self.rect = self.image.get_rect()
            self.rect.left = 593
            self.rect.top = 32
        if self.scoreChoice == "score":
            message = "X " + str(self.score)
            self.image = self.font.render(message, True, (255, 255, 255))
            self.rect = self.image.get_rect()
            self.rect.left = 809
            self.rect.top = 32
        if self.scoreChoice == "time":
            self.countTime += 1
            self.time = int(self.countTime / (30 * (1 / self.dxMultiplier)))
            self.actualTime = self.countTime / (30 * (1 / self.dxMultiplier))
            message = "X" + str(self.time)
            self.image = self.font.render(message, True, (255, 255, 255))
            self.rect = self.image.get_rect()
            self.rect.left = 1076
            self.rect.top = 32
        if self.scoreChoice == "intro":
            self.countImage += 1
            message = "PRESS SPACE TO START"
            if self.countImage % 10 == 0 or self.countImage % 10 == 1  or \
               self.countImage % 10 == 2 or self.countImage % 10 == 3 or \
               self.countImage % 10 == 4:
                self.image = self.introFont.render(message, True, (255, 255, 255))
                self.rect = self.image.get_rect()
                self.rect.left = 305
                self.rect.centery = 360
            if self.countImage % 10 == 5 or self.countImage % 10 == 6 or \
               self.countImage % 10 == 7 or self.countImage % 10 == 8 \
               or self.countImage % 10 == 9:
                self.image = pygame.image.load("Images/TransparentDot.png")
        if self.scoreChoice == "title":
            message = "TWICE - DANCE THE NIGHT AWAY (8 Bit)"
            self.image = self.introFont.render(message, True, (255, 255, 255))
            self.rect = self.image.get_rect()
            self.rect.centerx = 640
            self.rect.centery = 30
        if self.scoreChoice == "controls":
            message = "CONTROLS"
            self.image = self.controlFont.render(message, True, (255, 255, 255))
            self.rect = self.image.get_rect()
            self.rect.right = 1280
            self.rect.centery = 127
        if self.scoreChoice == "up":
            message = "ARROW KEY UP -> GOES UP"
            self.image = self.controlFont.render(message, True, (255, 255, 255))
            self.rect = self.image.get_rect()
            self.rect.right = 1280
            self.rect.centery = 154
        if self.scoreChoice == "down":
            message = "ARROW KEY DOWN -> GOES DOWN"
            self.image = self.controlFont.render(message, True, (255, 255, 255))
            self.rect = self.image.get_rect()
            self.rect.right = 1280
            self.rect.centery = 181
        if self.scoreChoice == "mods":
            message = "MODS"
            self.image = self.controlFont.render(message, True, (255, 255, 255))
            self.rect = self.image.get_rect()
            self.rect.left = 0
            self.rect.centery = 127
        if self.scoreChoice == "hiddenInstruction":
            message = "PRESS H -> HIDDEN ON/OFF"
            self.image = self.controlFont.render(message, True, (255, 255, 255))
            self.rect = self.image.get_rect()
            self.rect.left = 0
            self.rect.centery = 154
        if self.scoreChoice == "doubleTimeInstruction":
            message = "PRESS D -> DOUBLETIME ON/OFF"
            self.image = self.controlFont.render(message, True, (255, 255, 255))
            self.rect = self.image.get_rect()
            self.rect.left = 0
            self.rect.centery = 181
        if self.scoreChoice == "hidden":
            message = "HIDDEN -> " + str(self.isHidden)
            self.image = self.controlFont.render(message, True, (255, 255, 255))
            self.rect = self.image.get_rect()
            self.rect.left = 0
            self.rect.centery = 235
        if self.scoreChoice == "doubleTime":
            message = "DOUBLETIME -> " + str(self.isDoubleTime)
            self.image = self.controlFont.render(message, True, (255, 255, 255))
            self.rect = self.image.get_rect()
            self.rect.left = 0
            self.rect.centery = 262

class BlackTop(pygame.sprite.Sprite):
    """This class defines the sprite for our Black Background Top"""
    def __init__(self):
        """This initializer loads in a black background image and places it
        at the top of our screen to make our score board look more visually
        appleasing"""

        # Call the parent __init__() method
        pygame.sprite.Sprite.__init__(self)

        # Load the black background image
        self.image = pygame.image.load("Images/BlackBackground.png")
        self.image = self.image.convert()

        # Get the rect attributes of the image to control its location
        self.rect = self.image.get_rect()
        self.rect.left = 0
        self.rect.top = 0

class FootPrint(pygame.sprite.Sprite):
    """This class defines the sprite for our footprint"""
    def __init__(self, xPlayer, yPlayer, count, dxMultiplier):
        """This initializer takes in the x and y location of our player, along
        with a count variable and uses it to create footprints from where our
        player was last in by initializing the image and getting its rect
        attributes"""

        # Call the parent __init__() method
        pygame.sprite.Sprite.__init__(self)

        # Create an image list to allow image alternating for the footprints
        self.footPrintImages = [pygame.image.load("Images/BlueFootPrintFirst.png"), pygame.image.load("Images/BlueFootPrintSecond.png")]

        # Using a count variable and equation, the image instance variable alternates between two images
        self.count = count
        self.imageCount = self.count % 2
        self.image = self.footPrintImages[self.imageCount]

        # Get the rect attributes of the sprite in order to control its direction and its starting position
        self.rect = self.image.get_rect()
        self.rect.centerx = xPlayer
        self.rect.centery = yPlayer
        self.dx = 7 * dxMultiplier

        self.keepMoving = True

    def stopKeepMoving(self):
        '''This is a method that changed the keepMoving instance variable
        to false to be used later on in the update method'''
        self.keepMoving = False

    def update(self):
        """This method is automatically called in order to update the position
        of our sprite and to check if it should be killed"""

        # Causes The footprint Sprite To Continuously Go Left
        self.rect.right -= self.dx

        # If the footprint passes the left edge of the screen, tell the sprite to delete itself
        if self.rect.right <= 0:
            self.kill()

        # Tells The Sprite To Stop Moving
        if self.keepMoving == False:
            self.dx = 0

class TransparentRectangle(pygame.sprite.Sprite):
    """This class defines the sprite for our Transparent Rectangle"""
    def __init__(self):
        """This initializer takes in the x location of our music note and uses
        it to create a transparent rectangle, the same width of the music note
        and the height of the screen and places it on top of our music note,
        covering all the music note and the whole vertical width above and
        below the music note which can be done by initializing the image and
        getting its rect attributes"""

        # Call the parent __init__() method
        pygame.sprite.Sprite.__init__(self)

        # Initialzing The Image and Getting the rect attributes of the sprite in order to control its direction and its starting position
        self.image = pygame.image.load("Images/TransparentRectangle.png")
        self.rect = self.image.get_rect()
        self.rect.left = 540
        self.rect.top = 0

class TransparentDot(pygame.sprite.Sprite):
    """This class defines the sprite for our Transparent Dot"""
    def __init__(self, x, y, dxMultiplier):
        """This initializer takes an x and y location,and a integer value as
        parameters for this class. It uses these parameters to make a transparent
        dot sprite and by initialzing the image and getting the sprite's rect attributes,
        this class controls the direction of our sprite too"""
        # Call the parent __init__() method
        pygame.sprite.Sprite.__init__(self)

        # Define the image attributes for our dot sprite
        self.image = pygame.image.load("Images/TransparentDot.png")

        # Get the rect attributes of the sprite and use it to control the direction and starting point
        self.rect = self.image.get_rect()
        self.rect.left = x
        self.rect.centery = y
        self.dx = 7 * dxMultiplier
        self.killSelf = False

    def killItSelf(self):
        '''This method is used to kill the sprite in the update function'''
        self.killSelf = True

    def update(self):
        '''This method will be called automatically in order to reposition our
        sprite and to allow our sprite's image to change and alternate'''

        # Causes The Dot Sprite To Continuously Go Left
        self.rect.right -= self.dx

        # Checks If The Dot Note Hits The End Of The Screen, If Yes Tell It To Delete Itself
        if self.rect.right <= 0:
            self.kill()

        # Tell The Sprite To Kill Itself
        if self.killSelf == True:
            self.kill()