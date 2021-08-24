"""Author : Mario Liao

   Date : 05/03/2019

   Description: This program is a game I made using pygame. The goal of the
   game is to survive before the song finishes and to try and earn as much
   points as you can. You lose one life for each music note you miss"""

# Initialize and Import
import pygame
import TWICE
pygame.init()
pygame.mixer.init()

def playGame(hidden, doubleTime):
    """This is the mainline logic of my program"""

    # Display
    screen = pygame.display.set_mode((1280, 720))
    pygame.display.set_caption("TWICE - Dance The Night Away (8 Bit)")

    # Entities
    background = pygame.Surface(screen.get_size())
    background = background.convert()
    background.fill((255, 255, 255))
    screen.blit(background, (0, 0))

    # Background Music and Sound Effects
    if doubleTime:
        pygame.mixer.music.load("Music/TWICE - Dance The Night Away (8 Bit) (DT).ogg")
    else:
        pygame.mixer.music.load("Music/TWICE - Dance The Night Away (8 Bit).mp3")

    pygame.mixer.music.set_volume(0.3)
    pygame.mixer.music.play(1)

    # Sprites for: Player, MusicNote, Beach, ScoreNames, ScoreImages, ScoreKeeper, BlackTop, FootPrint
    if doubleTime:
        dxMultiplier = 2.0
    else:
        dxMultiplier = 1.0

    player = TWICE.Player(screen, -550, dxMultiplier)
    beach = TWICE.Beach(screen, dxMultiplier)
    musicNote = []
    scoreNames = TWICE.ScoreNames()
    scoreImages = []
    for imageCount in range(5):
        scoreImages.append(TWICE.ScoreImages(imageCount))
    playerMessage = TWICE.ScoreKeeper("NAYEON", 0, "player", dxMultiplier)
    livesMessage = TWICE.ScoreKeeper("none", 9, "lives", dxMultiplier)
    musicNoteMessage = TWICE.ScoreKeeper("none", 0, "musicNote", dxMultiplier)
    scoreMessage = TWICE.ScoreKeeper("none", 0, "score", dxMultiplier)
    timeMessage = TWICE.ScoreKeeper("none", 0, "time", dxMultiplier)
    blackBackgroundTop = TWICE.BlackTop()
    footPrint = []
    transparentRectangle = TWICE.TransparentRectangle()
    transparentDot = []

    # Hard Code Of The Music Note Sprite Position In Order To Fit With The Song

    # Variable Used To Help Change The Colour Of The Note And The Position
    noteColour = 0
    xPos = 0
    yPos = 0

    xPos = 2272
    yPos = 360
    musicNote.append(TWICE.MusicNote(xPos, yPos, noteColour, dxMultiplier))
    noteColour += 1
    transparentDot.append(TWICE.TransparentDot(xPos, yPos, dxMultiplier))

    xPos -= 32

    xPos += 128
    yPos += 0
    musicNote.append(TWICE.MusicNote(xPos, yPos, noteColour, dxMultiplier))
    noteColour += 1
    transparentDot.append(TWICE.TransparentDot(xPos, yPos, dxMultiplier))

    xPos += 128
    yPos += 0
    musicNote.append(TWICE.MusicNote(xPos, yPos, noteColour, dxMultiplier))
    noteColour += 1
    transparentDot.append(TWICE.TransparentDot(xPos, yPos, dxMultiplier))

    xPos += 128
    yPos += 0
    musicNote.append(TWICE.MusicNote(xPos, yPos, noteColour, dxMultiplier))
    noteColour += 1
    transparentDot.append(TWICE.TransparentDot(xPos, yPos, dxMultiplier))

    xPos += 64
    yPos += 0
    musicNote.append(TWICE.MusicNote(xPos, yPos, noteColour, dxMultiplier))
    noteColour += 1
    transparentDot.append(TWICE.TransparentDot(xPos, yPos, dxMultiplier))

    xPos += 64
    yPos -= 50
    musicNote.append(TWICE.MusicNote(xPos, yPos, noteColour, dxMultiplier))
    noteColour += 1
    transparentDot.append(TWICE.TransparentDot(xPos, yPos, dxMultiplier))

    xPos += 64
    yPos -= 50
    musicNote.append(TWICE.MusicNote(xPos, yPos, noteColour, dxMultiplier))
    noteColour += 1
    transparentDot.append(TWICE.TransparentDot(xPos, yPos, dxMultiplier))

    xPos += 128
    yPos += 50
    musicNote.append(TWICE.MusicNote(xPos, yPos, noteColour, dxMultiplier))
    noteColour += 1
    transparentDot.append(TWICE.TransparentDot(xPos, yPos, dxMultiplier))

    xPos += 64
    yPos += 50
    musicNote.append(TWICE.MusicNote(xPos, yPos, noteColour, dxMultiplier))
    noteColour += 1
    transparentDot.append(TWICE.TransparentDot(xPos, yPos, dxMultiplier))

    xPos += 64
    yPos += 50
    musicNote.append(TWICE.MusicNote(xPos, yPos, noteColour, dxMultiplier))
    noteColour += 1
    transparentDot.append(TWICE.TransparentDot(xPos, yPos, dxMultiplier))

    xPos += 64
    yPos += 50
    musicNote.append(TWICE.MusicNote(xPos, yPos, noteColour, dxMultiplier))
    noteColour += 1
    transparentDot.append(TWICE.TransparentDot(xPos, yPos, dxMultiplier))

    xPos += 128
    yPos -= 50
    musicNote.append(TWICE.MusicNote(xPos, yPos, noteColour, dxMultiplier))
    noteColour += 1
    transparentDot.append(TWICE.TransparentDot(xPos, yPos, dxMultiplier))

    xPos += 64
    yPos -= 0
    musicNote.append(TWICE.MusicNote(xPos, yPos, noteColour, dxMultiplier))
    noteColour += 1
    transparentDot.append(TWICE.TransparentDot(xPos, yPos, dxMultiplier))

    xPos += 64
    yPos -= 0
    musicNote.append(TWICE.MusicNote(xPos, yPos, noteColour, dxMultiplier))
    noteColour += 1
    transparentDot.append(TWICE.TransparentDot(xPos, yPos, dxMultiplier))

    xPos += 64
    yPos -= 0
    musicNote.append(TWICE.MusicNote(xPos, yPos, noteColour, dxMultiplier))
    noteColour += 1
    transparentDot.append(TWICE.TransparentDot(xPos, yPos, dxMultiplier))

    xPos += 64
    yPos -= 0
    musicNote.append(TWICE.MusicNote(xPos, yPos, noteColour, dxMultiplier))
    noteColour += 1
    transparentDot.append(TWICE.TransparentDot(xPos, yPos, dxMultiplier))

    xPos += 64
    yPos -= 50
    musicNote.append(TWICE.MusicNote(xPos, yPos, noteColour, dxMultiplier))
    noteColour += 1
    transparentDot.append(TWICE.TransparentDot(xPos, yPos, dxMultiplier))

    xPos += 64
    yPos += 50
    musicNote.append(TWICE.MusicNote(xPos, yPos, noteColour, dxMultiplier))
    noteColour += 1
    transparentDot.append(TWICE.TransparentDot(xPos, yPos, dxMultiplier))

    xPos += 64
    yPos -= 0
    musicNote.append(TWICE.MusicNote(xPos, yPos, noteColour, dxMultiplier))
    noteColour += 1
    transparentDot.append(TWICE.TransparentDot(xPos, yPos, dxMultiplier))

    xPos += 64
    yPos += 50
    musicNote.append(TWICE.MusicNote(xPos, yPos, noteColour, dxMultiplier))
    noteColour += 1
    transparentDot.append(TWICE.TransparentDot(xPos, yPos, dxMultiplier))

    xPos += 64
    yPos -= 50
    musicNote.append(TWICE.MusicNote(xPos, yPos, noteColour, dxMultiplier))
    noteColour += 1
    transparentDot.append(TWICE.TransparentDot(xPos, yPos, dxMultiplier))

    xPos += 64
    yPos -= 50
    musicNote.append(TWICE.MusicNote(xPos, yPos, noteColour, dxMultiplier))
    noteColour += 1
    transparentDot.append(TWICE.TransparentDot(xPos, yPos, dxMultiplier))

    xPos += 64
    yPos += 50
    musicNote.append(TWICE.MusicNote(xPos, yPos, noteColour, dxMultiplier))
    noteColour += 1
    transparentDot.append(TWICE.TransparentDot(xPos, yPos, dxMultiplier))

    xPos += 64
    yPos -= 50
    musicNote.append(TWICE.MusicNote(xPos, yPos, noteColour, dxMultiplier))
    noteColour += 1
    transparentDot.append(TWICE.TransparentDot(xPos, yPos, dxMultiplier))

    xPos += 64
    yPos -= 50
    musicNote.append(TWICE.MusicNote(xPos, yPos, noteColour, dxMultiplier))
    noteColour += 1
    transparentDot.append(TWICE.TransparentDot(xPos, yPos, dxMultiplier))

    xPos += 64
    yPos += 50
    musicNote.append(TWICE.MusicNote(xPos, yPos, noteColour, dxMultiplier))
    noteColour += 1
    transparentDot.append(TWICE.TransparentDot(xPos, yPos, dxMultiplier))

    xPos += 64
    yPos += 50
    musicNote.append(TWICE.MusicNote(xPos, yPos, noteColour, dxMultiplier))
    noteColour += 2
    transparentDot.append(TWICE.TransparentDot(xPos, yPos, dxMultiplier))

    xPos += 64
    yPos += 50
    musicNote.append(TWICE.MusicNote(xPos, yPos, noteColour, dxMultiplier))
    noteColour += 1
    transparentDot.append(TWICE.TransparentDot(xPos, yPos, dxMultiplier))

    xPos += 64
    yPos -= 50
    musicNote.append(TWICE.MusicNote(xPos, yPos, noteColour, dxMultiplier))
    noteColour += 1
    transparentDot.append(TWICE.TransparentDot(xPos, yPos, dxMultiplier))

    xPos += 128
    yPos -= 0
    musicNote.append(TWICE.MusicNote(xPos, yPos, noteColour, dxMultiplier))
    noteColour += 1
    transparentDot.append(TWICE.TransparentDot(xPos, yPos, dxMultiplier))

    xPos += 64
    yPos -= 50
    musicNote.append(TWICE.MusicNote(xPos, yPos, noteColour, dxMultiplier))
    noteColour += 1
    transparentDot.append(TWICE.TransparentDot(xPos, yPos, dxMultiplier))

    xPos += 64
    yPos += 50
    musicNote.append(TWICE.MusicNote(xPos, yPos, noteColour, dxMultiplier))
    noteColour += 1
    transparentDot.append(TWICE.TransparentDot(xPos, yPos, dxMultiplier))

    xPos += 64
    yPos += 50
    musicNote.append(TWICE.MusicNote(xPos, yPos, noteColour, dxMultiplier))
    noteColour += 1
    transparentDot.append(TWICE.TransparentDot(xPos, yPos, dxMultiplier))

    xPos += 64
    yPos += 50
    musicNote.append(TWICE.MusicNote(xPos, yPos, noteColour, dxMultiplier))
    noteColour += 1
    transparentDot.append(TWICE.TransparentDot(xPos, yPos, dxMultiplier))

    xPos += 64
    yPos += 50
    musicNote.append(TWICE.MusicNote(xPos, yPos, noteColour, dxMultiplier))
    noteColour += 2
    transparentDot.append(TWICE.TransparentDot(xPos, yPos, dxMultiplier))

    xPos += 64
    yPos -= 50
    musicNote.append(TWICE.MusicNote(xPos, yPos, noteColour, dxMultiplier))
    noteColour += 1
    transparentDot.append(TWICE.TransparentDot(xPos, yPos, dxMultiplier))

    xPos += 128
    yPos -= 0
    musicNote.append(TWICE.MusicNote(xPos, yPos, noteColour, dxMultiplier))
    noteColour += 1
    transparentDot.append(TWICE.TransparentDot(xPos, yPos, dxMultiplier))

    xPos += 128
    yPos -= 0
    musicNote.append(TWICE.MusicNote(xPos, yPos, noteColour, dxMultiplier))
    noteColour += 1
    transparentDot.append(TWICE.TransparentDot(xPos, yPos, dxMultiplier))

    xPos += 64
    yPos -= 0
    musicNote.append(TWICE.MusicNote(xPos, yPos, noteColour, dxMultiplier))
    noteColour += 1
    transparentDot.append(TWICE.TransparentDot(xPos, yPos, dxMultiplier))

    xPos += 64
    yPos -= 0
    musicNote.append(TWICE.MusicNote(xPos, yPos, noteColour, dxMultiplier))
    noteColour += 1
    transparentDot.append(TWICE.TransparentDot(xPos, yPos, dxMultiplier))

    xPos += 64
    yPos -= 50
    musicNote.append(TWICE.MusicNote(xPos, yPos, noteColour, dxMultiplier))
    noteColour += 1
    transparentDot.append(TWICE.TransparentDot(xPos, yPos, dxMultiplier))

    xPos += 64
    yPos += 50
    musicNote.append(TWICE.MusicNote(xPos, yPos, noteColour, dxMultiplier))
    noteColour += 1
    transparentDot.append(TWICE.TransparentDot(xPos, yPos, dxMultiplier))

    xPos += 64
    yPos += 0
    musicNote.append(TWICE.MusicNote(xPos, yPos, noteColour, dxMultiplier))
    noteColour += 1
    transparentDot.append(TWICE.TransparentDot(xPos, yPos, dxMultiplier))

    xPos += 64
    yPos += 50
    musicNote.append(TWICE.MusicNote(xPos, yPos, noteColour, dxMultiplier))
    noteColour += 1
    transparentDot.append(TWICE.TransparentDot(xPos, yPos, dxMultiplier))

    xPos += 64
    yPos -= 50
    musicNote.append(TWICE.MusicNote(xPos, yPos, noteColour, dxMultiplier))
    noteColour += 1
    transparentDot.append(TWICE.TransparentDot(xPos, yPos, dxMultiplier))

    xPos += 64
    yPos -= 50
    musicNote.append(TWICE.MusicNote(xPos, yPos, noteColour, dxMultiplier))
    noteColour += 2
    transparentDot.append(TWICE.TransparentDot(xPos, yPos, dxMultiplier))

    xPos += 64
    yPos += 50
    musicNote.append(TWICE.MusicNote(xPos, yPos, noteColour, dxMultiplier))
    noteColour += 1
    transparentDot.append(TWICE.TransparentDot(xPos, yPos, dxMultiplier))

    xPos += 40
    yPos += 0
    musicNote.append(TWICE.MusicNote(xPos, yPos, noteColour, dxMultiplier))
    noteColour += 1
    transparentDot.append(TWICE.TransparentDot(xPos, yPos, dxMultiplier))

    xPos += 40
    yPos += 0
    musicNote.append(TWICE.MusicNote(xPos, yPos, noteColour, dxMultiplier))
    noteColour += 1
    transparentDot.append(TWICE.TransparentDot(xPos, yPos, dxMultiplier))

    xPos += 40
    yPos += 0
    musicNote.append(TWICE.MusicNote(xPos, yPos, noteColour, dxMultiplier))
    noteColour += 1
    transparentDot.append(TWICE.TransparentDot(xPos, yPos, dxMultiplier))

    xPos += 40
    yPos += 0
    musicNote.append(TWICE.MusicNote(xPos, yPos, noteColour, dxMultiplier))
    noteColour += 1
    transparentDot.append(TWICE.TransparentDot(xPos, yPos, dxMultiplier))

    xPos += 40
    yPos += 0
    musicNote.append(TWICE.MusicNote(xPos, yPos, noteColour, dxMultiplier))
    noteColour += 1
    transparentDot.append(TWICE.TransparentDot(xPos, yPos, dxMultiplier))

    xPos += 40
    yPos += 0
    musicNote.append(TWICE.MusicNote(xPos, yPos, noteColour, dxMultiplier))
    noteColour += 1
    transparentDot.append(TWICE.TransparentDot(xPos, yPos, dxMultiplier))

    xPos += 40
    yPos += 0
    musicNote.append(TWICE.MusicNote(xPos, yPos, noteColour, dxMultiplier))
    noteColour += 1
    transparentDot.append(TWICE.TransparentDot(xPos, yPos, dxMultiplier))

    xPos += 40
    yPos += 0
    musicNote.append(TWICE.MusicNote(xPos, yPos, noteColour, dxMultiplier))
    noteColour += 1
    transparentDot.append(TWICE.TransparentDot(xPos, yPos, dxMultiplier))

    xPos += 40
    yPos += 0
    musicNote.append(TWICE.MusicNote(xPos, yPos, noteColour, dxMultiplier))
    noteColour += 1
    transparentDot.append(TWICE.TransparentDot(xPos, yPos, dxMultiplier))

    xPos += 256
    yPos += 0
    musicNote.append(TWICE.MusicNote(xPos, yPos, noteColour, dxMultiplier))
    noteColour += 1
    transparentDot.append(TWICE.TransparentDot(xPos, yPos, dxMultiplier))

    xPos += 256
    yPos += 0
    musicNote.append(TWICE.MusicNote(xPos, yPos, noteColour, dxMultiplier))
    noteColour += 1
    transparentDot.append(TWICE.TransparentDot(xPos, yPos, dxMultiplier))

    xPos += 40
    yPos += 0
    musicNote.append(TWICE.MusicNote(xPos, yPos, noteColour, dxMultiplier))
    noteColour += 1
    transparentDot.append(TWICE.TransparentDot(xPos, yPos, dxMultiplier))

    xPos += 40
    yPos += 0
    musicNote.append(TWICE.MusicNote(xPos, yPos, noteColour, dxMultiplier))
    noteColour += 1
    transparentDot.append(TWICE.TransparentDot(xPos, yPos, dxMultiplier))

    xPos += 40
    yPos += 0
    musicNote.append(TWICE.MusicNote(xPos, yPos, noteColour, dxMultiplier))
    noteColour += 1
    transparentDot.append(TWICE.TransparentDot(xPos, yPos, dxMultiplier))

    xPos += 40
    yPos += 0
    musicNote.append(TWICE.MusicNote(xPos, yPos, noteColour, dxMultiplier))
    noteColour += 1
    transparentDot.append(TWICE.TransparentDot(xPos, yPos, dxMultiplier))

    xPos += 40
    yPos += 0
    musicNote.append(TWICE.MusicNote(xPos, yPos, noteColour, dxMultiplier))
    noteColour += 1
    transparentDot.append(TWICE.TransparentDot(xPos, yPos, dxMultiplier))

    xPos += 40
    yPos += 0
    musicNote.append(TWICE.MusicNote(xPos, yPos, noteColour, dxMultiplier))
    noteColour += 1
    transparentDot.append(TWICE.TransparentDot(xPos, yPos, dxMultiplier))

    xPos += 40
    yPos += 0
    musicNote.append(TWICE.MusicNote(xPos, yPos, noteColour, dxMultiplier))
    noteColour += 1
    transparentDot.append(TWICE.TransparentDot(xPos, yPos, dxMultiplier))

    xPos += 40
    yPos += 0
    musicNote.append(TWICE.MusicNote(xPos, yPos, noteColour, dxMultiplier))
    noteColour += 1
    transparentDot.append(TWICE.TransparentDot(xPos, yPos, dxMultiplier))

    xPos += 40
    yPos += 0
    musicNote.append(TWICE.MusicNote(xPos, yPos, noteColour, dxMultiplier))
    noteColour += 1
    transparentDot.append(TWICE.TransparentDot(xPos, yPos, dxMultiplier))

    xPos += 192
    yPos += 0
    musicNote.append(TWICE.MusicNote(xPos, yPos, noteColour, dxMultiplier))
    noteColour += 1
    transparentDot.append(TWICE.TransparentDot(xPos, yPos, dxMultiplier))

    xPos += 128
    yPos -= 50
    musicNote.append(TWICE.MusicNote(xPos, yPos, noteColour, dxMultiplier))
    noteColour += 1
    transparentDot.append(TWICE.TransparentDot(xPos, yPos, dxMultiplier))

    xPos += 160
    yPos -= 50
    musicNote.append(TWICE.MusicNote(xPos, yPos, noteColour, dxMultiplier))
    noteColour += 1
    transparentDot.append(TWICE.TransparentDot(xPos, yPos, dxMultiplier))

    xPos += 64
    yPos -= 50
    musicNote.append(TWICE.MusicNote(xPos, yPos, noteColour, dxMultiplier))
    noteColour += 1
    transparentDot.append(TWICE.TransparentDot(xPos, yPos, dxMultiplier))

    xPos += 64
    yPos += 50
    musicNote.append(TWICE.MusicNote(xPos, yPos, noteColour, dxMultiplier))
    noteColour += 1
    transparentDot.append(TWICE.TransparentDot(xPos, yPos, dxMultiplier))

    xPos -= 21

    xPos += 64
    yPos += 50
    musicNote.append(TWICE.MusicNote(xPos, yPos, noteColour, dxMultiplier))
    noteColour += 2
    transparentDot.append(TWICE.TransparentDot(xPos, yPos, dxMultiplier))

    xPos += 64
    yPos += 50
    musicNote.append(TWICE.MusicNote(xPos, yPos, noteColour, dxMultiplier))
    noteColour += 1
    transparentDot.append(TWICE.TransparentDot(xPos, yPos, dxMultiplier))

    xPos += 64
    yPos -= 50
    musicNote.append(TWICE.MusicNote(xPos, yPos, noteColour, dxMultiplier))
    noteColour += 1
    transparentDot.append(TWICE.TransparentDot(xPos, yPos, dxMultiplier))

    xPos += 128
    yPos -= 0
    musicNote.append(TWICE.MusicNote(xPos, yPos, noteColour, dxMultiplier))
    noteColour += 1
    transparentDot.append(TWICE.TransparentDot(xPos, yPos, dxMultiplier))

    xPos += 64
    yPos -= 50
    musicNote.append(TWICE.MusicNote(xPos, yPos, noteColour, dxMultiplier))
    noteColour += 1
    transparentDot.append(TWICE.TransparentDot(xPos, yPos, dxMultiplier))

    xPos += 64
    yPos += 50
    musicNote.append(TWICE.MusicNote(xPos, yPos, noteColour, dxMultiplier))
    noteColour += 1
    transparentDot.append(TWICE.TransparentDot(xPos, yPos, dxMultiplier))

    xPos -= 21

    xPos += 64
    yPos += 50
    musicNote.append(TWICE.MusicNote(xPos, yPos, noteColour, dxMultiplier))
    noteColour += 2
    transparentDot.append(TWICE.TransparentDot(xPos, yPos, dxMultiplier))

    xPos += 64
    yPos += 50
    musicNote.append(TWICE.MusicNote(xPos, yPos, noteColour, dxMultiplier))
    noteColour += 1
    transparentDot.append(TWICE.TransparentDot(xPos, yPos, dxMultiplier))

    xPos += 64
    yPos -= 50
    musicNote.append(TWICE.MusicNote(xPos, yPos, noteColour, dxMultiplier))
    noteColour += 1
    transparentDot.append(TWICE.TransparentDot(xPos, yPos, dxMultiplier))

    xPos += 32

    xPos += 256
    yPos += 50
    musicNote.append(TWICE.MusicNote(xPos, yPos, noteColour, dxMultiplier))
    noteColour += 1
    transparentDot.append(TWICE.TransparentDot(xPos, yPos, dxMultiplier))

    xPos += 32
    yPos -= 0
    musicNote.append(TWICE.MusicNote(xPos, yPos, noteColour, dxMultiplier))
    noteColour += 1
    transparentDot.append(TWICE.TransparentDot(xPos, yPos, dxMultiplier))

    xPos += 32
    yPos -= 0
    musicNote.append(TWICE.MusicNote(xPos, yPos, noteColour, dxMultiplier))
    noteColour += 1
    transparentDot.append(TWICE.TransparentDot(xPos, yPos, dxMultiplier))

    xPos += 32
    yPos -= 50
    musicNote.append(TWICE.MusicNote(xPos, yPos, noteColour, dxMultiplier))
    noteColour += 1
    transparentDot.append(TWICE.TransparentDot(xPos, yPos, dxMultiplier))

    xPos += 32
    yPos -= 0
    musicNote.append(TWICE.MusicNote(xPos, yPos, noteColour, dxMultiplier))
    noteColour += 1
    transparentDot.append(TWICE.TransparentDot(xPos, yPos, dxMultiplier))

    xPos += 32
    yPos -= 0
    musicNote.append(TWICE.MusicNote(xPos, yPos, noteColour, dxMultiplier))
    noteColour += 1
    transparentDot.append(TWICE.TransparentDot(xPos, yPos, dxMultiplier))

    xPos += 32
    yPos += 50
    musicNote.append(TWICE.MusicNote(xPos, yPos, noteColour, dxMultiplier))
    noteColour += 1
    transparentDot.append(TWICE.TransparentDot(xPos, yPos, dxMultiplier))

    xPos += 64
    yPos -= 50
    musicNote.append(TWICE.MusicNote(xPos, yPos, noteColour, dxMultiplier))
    noteColour += 1
    transparentDot.append(TWICE.TransparentDot(xPos, yPos, dxMultiplier))

    xPos += 128
    yPos += 0
    musicNote.append(TWICE.MusicNote(xPos, yPos, noteColour, dxMultiplier))
    noteColour += 1
    transparentDot.append(TWICE.TransparentDot(xPos, yPos, dxMultiplier))

    xPos += 32
    yPos += 50
    musicNote.append(TWICE.MusicNote(xPos, yPos, noteColour, dxMultiplier))
    noteColour += 1
    transparentDot.append(TWICE.TransparentDot(xPos, yPos, dxMultiplier))

    xPos += 48
    yPos -= 50
    musicNote.append(TWICE.MusicNote(xPos, yPos, noteColour, dxMultiplier))
    noteColour += 1
    transparentDot.append(TWICE.TransparentDot(xPos, yPos, dxMultiplier))

    xPos += 64
    yPos -= 50
    musicNote.append(TWICE.MusicNote(xPos, yPos, noteColour, dxMultiplier))
    noteColour += 1
    transparentDot.append(TWICE.TransparentDot(xPos, yPos, dxMultiplier))

    xPos += 96
    yPos -= 0
    musicNote.append(TWICE.MusicNote(xPos, yPos, noteColour, dxMultiplier))
    noteColour += 1
    transparentDot.append(TWICE.TransparentDot(xPos, yPos, dxMultiplier))

    xPos += 64
    yPos -= 50
    musicNote.append(TWICE.MusicNote(xPos, yPos, noteColour, dxMultiplier))
    noteColour += 1
    transparentDot.append(TWICE.TransparentDot(xPos, yPos, dxMultiplier))

    xPos += 64
    yPos -= 50
    musicNote.append(TWICE.MusicNote(xPos, yPos, noteColour, dxMultiplier))
    noteColour += 1
    transparentDot.append(TWICE.TransparentDot(xPos, yPos, dxMultiplier))

    xPos += 48
    yPos += 50
    musicNote.append(TWICE.MusicNote(xPos, yPos, noteColour, dxMultiplier))
    noteColour += 1
    transparentDot.append(TWICE.TransparentDot(xPos, yPos, dxMultiplier))

    xPos += 32
    yPos -= 50
    musicNote.append(TWICE.MusicNote(xPos, yPos, noteColour, dxMultiplier))
    noteColour += 1
    transparentDot.append(TWICE.TransparentDot(xPos, yPos, dxMultiplier))

    xPos += 64
    yPos -= 50
    musicNote.append(TWICE.MusicNote(xPos, yPos, noteColour, dxMultiplier))
    noteColour += 1
    transparentDot.append(TWICE.TransparentDot(xPos, yPos, dxMultiplier))

    xPos += 48
    yPos += 50
    musicNote.append(TWICE.MusicNote(xPos, yPos, noteColour, dxMultiplier))
    noteColour += 1
    transparentDot.append(TWICE.TransparentDot(xPos, yPos, dxMultiplier))

    xPos += 192
    yPos -= 50
    musicNote.append(TWICE.MusicNote(xPos, yPos, noteColour, dxMultiplier))
    noteColour += 1
    transparentDot.append(TWICE.TransparentDot(xPos, yPos, dxMultiplier))

    xPos += 64
    yPos -= 0
    musicNote.append(TWICE.MusicNote(xPos, yPos, noteColour, dxMultiplier))
    noteColour += 1
    transparentDot.append(TWICE.TransparentDot(xPos, yPos, dxMultiplier))

    xPos += 64
    yPos += 50
    musicNote.append(TWICE.MusicNote(xPos, yPos, noteColour, dxMultiplier))
    noteColour += 1
    transparentDot.append(TWICE.TransparentDot(xPos, yPos, dxMultiplier))

    xPos += 32
    yPos -= 50
    musicNote.append(TWICE.MusicNote(xPos, yPos, noteColour, dxMultiplier))
    noteColour += 1
    transparentDot.append(TWICE.TransparentDot(xPos, yPos, dxMultiplier))

    xPos += 64
    yPos -= 50
    musicNote.append(TWICE.MusicNote(xPos, yPos, noteColour, dxMultiplier))
    noteColour += 1
    transparentDot.append(TWICE.TransparentDot(xPos, yPos, dxMultiplier))

    xPos += 64
    yPos -= 50
    musicNote.append(TWICE.MusicNote(xPos, yPos, noteColour, dxMultiplier))
    noteColour += 1
    transparentDot.append(TWICE.TransparentDot(xPos, yPos, dxMultiplier))

    xPos += 96
    yPos += 50
    musicNote.append(TWICE.MusicNote(xPos, yPos, noteColour, dxMultiplier))
    noteColour += 1
    transparentDot.append(TWICE.TransparentDot(xPos, yPos, dxMultiplier))

    xPos += 64
    yPos += 0
    musicNote.append(TWICE.MusicNote(xPos, yPos, noteColour, dxMultiplier))
    noteColour += 1
    transparentDot.append(TWICE.TransparentDot(xPos, yPos, dxMultiplier))

    xPos += 64
    yPos -= 50
    musicNote.append(TWICE.MusicNote(xPos, yPos, noteColour, dxMultiplier))
    noteColour += 1
    transparentDot.append(TWICE.TransparentDot(xPos, yPos, dxMultiplier))

    xPos += 64
    yPos -= 50
    musicNote.append(TWICE.MusicNote(xPos, yPos, noteColour, dxMultiplier))
    noteColour += 1
    transparentDot.append(TWICE.TransparentDot(xPos, yPos, dxMultiplier))

    xPos += 48
    yPos += 50
    musicNote.append(TWICE.MusicNote(xPos, yPos, noteColour, dxMultiplier))
    noteColour += 1
    transparentDot.append(TWICE.TransparentDot(xPos, yPos, dxMultiplier))

    xPos += 32
    yPos -= 50
    musicNote.append(TWICE.MusicNote(xPos, yPos, noteColour, dxMultiplier))
    noteColour += 1
    transparentDot.append(TWICE.TransparentDot(xPos, yPos, dxMultiplier))

    xPos += 64
    yPos += 50
    musicNote.append(TWICE.MusicNote(xPos, yPos, noteColour, dxMultiplier))
    noteColour += 1
    transparentDot.append(TWICE.TransparentDot(xPos, yPos, dxMultiplier))

    xPos += 64
    yPos -= 50
    musicNote.append(TWICE.MusicNote(xPos, yPos, noteColour, dxMultiplier))
    noteColour += 1
    transparentDot.append(TWICE.TransparentDot(xPos, yPos, dxMultiplier))

    xPos += 96
    yPos += 50
    musicNote.append(TWICE.MusicNote(xPos, yPos, noteColour, dxMultiplier))
    noteColour += 1
    transparentDot.append(TWICE.TransparentDot(xPos, yPos, dxMultiplier))

    xPos += 64
    yPos += 50
    musicNote.append(TWICE.MusicNote(xPos, yPos, noteColour, dxMultiplier))
    noteColour -= 1
    transparentDot.append(TWICE.TransparentDot(xPos, yPos, dxMultiplier))

    xPos += 64
    yPos += 0
    musicNote.append(TWICE.MusicNote(xPos, yPos, noteColour, dxMultiplier))
    noteColour -= 1
    transparentDot.append(TWICE.TransparentDot(xPos, yPos, dxMultiplier))

    xPos += 64
    yPos += 0
    musicNote.append(TWICE.MusicNote(xPos, yPos, noteColour, dxMultiplier))
    noteColour += 1
    transparentDot.append(TWICE.TransparentDot(xPos, yPos, dxMultiplier))

    xPos += 64
    yPos += 0
    musicNote.append(TWICE.MusicNote(xPos, yPos, noteColour, dxMultiplier))
    noteColour += 1
    transparentDot.append(TWICE.TransparentDot(xPos, yPos, dxMultiplier))

    xPos += 48
    yPos -= 50
    musicNote.append(TWICE.MusicNote(xPos, yPos, noteColour, dxMultiplier))
    noteColour += 1
    transparentDot.append(TWICE.TransparentDot(xPos, yPos, dxMultiplier))

    xPos += 96
    yPos -= 0
    musicNote.append(TWICE.MusicNote(xPos, yPos, noteColour, dxMultiplier))
    noteColour += 1
    transparentDot.append(TWICE.TransparentDot(xPos, yPos, dxMultiplier))

    xPos += 96
    yPos -= 0
    musicNote.append(TWICE.MusicNote(xPos, yPos, noteColour, dxMultiplier))
    noteColour += 1
    transparentDot.append(TWICE.TransparentDot(xPos, yPos, dxMultiplier))

    xPos += 80
    yPos += 50
    musicNote.append(TWICE.MusicNote(xPos, yPos, noteColour, dxMultiplier))
    noteColour += 1
    transparentDot.append(TWICE.TransparentDot(xPos, yPos, dxMultiplier))

    xPos += 64
    yPos += 50
    musicNote.append(TWICE.MusicNote(xPos, yPos, noteColour, dxMultiplier))
    noteColour += 1
    transparentDot.append(TWICE.TransparentDot(xPos, yPos, dxMultiplier))

    xPos += 86
    yPos -= 50
    musicNote.append(TWICE.MusicNote(xPos, yPos, noteColour, dxMultiplier))
    noteColour += 1
    transparentDot.append(TWICE.TransparentDot(xPos, yPos, dxMultiplier))

    xPos += 64
    yPos -= 0
    musicNote.append(TWICE.MusicNote(xPos, yPos, noteColour, dxMultiplier))
    noteColour += 1
    transparentDot.append(TWICE.TransparentDot(xPos, yPos, dxMultiplier))

    xPos += 64
    yPos -= 50
    musicNote.append(TWICE.MusicNote(xPos, yPos, noteColour, dxMultiplier))
    noteColour += 1
    transparentDot.append(TWICE.TransparentDot(xPos, yPos, dxMultiplier))

    xPos += 64
    yPos += 50
    musicNote.append(TWICE.MusicNote(xPos, yPos, noteColour, dxMultiplier))
    noteColour += 1
    transparentDot.append(TWICE.TransparentDot(xPos, yPos, dxMultiplier))

    xPos += 48
    yPos += 50
    musicNote.append(TWICE.MusicNote(xPos, yPos, noteColour, dxMultiplier))
    noteColour += 1
    transparentDot.append(TWICE.TransparentDot(xPos, yPos, dxMultiplier))

    xPos += 96
    yPos += 50
    musicNote.append(TWICE.MusicNote(xPos, yPos, noteColour, dxMultiplier))
    noteColour += 1
    transparentDot.append(TWICE.TransparentDot(xPos, yPos, dxMultiplier))

    xPos += 64
    yPos -= 50
    musicNote.append(TWICE.MusicNote(xPos, yPos, noteColour, dxMultiplier))
    noteColour += 1
    transparentDot.append(TWICE.TransparentDot(xPos, yPos, dxMultiplier))

    xPos += 64
    yPos -= 50
    musicNote.append(TWICE.MusicNote(xPos, yPos, noteColour, dxMultiplier))
    noteColour += 1
    transparentDot.append(TWICE.TransparentDot(xPos, yPos, dxMultiplier))

    xPos += 48
    yPos += 50
    musicNote.append(TWICE.MusicNote(xPos, yPos, noteColour, dxMultiplier))
    noteColour += 1
    transparentDot.append(TWICE.TransparentDot(xPos, yPos, dxMultiplier))

    xPos += 32
    yPos -= 50
    musicNote.append(TWICE.MusicNote(xPos, yPos, noteColour, dxMultiplier))
    noteColour += 1
    transparentDot.append(TWICE.TransparentDot(xPos, yPos, dxMultiplier))

    xPos += 64
    yPos -= 50
    musicNote.append(TWICE.MusicNote(xPos, yPos, noteColour, dxMultiplier))
    noteColour += 1
    transparentDot.append(TWICE.TransparentDot(xPos, yPos, dxMultiplier))

    xPos += 48
    yPos += 50
    musicNote.append(TWICE.MusicNote(xPos, yPos, noteColour, dxMultiplier))
    noteColour += 1
    transparentDot.append(TWICE.TransparentDot(xPos, yPos, dxMultiplier))

    xPos += 64
    yPos += 0
    musicNote.append(TWICE.MusicNote(xPos, yPos, noteColour, dxMultiplier))
    noteColour += 1
    transparentDot.append(TWICE.TransparentDot(xPos, yPos, dxMultiplier))

    xPos += 32
    yPos -= 50
    musicNote.append(TWICE.MusicNote(xPos, yPos, noteColour, dxMultiplier))
    noteColour += 1
    transparentDot.append(TWICE.TransparentDot(xPos, yPos, dxMultiplier))

    xPos += 256
    yPos -= 0
    musicNote.append(TWICE.MusicNote(xPos, yPos, noteColour, dxMultiplier))
    noteColour += 1
    transparentDot.append(TWICE.TransparentDot(xPos, yPos, dxMultiplier))

    xPos += 64
    yPos += 50
    musicNote.append(TWICE.MusicNote(xPos, yPos, noteColour, dxMultiplier))
    noteColour += 1
    transparentDot.append(TWICE.TransparentDot(xPos, yPos, dxMultiplier))

    xPos += 64
    yPos -= 50
    musicNote.append(TWICE.MusicNote(xPos, yPos, noteColour, dxMultiplier))
    noteColour += 1
    transparentDot.append(TWICE.TransparentDot(xPos, yPos, dxMultiplier))

    xPos += 32
    yPos -= 50
    musicNote.append(TWICE.MusicNote(xPos, yPos, noteColour, dxMultiplier))
    noteColour += 1
    transparentDot.append(TWICE.TransparentDot(xPos, yPos, dxMultiplier))

    xPos += 48
    yPos += 50
    musicNote.append(TWICE.MusicNote(xPos, yPos, noteColour, dxMultiplier))
    noteColour += 1
    transparentDot.append(TWICE.TransparentDot(xPos, yPos, dxMultiplier))

    xPos += 32
    yPos -= 50
    musicNote.append(TWICE.MusicNote(xPos, yPos, noteColour, dxMultiplier))
    noteColour += 1
    transparentDot.append(TWICE.TransparentDot(xPos, yPos, dxMultiplier))

    xPos += 608
    yPos += 50
    musicNote.append(TWICE.MusicNote(xPos, yPos, noteColour, dxMultiplier))
    noteColour += 1
    transparentDot.append(TWICE.TransparentDot(xPos, yPos, dxMultiplier))

    xPos += 48
    yPos -= 50
    musicNote.append(TWICE.MusicNote(xPos, yPos, noteColour, dxMultiplier))
    noteColour += 1
    transparentDot.append(TWICE.TransparentDot(xPos, yPos, dxMultiplier))

    xPos += 48
    yPos += 50
    musicNote.append(TWICE.MusicNote(xPos, yPos, noteColour, dxMultiplier))
    noteColour += 1
    transparentDot.append(TWICE.TransparentDot(xPos, yPos, dxMultiplier))

    xPos += 32
    yPos += 50
    musicNote.append(TWICE.MusicNote(xPos, yPos, noteColour, dxMultiplier))
    noteColour += 1
    transparentDot.append(TWICE.TransparentDot(xPos, yPos, dxMultiplier))

    xPos += 48
    yPos += 50
    musicNote.append(TWICE.MusicNote(xPos, yPos, noteColour, dxMultiplier))
    noteColour += 1
    transparentDot.append(TWICE.TransparentDot(xPos, yPos, dxMultiplier))

    xPos += 48
    yPos += 0
    musicNote.append(TWICE.MusicNote(xPos, yPos, noteColour, dxMultiplier))
    noteColour += 1
    transparentDot.append(TWICE.TransparentDot(xPos, yPos, dxMultiplier))

    xPos += 608
    yPos -= 50
    musicNote.append(TWICE.MusicNote(xPos, yPos, noteColour, dxMultiplier))
    noteColour += 1
    transparentDot.append(TWICE.TransparentDot(xPos, yPos, dxMultiplier))

    xPos += 64
    yPos += 50
    musicNote.append(TWICE.MusicNote(xPos, yPos, noteColour, dxMultiplier))
    noteColour += 1
    transparentDot.append(TWICE.TransparentDot(xPos, yPos, dxMultiplier))

    xPos += 128
    yPos += 50
    musicNote.append(TWICE.MusicNote(xPos, yPos, noteColour, dxMultiplier))
    noteColour += 1
    transparentDot.append(TWICE.TransparentDot(xPos, yPos, dxMultiplier))

    xPos += 64
    yPos -= 50
    musicNote.append(TWICE.MusicNote(xPos, yPos, noteColour, dxMultiplier))
    noteColour += 1
    transparentDot.append(TWICE.TransparentDot(xPos, yPos, dxMultiplier))

    xPos += 64
    yPos -= 0
    musicNote.append(TWICE.MusicNote(xPos, yPos, noteColour, dxMultiplier))
    noteColour += 1
    transparentDot.append(TWICE.TransparentDot(xPos, yPos, dxMultiplier))

    xPos += 64
    yPos -= 0
    musicNote.append(TWICE.MusicNote(xPos, yPos, noteColour, dxMultiplier))
    noteColour += 1
    transparentDot.append(TWICE.TransparentDot(xPos, yPos, dxMultiplier))

    xPos += 80
    yPos += 50
    musicNote.append(TWICE.MusicNote(xPos, yPos, noteColour, dxMultiplier))
    noteColour += 1
    transparentDot.append(TWICE.TransparentDot(xPos, yPos, dxMultiplier))

    xPos += 64
    yPos += 50
    musicNote.append(TWICE.MusicNote(xPos, yPos, noteColour, dxMultiplier))
    noteColour += 1
    transparentDot.append(TWICE.TransparentDot(xPos, yPos, dxMultiplier))

    xPos += 64
    yPos -= 50
    musicNote.append(TWICE.MusicNote(xPos, yPos, noteColour, dxMultiplier))
    noteColour += 1
    transparentDot.append(TWICE.TransparentDot(xPos, yPos, dxMultiplier))

    xPos += 64
    yPos -= 0
    musicNote.append(TWICE.MusicNote(xPos, yPos, noteColour, dxMultiplier))
    noteColour += 1
    transparentDot.append(TWICE.TransparentDot(xPos, yPos, dxMultiplier))

    xPos += 64
    yPos -= 50
    musicNote.append(TWICE.MusicNote(xPos, yPos, noteColour, dxMultiplier))
    noteColour += 1
    transparentDot.append(TWICE.TransparentDot(xPos, yPos, dxMultiplier))

    xPos += 96
    yPos += 50
    musicNote.append(TWICE.MusicNote(xPos, yPos, noteColour, dxMultiplier))
    noteColour += 1
    transparentDot.append(TWICE.TransparentDot(xPos, yPos, dxMultiplier))

    xPos += 64
    yPos += 50
    musicNote.append(TWICE.MusicNote(xPos, yPos, noteColour, dxMultiplier))
    noteColour += 1
    transparentDot.append(TWICE.TransparentDot(xPos, yPos, dxMultiplier))

    xPos += 128
    yPos += 50
    musicNote.append(TWICE.MusicNote(xPos, yPos, noteColour, dxMultiplier))
    noteColour += 1
    transparentDot.append(TWICE.TransparentDot(xPos, yPos, dxMultiplier))

    xPos += 64
    yPos -= 50
    musicNote.append(TWICE.MusicNote(xPos, yPos, noteColour, dxMultiplier))
    noteColour += 1
    transparentDot.append(TWICE.TransparentDot(xPos, yPos, dxMultiplier))

    xPos += 64
    yPos -= 50
    musicNote.append(TWICE.MusicNote(xPos, yPos, noteColour, dxMultiplier))
    noteColour += 1
    transparentDot.append(TWICE.TransparentDot(xPos, yPos, dxMultiplier))

    xPos += 48
    yPos += 50
    musicNote.append(TWICE.MusicNote(xPos, yPos, noteColour, dxMultiplier))
    noteColour += 1
    transparentDot.append(TWICE.TransparentDot(xPos, yPos, dxMultiplier))

    xPos += 48
    yPos -= 50
    musicNote.append(TWICE.MusicNote(xPos, yPos, noteColour, dxMultiplier))
    noteColour += 1
    transparentDot.append(TWICE.TransparentDot(xPos, yPos, dxMultiplier))

    xPos += 64
    yPos -= 50
    musicNote.append(TWICE.MusicNote(xPos, yPos, noteColour, dxMultiplier))
    noteColour += 1
    transparentDot.append(TWICE.TransparentDot(xPos, yPos, dxMultiplier))

    xPos += 64
    yPos -= 50
    musicNote.append(TWICE.MusicNote(xPos, yPos, noteColour, dxMultiplier))
    noteColour += 1
    transparentDot.append(TWICE.TransparentDot(xPos, yPos, dxMultiplier))

    xPos += 320
    yPos += 50
    musicNote.append(TWICE.MusicNote(xPos, yPos, noteColour, dxMultiplier))
    noteColour += 1
    transparentDot.append(TWICE.TransparentDot(xPos, yPos, dxMultiplier))

    xPos += 48
    yPos -= 50
    musicNote.append(TWICE.MusicNote(xPos, yPos, noteColour, dxMultiplier))
    noteColour += 1
    transparentDot.append(TWICE.TransparentDot(xPos, yPos, dxMultiplier))

    xPos += 48
    yPos += 50
    musicNote.append(TWICE.MusicNote(xPos, yPos, noteColour, dxMultiplier))
    noteColour += 1
    transparentDot.append(TWICE.TransparentDot(xPos, yPos, dxMultiplier))

    xPos += 32
    yPos += 50
    musicNote.append(TWICE.MusicNote(xPos, yPos, noteColour, dxMultiplier))
    noteColour += 1
    transparentDot.append(TWICE.TransparentDot(xPos, yPos, dxMultiplier))

    xPos += 48
    yPos += 50
    musicNote.append(TWICE.MusicNote(xPos, yPos, noteColour, dxMultiplier))
    noteColour += 1
    transparentDot.append(TWICE.TransparentDot(xPos, yPos, dxMultiplier))

    xPos += 32
    yPos += 0
    musicNote.append(TWICE.MusicNote(xPos, yPos, noteColour, dxMultiplier))
    noteColour += 1
    transparentDot.append(TWICE.TransparentDot(xPos, yPos, dxMultiplier))

    xPos += 48
    yPos -= 50
    musicNote.append(TWICE.MusicNote(xPos, yPos, noteColour, dxMultiplier))
    noteColour += 1
    transparentDot.append(TWICE.TransparentDot(xPos, yPos, dxMultiplier))

    xPos += 96
    yPos += 50
    musicNote.append(TWICE.MusicNote(xPos, yPos, noteColour, dxMultiplier))
    noteColour += 1
    transparentDot.append(TWICE.TransparentDot(xPos, yPos, dxMultiplier))

    xPos += 96
    yPos += 50
    musicNote.append(TWICE.MusicNote(xPos, yPos, noteColour, dxMultiplier))
    noteColour += 1
    transparentDot.append(TWICE.TransparentDot(xPos, yPos, dxMultiplier))

    xPos += 64
    yPos += 50
    musicNote.append(TWICE.MusicNote(xPos, yPos, noteColour, dxMultiplier))
    noteColour += 1
    transparentDot.append(TWICE.TransparentDot(xPos, yPos, dxMultiplier))

    xPos += 32
    yPos += 0
    musicNote.append(TWICE.MusicNote(xPos, yPos, noteColour, dxMultiplier))
    noteColour += 1
    transparentDot.append(TWICE.TransparentDot(xPos, yPos, dxMultiplier))

    xPos += 64
    yPos += 0
    musicNote.append(TWICE.MusicNote(xPos, yPos, noteColour, dxMultiplier))
    noteColour += 1
    transparentDot.append(TWICE.TransparentDot(xPos, yPos, dxMultiplier))

    xPos += 48
    yPos -= 50
    musicNote.append(TWICE.MusicNote(xPos, yPos, noteColour, dxMultiplier))
    noteColour += 1
    transparentDot.append(TWICE.TransparentDot(xPos, yPos, dxMultiplier))

    xPos += 64
    yPos -= 50
    musicNote.append(TWICE.MusicNote(xPos, yPos, noteColour, dxMultiplier))
    noteColour += 1
    transparentDot.append(TWICE.TransparentDot(xPos, yPos, dxMultiplier))

    xPos += 64
    yPos -= 50
    musicNote.append(TWICE.MusicNote(xPos, yPos, noteColour, dxMultiplier))
    noteColour += 1
    transparentDot.append(TWICE.TransparentDot(xPos, yPos, dxMultiplier))

    xPos += 64
    yPos -= 50
    musicNote.append(TWICE.MusicNote(xPos, yPos, noteColour, dxMultiplier))
    noteColour += 1
    transparentDot.append(TWICE.TransparentDot(xPos, yPos, dxMultiplier))

    xPos += 32
    yPos -= 0
    musicNote.append(TWICE.MusicNote(xPos, yPos, noteColour, dxMultiplier))
    noteColour += 1
    transparentDot.append(TWICE.TransparentDot(xPos, yPos, dxMultiplier))

    xPos += 224
    yPos -= 50
    musicNote.append(TWICE.MusicNote(xPos, yPos, noteColour, dxMultiplier))
    noteColour += 1
    transparentDot.append(TWICE.TransparentDot(xPos, yPos, dxMultiplier))

    xPos += 96
    yPos += 50
    musicNote.append(TWICE.MusicNote(xPos, yPos, noteColour, dxMultiplier))
    noteColour += 1
    transparentDot.append(TWICE.TransparentDot(xPos, yPos, dxMultiplier))

    xPos += 96
    yPos += 50
    musicNote.append(TWICE.MusicNote(xPos, yPos, noteColour, dxMultiplier))
    noteColour += 1
    transparentDot.append(TWICE.TransparentDot(xPos, yPos, dxMultiplier))

    xPos += 48
    yPos += 50
    musicNote.append(TWICE.MusicNote(xPos, yPos, noteColour, dxMultiplier))
    noteColour += 1
    transparentDot.append(TWICE.TransparentDot(xPos, yPos, dxMultiplier))

    xPos += 32
    yPos += 0
    musicNote.append(TWICE.MusicNote(xPos, yPos, noteColour, dxMultiplier))
    noteColour += 1
    transparentDot.append(TWICE.TransparentDot(xPos, yPos, dxMultiplier))

    xPos += 64
    yPos += 0
    musicNote.append(TWICE.MusicNote(xPos, yPos, noteColour, dxMultiplier))
    noteColour += 1
    transparentDot.append(TWICE.TransparentDot(xPos, yPos, dxMultiplier))

    xPos += 48
    yPos -= 50
    musicNote.append(TWICE.MusicNote(xPos, yPos, noteColour, dxMultiplier))
    noteColour += 1
    transparentDot.append(TWICE.TransparentDot(xPos, yPos, dxMultiplier))

    xPos += 64
    yPos += 50
    musicNote.append(TWICE.MusicNote(xPos, yPos, noteColour, dxMultiplier))
    noteColour += 1
    transparentDot.append(TWICE.TransparentDot(xPos, yPos, dxMultiplier))

    xPos += 64
    yPos += 50
    musicNote.append(TWICE.MusicNote(xPos, yPos, noteColour, dxMultiplier))
    noteColour += 1
    transparentDot.append(TWICE.TransparentDot(xPos, yPos, dxMultiplier))

    xPos += 64
    yPos += 50
    musicNote.append(TWICE.MusicNote(xPos, yPos, noteColour, dxMultiplier))
    noteColour += 1
    transparentDot.append(TWICE.TransparentDot(xPos, yPos, dxMultiplier))

    xPos += 32
    yPos += 0
    musicNote.append(TWICE.MusicNote(xPos, yPos, noteColour, dxMultiplier))
    noteColour += 1
    transparentDot.append(TWICE.TransparentDot(xPos, yPos, dxMultiplier))

    xPos += 196
    yPos = 360
    musicNote.append(TWICE.MusicNote(xPos, yPos, noteColour, dxMultiplier))
    noteColour += 1
    transparentDot.append(TWICE.TransparentDot(xPos, yPos, dxMultiplier))

    xPos -= 64

    xPos += 128
    yPos += 0
    musicNote.append(TWICE.MusicNote(xPos, yPos, noteColour, dxMultiplier))
    noteColour += 1
    transparentDot.append(TWICE.TransparentDot(xPos, yPos, dxMultiplier))

    xPos -= 64

    xPos += 128
    yPos += 0
    musicNote.append(TWICE.MusicNote(xPos, yPos, noteColour, dxMultiplier))
    noteColour += 1
    transparentDot.append(TWICE.TransparentDot(xPos, yPos, dxMultiplier))

    xPos += 128
    yPos += 0
    musicNote.append(TWICE.MusicNote(xPos, yPos, noteColour, dxMultiplier))
    noteColour += 1
    transparentDot.append(TWICE.TransparentDot(xPos, yPos, dxMultiplier))

    xPos += 64
    yPos += 0
    musicNote.append(TWICE.MusicNote(xPos, yPos, noteColour, dxMultiplier))
    noteColour += 1
    transparentDot.append(TWICE.TransparentDot(xPos, yPos, dxMultiplier))

    xPos += 64
    yPos -= 50
    musicNote.append(TWICE.MusicNote(xPos, yPos, noteColour, dxMultiplier))
    noteColour += 1
    transparentDot.append(TWICE.TransparentDot(xPos, yPos, dxMultiplier))

    xPos += 64
    yPos -= 50
    musicNote.append(TWICE.MusicNote(xPos, yPos, noteColour, dxMultiplier))
    noteColour += 1
    transparentDot.append(TWICE.TransparentDot(xPos, yPos, dxMultiplier))

    xPos += 128
    yPos += 50
    musicNote.append(TWICE.MusicNote(xPos, yPos, noteColour, dxMultiplier))
    noteColour += 1
    transparentDot.append(TWICE.TransparentDot(xPos, yPos, dxMultiplier))

    xPos += 64
    yPos += 50
    musicNote.append(TWICE.MusicNote(xPos, yPos, noteColour, dxMultiplier))
    noteColour += 1
    transparentDot.append(TWICE.TransparentDot(xPos, yPos, dxMultiplier))

    xPos += 64
    yPos += 50
    musicNote.append(TWICE.MusicNote(xPos, yPos, noteColour, dxMultiplier))
    noteColour += 1
    transparentDot.append(TWICE.TransparentDot(xPos, yPos, dxMultiplier))

    xPos += 64
    yPos += 50
    musicNote.append(TWICE.MusicNote(xPos, yPos, noteColour, dxMultiplier))
    noteColour += 1
    transparentDot.append(TWICE.TransparentDot(xPos, yPos, dxMultiplier))

    xPos -= 32

    xPos += 128
    yPos -= 50
    musicNote.append(TWICE.MusicNote(xPos, yPos, noteColour, dxMultiplier))
    noteColour += 1
    transparentDot.append(TWICE.TransparentDot(xPos, yPos, dxMultiplier))

    xPos += 64
    yPos -= 0
    musicNote.append(TWICE.MusicNote(xPos, yPos, noteColour, dxMultiplier))
    noteColour += 1
    transparentDot.append(TWICE.TransparentDot(xPos, yPos, dxMultiplier))

    xPos += 64
    yPos -= 0
    musicNote.append(TWICE.MusicNote(xPos, yPos, noteColour, dxMultiplier))
    noteColour += 1
    transparentDot.append(TWICE.TransparentDot(xPos, yPos, dxMultiplier))

    xPos += 64
    yPos -= 0
    musicNote.append(TWICE.MusicNote(xPos, yPos, noteColour, dxMultiplier))
    noteColour += 1
    transparentDot.append(TWICE.TransparentDot(xPos, yPos, dxMultiplier))

    xPos += 64
    yPos -= 0
    musicNote.append(TWICE.MusicNote(xPos, yPos, noteColour, dxMultiplier))
    noteColour += 1
    transparentDot.append(TWICE.TransparentDot(xPos, yPos, dxMultiplier))

    xPos += 64
    yPos -= 50
    musicNote.append(TWICE.MusicNote(xPos, yPos, noteColour, dxMultiplier))
    noteColour += 1
    transparentDot.append(TWICE.TransparentDot(xPos, yPos, dxMultiplier))

    xPos += 64
    yPos += 50
    musicNote.append(TWICE.MusicNote(xPos, yPos, noteColour, dxMultiplier))
    noteColour += 1
    transparentDot.append(TWICE.TransparentDot(xPos, yPos, dxMultiplier))

    xPos += 64
    yPos -= 0
    musicNote.append(TWICE.MusicNote(xPos, yPos, noteColour, dxMultiplier))
    noteColour += 1
    transparentDot.append(TWICE.TransparentDot(xPos, yPos, dxMultiplier))

    xPos += 64
    yPos += 50
    musicNote.append(TWICE.MusicNote(xPos, yPos, noteColour, dxMultiplier))
    noteColour += 1
    transparentDot.append(TWICE.TransparentDot(xPos, yPos, dxMultiplier))

    xPos += 64
    yPos -= 50
    musicNote.append(TWICE.MusicNote(xPos, yPos, noteColour, dxMultiplier))
    noteColour += 1
    transparentDot.append(TWICE.TransparentDot(xPos, yPos, dxMultiplier))

    xPos += 64
    yPos -= 50
    musicNote.append(TWICE.MusicNote(xPos, yPos, noteColour, dxMultiplier))
    noteColour += 1
    transparentDot.append(TWICE.TransparentDot(xPos, yPos, dxMultiplier))

    xPos += 64
    yPos += 50
    musicNote.append(TWICE.MusicNote(xPos, yPos, noteColour, dxMultiplier))
    noteColour += 1
    transparentDot.append(TWICE.TransparentDot(xPos, yPos, dxMultiplier))

    xPos += 64
    yPos -= 50
    musicNote.append(TWICE.MusicNote(xPos, yPos, noteColour, dxMultiplier))
    noteColour += 1
    transparentDot.append(TWICE.TransparentDot(xPos, yPos, dxMultiplier))

    xPos += 64
    yPos -= 50
    musicNote.append(TWICE.MusicNote(xPos, yPos, noteColour, dxMultiplier))
    noteColour += 1
    transparentDot.append(TWICE.TransparentDot(xPos, yPos, dxMultiplier))

    xPos += 64
    yPos += 50
    musicNote.append(TWICE.MusicNote(xPos, yPos, noteColour, dxMultiplier))
    noteColour += 1
    transparentDot.append(TWICE.TransparentDot(xPos, yPos, dxMultiplier))

    xPos += 64
    yPos += 50
    musicNote.append(TWICE.MusicNote(xPos, yPos, noteColour, dxMultiplier))
    noteColour += 2
    transparentDot.append(TWICE.TransparentDot(xPos, yPos, dxMultiplier))

    xPos += 64
    yPos += 50
    musicNote.append(TWICE.MusicNote(xPos, yPos, noteColour, dxMultiplier))
    noteColour += 1
    transparentDot.append(TWICE.TransparentDot(xPos, yPos, dxMultiplier))

    xPos += 64
    yPos -= 50
    musicNote.append(TWICE.MusicNote(xPos, yPos, noteColour, dxMultiplier))
    noteColour += 1
    transparentDot.append(TWICE.TransparentDot(xPos, yPos, dxMultiplier))

    xPos -= 32

    xPos += 128
    yPos -= 0
    musicNote.append(TWICE.MusicNote(xPos, yPos, noteColour, dxMultiplier))
    noteColour += 1
    transparentDot.append(TWICE.TransparentDot(xPos, yPos, dxMultiplier))

    xPos += 64
    yPos -= 50
    musicNote.append(TWICE.MusicNote(xPos, yPos, noteColour, dxMultiplier))
    noteColour += 1
    transparentDot.append(TWICE.TransparentDot(xPos, yPos, dxMultiplier))

    xPos += 64
    yPos += 50
    musicNote.append(TWICE.MusicNote(xPos, yPos, noteColour, dxMultiplier))
    noteColour += 1
    transparentDot.append(TWICE.TransparentDot(xPos, yPos, dxMultiplier))

    xPos += 64
    yPos += 50
    musicNote.append(TWICE.MusicNote(xPos, yPos, noteColour, dxMultiplier))
    noteColour += 1
    transparentDot.append(TWICE.TransparentDot(xPos, yPos, dxMultiplier))

    xPos += 64
    yPos += 50
    musicNote.append(TWICE.MusicNote(xPos, yPos, noteColour, dxMultiplier))
    noteColour += 1
    transparentDot.append(TWICE.TransparentDot(xPos, yPos, dxMultiplier))

    xPos += 64
    yPos += 50
    musicNote.append(TWICE.MusicNote(xPos, yPos, noteColour, dxMultiplier))
    noteColour += 1
    transparentDot.append(TWICE.TransparentDot(xPos, yPos, dxMultiplier))

    xPos += 64
    yPos -= 50
    musicNote.append(TWICE.MusicNote(xPos, yPos, noteColour, dxMultiplier))
    noteColour += 1
    transparentDot.append(TWICE.TransparentDot(xPos, yPos, dxMultiplier))

    xPos += 15

    xPos += 224
    yPos += 50
    musicNote.append(TWICE.MusicNote(xPos, yPos, noteColour, dxMultiplier))
    noteColour += 1
    transparentDot.append(TWICE.TransparentDot(xPos, yPos, dxMultiplier))

    xPos += 32
    yPos -= 0
    musicNote.append(TWICE.MusicNote(xPos, yPos, noteColour, dxMultiplier))
    noteColour += 1
    transparentDot.append(TWICE.TransparentDot(xPos, yPos, dxMultiplier))

    xPos += 32
    yPos -= 0
    musicNote.append(TWICE.MusicNote(xPos, yPos, noteColour, dxMultiplier))
    noteColour += 1
    transparentDot.append(TWICE.TransparentDot(xPos, yPos, dxMultiplier))

    xPos += 32
    yPos -= 50
    musicNote.append(TWICE.MusicNote(xPos, yPos, noteColour, dxMultiplier))
    noteColour += 1
    transparentDot.append(TWICE.TransparentDot(xPos, yPos, dxMultiplier))

    xPos += 32
    yPos -= 0
    musicNote.append(TWICE.MusicNote(xPos, yPos, noteColour, dxMultiplier))
    noteColour += 1
    transparentDot.append(TWICE.TransparentDot(xPos, yPos, dxMultiplier))

    xPos += 32
    yPos -= 0
    musicNote.append(TWICE.MusicNote(xPos, yPos, noteColour, dxMultiplier))
    noteColour += 1
    transparentDot.append(TWICE.TransparentDot(xPos, yPos, dxMultiplier))

    xPos += 32
    yPos += 50
    musicNote.append(TWICE.MusicNote(xPos, yPos, noteColour, dxMultiplier))
    noteColour += 1
    transparentDot.append(TWICE.TransparentDot(xPos, yPos, dxMultiplier))

    xPos += 64
    yPos -= 50
    musicNote.append(TWICE.MusicNote(xPos, yPos, noteColour, dxMultiplier))
    noteColour += 1
    transparentDot.append(TWICE.TransparentDot(xPos, yPos, dxMultiplier))

    xPos += 128
    yPos += 0
    musicNote.append(TWICE.MusicNote(xPos, yPos, noteColour, dxMultiplier))
    noteColour += 1
    transparentDot.append(TWICE.TransparentDot(xPos, yPos, dxMultiplier))

    xPos += 32
    yPos += 50
    musicNote.append(TWICE.MusicNote(xPos, yPos, noteColour, dxMultiplier))
    noteColour += 1
    transparentDot.append(TWICE.TransparentDot(xPos, yPos, dxMultiplier))

    xPos += 48
    yPos -= 50
    musicNote.append(TWICE.MusicNote(xPos, yPos, noteColour, dxMultiplier))
    noteColour += 1
    transparentDot.append(TWICE.TransparentDot(xPos, yPos, dxMultiplier))

    xPos += 64
    yPos -= 50
    musicNote.append(TWICE.MusicNote(xPos, yPos, noteColour, dxMultiplier))
    noteColour += 1
    transparentDot.append(TWICE.TransparentDot(xPos, yPos, dxMultiplier))

    xPos += 96
    yPos -= 0
    musicNote.append(TWICE.MusicNote(xPos, yPos, noteColour, dxMultiplier))
    noteColour += 1
    transparentDot.append(TWICE.TransparentDot(xPos, yPos, dxMultiplier))

    xPos += 64
    yPos -= 50
    musicNote.append(TWICE.MusicNote(xPos, yPos, noteColour, dxMultiplier))
    noteColour += 1
    transparentDot.append(TWICE.TransparentDot(xPos, yPos, dxMultiplier))

    xPos += 64
    yPos -= 50
    musicNote.append(TWICE.MusicNote(xPos, yPos, noteColour, dxMultiplier))
    noteColour += 1
    transparentDot.append(TWICE.TransparentDot(xPos, yPos, dxMultiplier))

    xPos += 48
    yPos += 50
    musicNote.append(TWICE.MusicNote(xPos, yPos, noteColour, dxMultiplier))
    noteColour += 1
    transparentDot.append(TWICE.TransparentDot(xPos, yPos, dxMultiplier))

    xPos += 32
    yPos -= 50
    musicNote.append(TWICE.MusicNote(xPos, yPos, noteColour, dxMultiplier))
    noteColour += 1
    transparentDot.append(TWICE.TransparentDot(xPos, yPos, dxMultiplier))

    xPos += 64
    yPos -= 50
    musicNote.append(TWICE.MusicNote(xPos, yPos, noteColour, dxMultiplier))
    noteColour += 1
    transparentDot.append(TWICE.TransparentDot(xPos, yPos, dxMultiplier))

    xPos += 48
    yPos += 50
    musicNote.append(TWICE.MusicNote(xPos, yPos, noteColour, dxMultiplier))
    noteColour += 1
    transparentDot.append(TWICE.TransparentDot(xPos, yPos, dxMultiplier))

    xPos += 192
    yPos -= 50
    musicNote.append(TWICE.MusicNote(xPos, yPos, noteColour, dxMultiplier))
    noteColour += 1
    transparentDot.append(TWICE.TransparentDot(xPos, yPos, dxMultiplier))

    xPos += 64
    yPos -= 0
    musicNote.append(TWICE.MusicNote(xPos, yPos, noteColour, dxMultiplier))
    noteColour += 1
    transparentDot.append(TWICE.TransparentDot(xPos, yPos, dxMultiplier))

    xPos += 64
    yPos += 50
    musicNote.append(TWICE.MusicNote(xPos, yPos, noteColour, dxMultiplier))
    noteColour += 1
    transparentDot.append(TWICE.TransparentDot(xPos, yPos, dxMultiplier))

    xPos += 32
    yPos -= 50
    musicNote.append(TWICE.MusicNote(xPos, yPos, noteColour, dxMultiplier))
    noteColour += 1
    transparentDot.append(TWICE.TransparentDot(xPos, yPos, dxMultiplier))

    xPos += 64
    yPos -= 50
    musicNote.append(TWICE.MusicNote(xPos, yPos, noteColour, dxMultiplier))
    noteColour += 1
    transparentDot.append(TWICE.TransparentDot(xPos, yPos, dxMultiplier))

    xPos += 64
    yPos -= 50
    musicNote.append(TWICE.MusicNote(xPos, yPos, noteColour, dxMultiplier))
    noteColour += 1
    transparentDot.append(TWICE.TransparentDot(xPos, yPos, dxMultiplier))

    xPos += 96
    yPos += 50
    musicNote.append(TWICE.MusicNote(xPos, yPos, noteColour, dxMultiplier))
    noteColour += 1
    transparentDot.append(TWICE.TransparentDot(xPos, yPos, dxMultiplier))

    xPos += 64
    yPos += 0
    musicNote.append(TWICE.MusicNote(xPos, yPos, noteColour, dxMultiplier))
    noteColour += 1
    transparentDot.append(TWICE.TransparentDot(xPos, yPos, dxMultiplier))

    xPos += 64
    yPos -= 50
    musicNote.append(TWICE.MusicNote(xPos, yPos, noteColour, dxMultiplier))
    noteColour += 1
    transparentDot.append(TWICE.TransparentDot(xPos, yPos, dxMultiplier))

    xPos += 64
    yPos -= 50
    musicNote.append(TWICE.MusicNote(xPos, yPos, noteColour, dxMultiplier))
    noteColour += 1
    transparentDot.append(TWICE.TransparentDot(xPos, yPos, dxMultiplier))

    xPos += 48
    yPos += 50
    musicNote.append(TWICE.MusicNote(xPos, yPos, noteColour, dxMultiplier))
    noteColour += 1
    transparentDot.append(TWICE.TransparentDot(xPos, yPos, dxMultiplier))

    xPos += 32
    yPos -= 50
    musicNote.append(TWICE.MusicNote(xPos, yPos, noteColour, dxMultiplier))
    noteColour += 1
    transparentDot.append(TWICE.TransparentDot(xPos, yPos, dxMultiplier))

    xPos += 64
    yPos += 50
    musicNote.append(TWICE.MusicNote(xPos, yPos, noteColour, dxMultiplier))
    noteColour += 1
    transparentDot.append(TWICE.TransparentDot(xPos, yPos, dxMultiplier))

    xPos += 64
    yPos -= 50
    musicNote.append(TWICE.MusicNote(xPos, yPos, noteColour, dxMultiplier))
    noteColour += 1
    transparentDot.append(TWICE.TransparentDot(xPos, yPos, dxMultiplier))

    xPos += 96
    yPos += 50
    musicNote.append(TWICE.MusicNote(xPos, yPos, noteColour, dxMultiplier))
    noteColour += 1
    transparentDot.append(TWICE.TransparentDot(xPos, yPos, dxMultiplier))

    xPos += 64
    yPos += 50
    musicNote.append(TWICE.MusicNote(xPos, yPos, noteColour, dxMultiplier))
    noteColour -= 1
    transparentDot.append(TWICE.TransparentDot(xPos, yPos, dxMultiplier))

    xPos += 64
    yPos += 0
    musicNote.append(TWICE.MusicNote(xPos, yPos, noteColour, dxMultiplier))
    noteColour -= 1
    transparentDot.append(TWICE.TransparentDot(xPos, yPos, dxMultiplier))

    xPos += 64
    yPos += 0
    musicNote.append(TWICE.MusicNote(xPos, yPos, noteColour, dxMultiplier))
    noteColour += 1
    transparentDot.append(TWICE.TransparentDot(xPos, yPos, dxMultiplier))

    xPos += 64
    yPos += 0
    musicNote.append(TWICE.MusicNote(xPos, yPos, noteColour, dxMultiplier))
    noteColour += 1
    transparentDot.append(TWICE.TransparentDot(xPos, yPos, dxMultiplier))

    xPos += 48
    yPos -= 50
    musicNote.append(TWICE.MusicNote(xPos, yPos, noteColour, dxMultiplier))
    noteColour += 1
    transparentDot.append(TWICE.TransparentDot(xPos, yPos, dxMultiplier))

    xPos += 96
    yPos -= 0
    musicNote.append(TWICE.MusicNote(xPos, yPos, noteColour, dxMultiplier))
    noteColour += 1
    transparentDot.append(TWICE.TransparentDot(xPos, yPos, dxMultiplier))

    xPos += 96
    yPos -= 0
    musicNote.append(TWICE.MusicNote(xPos, yPos, noteColour, dxMultiplier))
    noteColour += 1
    transparentDot.append(TWICE.TransparentDot(xPos, yPos, dxMultiplier))

    xPos += 80
    yPos += 50
    musicNote.append(TWICE.MusicNote(xPos, yPos, noteColour, dxMultiplier))
    noteColour += 1
    transparentDot.append(TWICE.TransparentDot(xPos, yPos, dxMultiplier))

    xPos += 64
    yPos += 50
    musicNote.append(TWICE.MusicNote(xPos, yPos, noteColour, dxMultiplier))
    noteColour += 1
    transparentDot.append(TWICE.TransparentDot(xPos, yPos, dxMultiplier))

    xPos += 86
    yPos -= 50
    musicNote.append(TWICE.MusicNote(xPos, yPos, noteColour, dxMultiplier))
    noteColour += 1
    transparentDot.append(TWICE.TransparentDot(xPos, yPos, dxMultiplier))

    xPos += 64
    yPos -= 0
    musicNote.append(TWICE.MusicNote(xPos, yPos, noteColour, dxMultiplier))
    noteColour += 1
    transparentDot.append(TWICE.TransparentDot(xPos, yPos, dxMultiplier))

    xPos += 64
    yPos -= 50
    musicNote.append(TWICE.MusicNote(xPos, yPos, noteColour, dxMultiplier))
    noteColour += 1
    transparentDot.append(TWICE.TransparentDot(xPos, yPos, dxMultiplier))

    xPos += 64
    yPos += 50
    musicNote.append(TWICE.MusicNote(xPos, yPos, noteColour, dxMultiplier))
    noteColour += 1
    transparentDot.append(TWICE.TransparentDot(xPos, yPos, dxMultiplier))

    xPos += 48
    yPos += 50
    musicNote.append(TWICE.MusicNote(xPos, yPos, noteColour, dxMultiplier))
    noteColour += 1
    transparentDot.append(TWICE.TransparentDot(xPos, yPos, dxMultiplier))

    xPos += 96
    yPos += 50
    musicNote.append(TWICE.MusicNote(xPos, yPos, noteColour, dxMultiplier))
    noteColour += 1
    transparentDot.append(TWICE.TransparentDot(xPos, yPos, dxMultiplier))

    xPos += 64
    yPos -= 50
    musicNote.append(TWICE.MusicNote(xPos, yPos, noteColour, dxMultiplier))
    noteColour += 1
    transparentDot.append(TWICE.TransparentDot(xPos, yPos, dxMultiplier))

    xPos += 64
    yPos -= 50
    musicNote.append(TWICE.MusicNote(xPos, yPos, noteColour, dxMultiplier))
    noteColour += 1
    transparentDot.append(TWICE.TransparentDot(xPos, yPos, dxMultiplier))

    xPos += 48
    yPos += 50
    musicNote.append(TWICE.MusicNote(xPos, yPos, noteColour, dxMultiplier))
    noteColour += 1
    transparentDot.append(TWICE.TransparentDot(xPos, yPos, dxMultiplier))

    xPos += 32
    yPos -= 50
    musicNote.append(TWICE.MusicNote(xPos, yPos, noteColour, dxMultiplier))
    noteColour += 1
    transparentDot.append(TWICE.TransparentDot(xPos, yPos, dxMultiplier))

    xPos += 64
    yPos -= 50
    musicNote.append(TWICE.MusicNote(xPos, yPos, noteColour, dxMultiplier))
    noteColour += 1
    transparentDot.append(TWICE.TransparentDot(xPos, yPos, dxMultiplier))

    xPos += 48
    yPos += 50
    musicNote.append(TWICE.MusicNote(xPos, yPos, noteColour, dxMultiplier))
    noteColour += 1
    transparentDot.append(TWICE.TransparentDot(xPos, yPos, dxMultiplier))

    xPos += 64
    yPos += 0
    musicNote.append(TWICE.MusicNote(xPos, yPos, noteColour, dxMultiplier))
    noteColour += 1
    transparentDot.append(TWICE.TransparentDot(xPos, yPos, dxMultiplier))

    xPos += 32
    yPos -= 50
    musicNote.append(TWICE.MusicNote(xPos, yPos, noteColour, dxMultiplier))
    noteColour += 1
    transparentDot.append(TWICE.TransparentDot(xPos, yPos, dxMultiplier))

    xPos += 256
    yPos -= 0
    musicNote.append(TWICE.MusicNote(xPos, yPos, noteColour, dxMultiplier))
    noteColour += 1
    transparentDot.append(TWICE.TransparentDot(xPos, yPos, dxMultiplier))

    xPos += 64
    yPos += 50
    musicNote.append(TWICE.MusicNote(xPos, yPos, noteColour, dxMultiplier))
    noteColour += 1
    transparentDot.append(TWICE.TransparentDot(xPos, yPos, dxMultiplier))

    xPos += 64
    yPos -= 50
    musicNote.append(TWICE.MusicNote(xPos, yPos, noteColour, dxMultiplier))
    noteColour += 1
    transparentDot.append(TWICE.TransparentDot(xPos, yPos, dxMultiplier))

    xPos += 32
    yPos -= 50
    musicNote.append(TWICE.MusicNote(xPos, yPos, noteColour, dxMultiplier))
    noteColour += 1
    transparentDot.append(TWICE.TransparentDot(xPos, yPos, dxMultiplier))

    xPos += 48
    yPos += 50
    musicNote.append(TWICE.MusicNote(xPos, yPos, noteColour, dxMultiplier))
    noteColour += 1
    transparentDot.append(TWICE.TransparentDot(xPos, yPos, dxMultiplier))

    xPos += 32
    yPos -= 50
    musicNote.append(TWICE.MusicNote(xPos, yPos, noteColour, dxMultiplier))
    noteColour += 1
    transparentDot.append(TWICE.TransparentDot(xPos, yPos, dxMultiplier))

    xPos += 608
    yPos += 50
    musicNote.append(TWICE.MusicNote(xPos, yPos, noteColour, dxMultiplier))
    noteColour += 1
    transparentDot.append(TWICE.TransparentDot(xPos, yPos, dxMultiplier))

    xPos += 48
    yPos -= 50
    musicNote.append(TWICE.MusicNote(xPos, yPos, noteColour, dxMultiplier))
    noteColour += 1
    transparentDot.append(TWICE.TransparentDot(xPos, yPos, dxMultiplier))

    xPos += 48
    yPos += 50
    musicNote.append(TWICE.MusicNote(xPos, yPos, noteColour, dxMultiplier))
    noteColour += 1
    transparentDot.append(TWICE.TransparentDot(xPos, yPos, dxMultiplier))

    xPos += 32
    yPos += 50
    musicNote.append(TWICE.MusicNote(xPos, yPos, noteColour, dxMultiplier))
    noteColour += 1
    transparentDot.append(TWICE.TransparentDot(xPos, yPos, dxMultiplier))

    xPos += 48
    yPos += 50
    musicNote.append(TWICE.MusicNote(xPos, yPos, noteColour, dxMultiplier))
    noteColour += 1
    transparentDot.append(TWICE.TransparentDot(xPos, yPos, dxMultiplier))

    xPos += 48
    yPos += 0
    musicNote.append(TWICE.MusicNote(xPos, yPos, noteColour, dxMultiplier))
    noteColour += 1
    transparentDot.append(TWICE.TransparentDot(xPos, yPos, dxMultiplier))

    xPos += 608
    yPos -= 50
    musicNote.append(TWICE.MusicNote(xPos, yPos, noteColour, dxMultiplier))
    noteColour += 1
    transparentDot.append(TWICE.TransparentDot(xPos, yPos, dxMultiplier))

    xPos += 64
    yPos += 50
    musicNote.append(TWICE.MusicNote(xPos, yPos, noteColour, dxMultiplier))
    noteColour += 1
    transparentDot.append(TWICE.TransparentDot(xPos, yPos, dxMultiplier))

    xPos += 128
    yPos += 50
    musicNote.append(TWICE.MusicNote(xPos, yPos, noteColour, dxMultiplier))
    noteColour += 1
    transparentDot.append(TWICE.TransparentDot(xPos, yPos, dxMultiplier))

    xPos += 64
    yPos -= 50
    musicNote.append(TWICE.MusicNote(xPos, yPos, noteColour, dxMultiplier))
    noteColour += 1
    transparentDot.append(TWICE.TransparentDot(xPos, yPos, dxMultiplier))

    xPos += 64
    yPos -= 0
    musicNote.append(TWICE.MusicNote(xPos, yPos, noteColour, dxMultiplier))
    noteColour += 1
    transparentDot.append(TWICE.TransparentDot(xPos, yPos, dxMultiplier))

    xPos += 64
    yPos -= 0
    musicNote.append(TWICE.MusicNote(xPos, yPos, noteColour, dxMultiplier))
    noteColour += 1
    transparentDot.append(TWICE.TransparentDot(xPos, yPos, dxMultiplier))

    xPos += 80
    yPos += 50
    musicNote.append(TWICE.MusicNote(xPos, yPos, noteColour, dxMultiplier))
    noteColour += 1
    transparentDot.append(TWICE.TransparentDot(xPos, yPos, dxMultiplier))

    xPos += 64
    yPos += 50
    musicNote.append(TWICE.MusicNote(xPos, yPos, noteColour, dxMultiplier))
    noteColour += 1
    transparentDot.append(TWICE.TransparentDot(xPos, yPos, dxMultiplier))

    xPos += 64
    yPos -= 50
    musicNote.append(TWICE.MusicNote(xPos, yPos, noteColour, dxMultiplier))
    noteColour += 1
    transparentDot.append(TWICE.TransparentDot(xPos, yPos, dxMultiplier))

    xPos += 64
    yPos -= 0
    musicNote.append(TWICE.MusicNote(xPos, yPos, noteColour, dxMultiplier))
    noteColour += 1
    transparentDot.append(TWICE.TransparentDot(xPos, yPos, dxMultiplier))

    xPos += 64
    yPos -= 50
    musicNote.append(TWICE.MusicNote(xPos, yPos, noteColour, dxMultiplier))
    noteColour += 1
    transparentDot.append(TWICE.TransparentDot(xPos, yPos, dxMultiplier))

    xPos += 96
    yPos += 50
    musicNote.append(TWICE.MusicNote(xPos, yPos, noteColour, dxMultiplier))
    noteColour += 1
    transparentDot.append(TWICE.TransparentDot(xPos, yPos, dxMultiplier))

    xPos += 64
    yPos += 50
    musicNote.append(TWICE.MusicNote(xPos, yPos, noteColour, dxMultiplier))
    noteColour += 1
    transparentDot.append(TWICE.TransparentDot(xPos, yPos, dxMultiplier))

    xPos += 128
    yPos += 50
    musicNote.append(TWICE.MusicNote(xPos, yPos, noteColour, dxMultiplier))
    noteColour += 1
    transparentDot.append(TWICE.TransparentDot(xPos, yPos, dxMultiplier))

    xPos += 64
    yPos -= 50
    musicNote.append(TWICE.MusicNote(xPos, yPos, noteColour, dxMultiplier))
    noteColour += 1
    transparentDot.append(TWICE.TransparentDot(xPos, yPos, dxMultiplier))

    xPos += 64
    yPos -= 50
    musicNote.append(TWICE.MusicNote(xPos, yPos, noteColour, dxMultiplier))
    noteColour += 1
    transparentDot.append(TWICE.TransparentDot(xPos, yPos, dxMultiplier))

    xPos += 48
    yPos += 50
    musicNote.append(TWICE.MusicNote(xPos, yPos, noteColour, dxMultiplier))
    noteColour += 1
    transparentDot.append(TWICE.TransparentDot(xPos, yPos, dxMultiplier))

    xPos += 48
    yPos -= 50
    musicNote.append(TWICE.MusicNote(xPos, yPos, noteColour, dxMultiplier))
    noteColour += 1
    transparentDot.append(TWICE.TransparentDot(xPos, yPos, dxMultiplier))

    xPos += 64
    yPos -= 50
    musicNote.append(TWICE.MusicNote(xPos, yPos, noteColour, dxMultiplier))
    noteColour += 1
    transparentDot.append(TWICE.TransparentDot(xPos, yPos, dxMultiplier))

    xPos += 64
    yPos -= 50
    musicNote.append(TWICE.MusicNote(xPos, yPos, noteColour, dxMultiplier))
    noteColour += 1
    transparentDot.append(TWICE.TransparentDot(xPos, yPos, dxMultiplier))

    xPos += 320
    yPos += 50
    musicNote.append(TWICE.MusicNote(xPos, yPos, noteColour, dxMultiplier))
    noteColour += 1
    transparentDot.append(TWICE.TransparentDot(xPos, yPos, dxMultiplier))

    xPos += 48
    yPos -= 50
    musicNote.append(TWICE.MusicNote(xPos, yPos, noteColour, dxMultiplier))
    noteColour += 1
    transparentDot.append(TWICE.TransparentDot(xPos, yPos, dxMultiplier))

    xPos += 48
    yPos += 50
    musicNote.append(TWICE.MusicNote(xPos, yPos, noteColour, dxMultiplier))
    noteColour += 1
    transparentDot.append(TWICE.TransparentDot(xPos, yPos, dxMultiplier))

    xPos += 32
    yPos += 50
    musicNote.append(TWICE.MusicNote(xPos, yPos, noteColour, dxMultiplier))
    noteColour += 1
    transparentDot.append(TWICE.TransparentDot(xPos, yPos, dxMultiplier))

    xPos += 48
    yPos += 50
    musicNote.append(TWICE.MusicNote(xPos, yPos, noteColour, dxMultiplier))
    noteColour += 1
    transparentDot.append(TWICE.TransparentDot(xPos, yPos, dxMultiplier))

    xPos += 32
    yPos += 0
    musicNote.append(TWICE.MusicNote(xPos, yPos, noteColour, dxMultiplier))
    noteColour += 1
    transparentDot.append(TWICE.TransparentDot(xPos, yPos, dxMultiplier))
    #NEW GREEN (PART 3)!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    xPos += 48
    yPos -= 50
    musicNote.append(TWICE.MusicNote(xPos, yPos, noteColour, dxMultiplier))
    noteColour += 1
    transparentDot.append(TWICE.TransparentDot(xPos, yPos, dxMultiplier))

    xPos += 48
    yPos += 50
    musicNote.append(TWICE.MusicNote(xPos, yPos, noteColour, dxMultiplier))
    noteColour += 1
    transparentDot.append(TWICE.TransparentDot(xPos, yPos, dxMultiplier))

    xPos += 64
    yPos += 50
    musicNote.append(TWICE.MusicNote(xPos, yPos, noteColour, dxMultiplier))
    noteColour += 1
    transparentDot.append(TWICE.TransparentDot(xPos, yPos, dxMultiplier))

    xPos += 64
    yPos -= 50
    musicNote.append(TWICE.MusicNote(xPos, yPos, noteColour, dxMultiplier))
    noteColour += 1
    transparentDot.append(TWICE.TransparentDot(xPos, yPos, dxMultiplier))

    xPos += 32
    yPos += 50
    musicNote.append(TWICE.MusicNote(xPos, yPos, noteColour, dxMultiplier))
    noteColour += 1
    transparentDot.append(TWICE.TransparentDot(xPos, yPos, dxMultiplier))

    xPos += 32
    yPos += 50
    musicNote.append(TWICE.MusicNote(xPos, yPos, noteColour, dxMultiplier))
    noteColour += 1
    transparentDot.append(TWICE.TransparentDot(xPos, yPos, dxMultiplier))

    xPos += 32
    yPos -= 50
    musicNote.append(TWICE.MusicNote(xPos, yPos, noteColour, dxMultiplier))
    noteColour += 1
    transparentDot.append(TWICE.TransparentDot(xPos, yPos, dxMultiplier))

    xPos += 32
    yPos += 50
    musicNote.append(TWICE.MusicNote(xPos, yPos, noteColour, dxMultiplier))
    noteColour += 1
    transparentDot.append(TWICE.TransparentDot(xPos, yPos, dxMultiplier))

    xPos += 64
    yPos -= 50
    musicNote.append(TWICE.MusicNote(xPos, yPos, noteColour, dxMultiplier))
    noteColour += 1
    transparentDot.append(TWICE.TransparentDot(xPos, yPos, dxMultiplier))

    xPos += 64
    yPos += 50
    musicNote.append(TWICE.MusicNote(xPos, yPos, noteColour, dxMultiplier))
    noteColour += 1
    transparentDot.append(TWICE.TransparentDot(xPos, yPos, dxMultiplier))

    xPos += 64
    yPos -= 50
    musicNote.append(TWICE.MusicNote(xPos, yPos, noteColour, dxMultiplier))
    noteColour += 1
    transparentDot.append(TWICE.TransparentDot(xPos, yPos, dxMultiplier))

    xPos += 64
    yPos -= 50
    musicNote.append(TWICE.MusicNote(xPos, yPos, noteColour, dxMultiplier))
    noteColour += 1
    transparentDot.append(TWICE.TransparentDot(xPos, yPos, dxMultiplier))

    xPos += 64
    yPos -= 50
    musicNote.append(TWICE.MusicNote(xPos, yPos, noteColour, dxMultiplier))
    noteColour += 1
    transparentDot.append(TWICE.TransparentDot(xPos, yPos, dxMultiplier))

    xPos += 64
    yPos -= 50
    musicNote.append(TWICE.MusicNote(xPos, yPos, noteColour, dxMultiplier))
    noteColour += 1
    transparentDot.append(TWICE.TransparentDot(xPos, yPos, dxMultiplier))

    xPos += 64
    yPos -= 50
    musicNote.append(TWICE.MusicNote(xPos, yPos, noteColour, dxMultiplier))
    noteColour += 1
    transparentDot.append(TWICE.TransparentDot(xPos, yPos, dxMultiplier))

    xPos += 96
    yPos -= 50
    musicNote.append(TWICE.MusicNote(xPos, yPos, noteColour, dxMultiplier))
    noteColour += 1
    transparentDot.append(TWICE.TransparentDot(xPos, yPos, dxMultiplier))

    xPos += 64
    yPos += 50
    musicNote.append(TWICE.MusicNote(xPos, yPos, noteColour, dxMultiplier))
    noteColour += 1
    transparentDot.append(TWICE.TransparentDot(xPos, yPos, dxMultiplier))

    xPos += 64
    yPos += 50
    musicNote.append(TWICE.MusicNote(xPos, yPos, noteColour, dxMultiplier))
    noteColour += 1
    transparentDot.append(TWICE.TransparentDot(xPos, yPos, dxMultiplier))

    xPos += 64
    yPos += 50
    musicNote.append(TWICE.MusicNote(xPos, yPos, noteColour, dxMultiplier))
    noteColour += 1
    transparentDot.append(TWICE.TransparentDot(xPos, yPos, dxMultiplier))

    xPos += 32
    yPos += 50
    musicNote.append(TWICE.MusicNote(xPos, yPos, noteColour, dxMultiplier))
    noteColour += 1
    transparentDot.append(TWICE.TransparentDot(xPos, yPos, dxMultiplier))

    xPos += 32
    yPos += 50
    musicNote.append(TWICE.MusicNote(xPos, yPos, noteColour, dxMultiplier))
    noteColour += 1
    transparentDot.append(TWICE.TransparentDot(xPos, yPos, dxMultiplier))

    xPos += 32
    yPos -= 50
    musicNote.append(TWICE.MusicNote(xPos, yPos, noteColour, dxMultiplier))
    noteColour += 1
    transparentDot.append(TWICE.TransparentDot(xPos, yPos, dxMultiplier))

    xPos += 32
    yPos += 50
    musicNote.append(TWICE.MusicNote(xPos, yPos, noteColour, dxMultiplier))
    noteColour += 1
    transparentDot.append(TWICE.TransparentDot(xPos, yPos, dxMultiplier))

    xPos += 64
    yPos -= 50
    musicNote.append(TWICE.MusicNote(xPos, yPos, noteColour, dxMultiplier))
    noteColour += 1
    transparentDot.append(TWICE.TransparentDot(xPos, yPos, dxMultiplier))

    xPos += 64
    yPos += 50
    musicNote.append(TWICE.MusicNote(xPos, yPos, noteColour, dxMultiplier))
    noteColour += 1
    transparentDot.append(TWICE.TransparentDot(xPos, yPos, dxMultiplier))

    xPos += 64
    yPos -= 50
    musicNote.append(TWICE.MusicNote(xPos, yPos, noteColour, dxMultiplier))
    noteColour += 1
    transparentDot.append(TWICE.TransparentDot(xPos, yPos, dxMultiplier))

    xPos += 64
    yPos -= 50
    musicNote.append(TWICE.MusicNote(xPos, yPos, noteColour, dxMultiplier))
    noteColour += 1
    transparentDot.append(TWICE.TransparentDot(xPos, yPos, dxMultiplier))

    xPos += 64
    yPos -= 50
    musicNote.append(TWICE.MusicNote(xPos, yPos, noteColour, dxMultiplier))
    noteColour += 1
    transparentDot.append(TWICE.TransparentDot(xPos, yPos, dxMultiplier))

    xPos += 64
    yPos += 50
    musicNote.append(TWICE.MusicNote(xPos, yPos, noteColour, dxMultiplier))
    noteColour += 1
    transparentDot.append(TWICE.TransparentDot(xPos, yPos, dxMultiplier))

    xPos += 64
    yPos += 50
    musicNote.append(TWICE.MusicNote(xPos, yPos, noteColour, dxMultiplier))
    noteColour += 1
    transparentDot.append(TWICE.TransparentDot(xPos, yPos, dxMultiplier))

    xPos += 64
    yPos += 50
    musicNote.append(TWICE.MusicNote(xPos, yPos, noteColour, dxMultiplier))
    noteColour += 1
    transparentDot.append(TWICE.TransparentDot(xPos, yPos, dxMultiplier))

    xPos += 64
    yPos += 0
    musicNote.append(TWICE.MusicNote(xPos, yPos, noteColour, dxMultiplier))
    noteColour += 1
    transparentDot.append(TWICE.TransparentDot(xPos, yPos, dxMultiplier))

    xPos += 64
    yPos += 50
    musicNote.append(TWICE.MusicNote(xPos, yPos, noteColour, dxMultiplier))
    noteColour += 1
    transparentDot.append(TWICE.TransparentDot(xPos, yPos, dxMultiplier))

    xPos += 64
    yPos -= 50
    musicNote.append(TWICE.MusicNote(xPos, yPos, noteColour, dxMultiplier))
    noteColour += 1
    transparentDot.append(TWICE.TransparentDot(xPos, yPos, dxMultiplier))

    xPos += 32
    yPos -= 0
    musicNote.append(TWICE.MusicNote(xPos, yPos, noteColour, dxMultiplier))
    noteColour += 1
    transparentDot.append(TWICE.TransparentDot(xPos, yPos, dxMultiplier))

    xPos += 32
    yPos -= 0
    musicNote.append(TWICE.MusicNote(xPos, yPos, noteColour, dxMultiplier))
    noteColour += 1
    transparentDot.append(TWICE.TransparentDot(xPos, yPos, dxMultiplier))

    xPos += 32
    yPos -= 0
    musicNote.append(TWICE.MusicNote(xPos, yPos, noteColour, dxMultiplier))
    noteColour += 1
    transparentDot.append(TWICE.TransparentDot(xPos, yPos, dxMultiplier))

    xPos += 32
    yPos += 50
    musicNote.append(TWICE.MusicNote(xPos, yPos, noteColour, dxMultiplier))
    noteColour += 1
    transparentDot.append(TWICE.TransparentDot(xPos, yPos, dxMultiplier))

    xPos += 64
    yPos -= 50
    musicNote.append(TWICE.MusicNote(xPos, yPos, noteColour, dxMultiplier))
    noteColour += 1
    transparentDot.append(TWICE.TransparentDot(xPos, yPos, dxMultiplier))

    xPos += 64
    yPos -= 0
    musicNote.append(TWICE.MusicNote(xPos, yPos, noteColour, dxMultiplier))
    noteColour += 1
    transparentDot.append(TWICE.TransparentDot(xPos, yPos, dxMultiplier))

    xPos += 64
    yPos += 50
    musicNote.append(TWICE.MusicNote(xPos, yPos, noteColour, dxMultiplier))
    noteColour += 1
    transparentDot.append(TWICE.TransparentDot(xPos, yPos, dxMultiplier))

    xPos += 64
    yPos -= 50
    musicNote.append(TWICE.MusicNote(xPos, yPos, noteColour, dxMultiplier))
    noteColour += 1
    transparentDot.append(TWICE.TransparentDot(xPos, yPos, dxMultiplier))

    xPos += 48
    yPos += 50
    musicNote.append(TWICE.MusicNote(xPos, yPos, noteColour, dxMultiplier))
    noteColour += 1
    transparentDot.append(TWICE.TransparentDot(xPos, yPos, dxMultiplier))

    xPos += 48
    yPos += 50
    musicNote.append(TWICE.MusicNote(xPos, yPos, noteColour, dxMultiplier))
    noteColour += 1
    transparentDot.append(TWICE.TransparentDot(xPos, yPos, dxMultiplier))

    xPos += 48
    yPos += 50
    musicNote.append(TWICE.MusicNote(xPos, yPos, noteColour, dxMultiplier))
    noteColour += 1
    transparentDot.append(TWICE.TransparentDot(xPos, yPos, dxMultiplier))

    xPos += 48
    yPos -= 50
    musicNote.append(TWICE.MusicNote(xPos, yPos, noteColour, dxMultiplier))
    noteColour += 1
    transparentDot.append(TWICE.TransparentDot(xPos, yPos, dxMultiplier))

    xPos += 48
    yPos += 0
    musicNote.append(TWICE.MusicNote(xPos, yPos, noteColour, dxMultiplier))
    noteColour += 1
    transparentDot.append(TWICE.TransparentDot(xPos, yPos, dxMultiplier))

    xPos += 48
    yPos -= 50
    musicNote.append(TWICE.MusicNote(xPos, yPos, noteColour, dxMultiplier))
    noteColour += 1
    transparentDot.append(TWICE.TransparentDot(xPos, yPos, dxMultiplier))

    xPos += 48
    yPos -= 50
    musicNote.append(TWICE.MusicNote(xPos, yPos, noteColour, dxMultiplier))
    noteColour += 1
    transparentDot.append(TWICE.TransparentDot(xPos, yPos, dxMultiplier))

    xPos += 48
    yPos += 50
    musicNote.append(TWICE.MusicNote(xPos, yPos, noteColour, dxMultiplier))
    noteColour += 1
    transparentDot.append(TWICE.TransparentDot(xPos, yPos, dxMultiplier))

    xPos += 48
    yPos -= 50
    musicNote.append(TWICE.MusicNote(xPos, yPos, noteColour, dxMultiplier))
    noteColour += 1
    transparentDot.append(TWICE.TransparentDot(xPos, yPos, dxMultiplier))

    xPos += 48
    yPos += 50
    musicNote.append(TWICE.MusicNote(xPos, yPos, noteColour, dxMultiplier))
    noteColour += 1
    transparentDot.append(TWICE.TransparentDot(xPos, yPos, dxMultiplier))

    xPos += 64
    yPos += 50
    musicNote.append(TWICE.MusicNote(xPos, yPos, noteColour, dxMultiplier))
    noteColour += 1
    transparentDot.append(TWICE.TransparentDot(xPos, yPos, dxMultiplier))

    xPos += 256
    yPos -= 50
    musicNote.append(TWICE.MusicNote(xPos, yPos, noteColour, dxMultiplier))
    noteColour += 1
    transparentDot.append(TWICE.TransparentDot(xPos, yPos, dxMultiplier))

    xPos += 64
    yPos -= 0
    musicNote.append(TWICE.MusicNote(xPos, yPos, noteColour, dxMultiplier))
    noteColour += 1
    transparentDot.append(TWICE.TransparentDot(xPos, yPos, dxMultiplier))

    xPos += 64
    yPos -= 0
    musicNote.append(TWICE.MusicNote(xPos, yPos, noteColour, dxMultiplier))
    noteColour += 1
    transparentDot.append(TWICE.TransparentDot(xPos, yPos, dxMultiplier))

    xPos += 32
    yPos -= 0
    musicNote.append(TWICE.MusicNote(xPos, yPos, noteColour, dxMultiplier))
    noteColour += 1
    transparentDot.append(TWICE.TransparentDot(xPos, yPos, dxMultiplier))

    xPos += 64
    yPos -= 0
    musicNote.append(TWICE.MusicNote(xPos, yPos, noteColour, dxMultiplier))
    noteColour += 1
    transparentDot.append(TWICE.TransparentDot(xPos, yPos, dxMultiplier))

    xPos += 32
    yPos -= 0
    musicNote.append(TWICE.MusicNote(xPos, yPos, noteColour, dxMultiplier))
    noteColour += 1
    transparentDot.append(TWICE.TransparentDot(xPos, yPos, dxMultiplier))

    xPos += 626
    yPos -= 350
    musicNote.append(TWICE.MusicNote(xPos, yPos, noteColour, dxMultiplier))
    noteColour += 1
    transparentDot.append(TWICE.TransparentDot(xPos, yPos, dxMultiplier))

    xPos += 48
    yPos -= 50
    musicNote.append(TWICE.MusicNote(xPos, yPos, noteColour, dxMultiplier))
    noteColour += 1
    transparentDot.append(TWICE.TransparentDot(xPos, yPos, dxMultiplier))

    xPos += 48
    yPos += 50
    musicNote.append(TWICE.MusicNote(xPos, yPos, noteColour, dxMultiplier))
    noteColour += 1
    transparentDot.append(TWICE.TransparentDot(xPos, yPos, dxMultiplier))

    xPos += 32
    yPos += 50
    musicNote.append(TWICE.MusicNote(xPos, yPos, noteColour, dxMultiplier))
    noteColour += 1
    transparentDot.append(TWICE.TransparentDot(xPos, yPos, dxMultiplier))

    xPos += 48
    yPos += 50
    musicNote.append(TWICE.MusicNote(xPos, yPos, noteColour, dxMultiplier))
    noteColour += 1
    transparentDot.append(TWICE.TransparentDot(xPos, yPos, dxMultiplier))

    xPos += 48
    yPos -= 50
    musicNote.append(TWICE.MusicNote(xPos, yPos, noteColour, dxMultiplier))
    noteColour += 1
    transparentDot.append(TWICE.TransparentDot(xPos, yPos, dxMultiplier))

    xPos += 608
    yPos -= 50
    musicNote.append(TWICE.MusicNote(xPos, yPos, noteColour, dxMultiplier))
    noteColour += 1
    transparentDot.append(TWICE.TransparentDot(xPos, yPos, dxMultiplier))

    xPos += 64
    yPos += 50
    musicNote.append(TWICE.MusicNote(xPos, yPos, noteColour, dxMultiplier))
    noteColour += 1
    transparentDot.append(TWICE.TransparentDot(xPos, yPos, dxMultiplier))

    xPos += 128
    yPos += 50
    musicNote.append(TWICE.MusicNote(xPos, yPos, noteColour, dxMultiplier))
    noteColour += 1
    transparentDot.append(TWICE.TransparentDot(xPos, yPos, dxMultiplier))

    xPos += 64
    yPos -= 50
    musicNote.append(TWICE.MusicNote(xPos, yPos, noteColour, dxMultiplier))
    noteColour += 1
    transparentDot.append(TWICE.TransparentDot(xPos, yPos, dxMultiplier))

    xPos += 64
    yPos -= 0
    musicNote.append(TWICE.MusicNote(xPos, yPos, noteColour, dxMultiplier))
    noteColour += 1
    transparentDot.append(TWICE.TransparentDot(xPos, yPos, dxMultiplier))

    xPos += 64
    yPos -= 0
    musicNote.append(TWICE.MusicNote(xPos, yPos, noteColour, dxMultiplier))
    noteColour += 1
    transparentDot.append(TWICE.TransparentDot(xPos, yPos, dxMultiplier))

    xPos += 80
    yPos += 50
    musicNote.append(TWICE.MusicNote(xPos, yPos, noteColour, dxMultiplier))
    noteColour += 1
    transparentDot.append(TWICE.TransparentDot(xPos, yPos, dxMultiplier))

    xPos += 64
    yPos += 50
    musicNote.append(TWICE.MusicNote(xPos, yPos, noteColour, dxMultiplier))
    noteColour += 1
    transparentDot.append(TWICE.TransparentDot(xPos, yPos, dxMultiplier))

    xPos += 64
    yPos -= 50
    musicNote.append(TWICE.MusicNote(xPos, yPos, noteColour, dxMultiplier))
    noteColour += 1
    transparentDot.append(TWICE.TransparentDot(xPos, yPos, dxMultiplier))

    xPos += 64
    yPos -= 0
    musicNote.append(TWICE.MusicNote(xPos, yPos, noteColour, dxMultiplier))
    noteColour += 1
    transparentDot.append(TWICE.TransparentDot(xPos, yPos, dxMultiplier))

    xPos += 64
    yPos -= 50
    musicNote.append(TWICE.MusicNote(xPos, yPos, noteColour, dxMultiplier))
    noteColour += 1
    transparentDot.append(TWICE.TransparentDot(xPos, yPos, dxMultiplier))

    xPos += 96
    yPos += 50
    musicNote.append(TWICE.MusicNote(xPos, yPos, noteColour, dxMultiplier))
    noteColour += 1
    transparentDot.append(TWICE.TransparentDot(xPos, yPos, dxMultiplier))

    xPos += 64
    yPos += 50
    musicNote.append(TWICE.MusicNote(xPos, yPos, noteColour, dxMultiplier))
    noteColour += 1
    transparentDot.append(TWICE.TransparentDot(xPos, yPos, dxMultiplier))

    xPos += 128
    yPos += 50
    musicNote.append(TWICE.MusicNote(xPos, yPos, noteColour, dxMultiplier))
    noteColour += 1
    transparentDot.append(TWICE.TransparentDot(xPos, yPos, dxMultiplier))

    xPos += 64
    yPos -= 50
    musicNote.append(TWICE.MusicNote(xPos, yPos, noteColour, dxMultiplier))
    noteColour += 1
    transparentDot.append(TWICE.TransparentDot(xPos, yPos, dxMultiplier))

    xPos += 64
    yPos -= 50
    musicNote.append(TWICE.MusicNote(xPos, yPos, noteColour, dxMultiplier))
    noteColour += 1
    transparentDot.append(TWICE.TransparentDot(xPos, yPos, dxMultiplier))

    xPos += 48
    yPos += 50
    musicNote.append(TWICE.MusicNote(xPos, yPos, noteColour, dxMultiplier))
    noteColour += 1
    transparentDot.append(TWICE.TransparentDot(xPos, yPos, dxMultiplier))

    xPos += 48
    yPos -= 50
    musicNote.append(TWICE.MusicNote(xPos, yPos, noteColour, dxMultiplier))
    noteColour += 1
    transparentDot.append(TWICE.TransparentDot(xPos, yPos, dxMultiplier))

    xPos += 64
    yPos -= 50
    musicNote.append(TWICE.MusicNote(xPos, yPos, noteColour, dxMultiplier))
    noteColour += 1
    transparentDot.append(TWICE.TransparentDot(xPos, yPos, dxMultiplier))

    xPos += 64
    yPos -= 50
    musicNote.append(TWICE.MusicNote(xPos, yPos, noteColour, dxMultiplier))
    noteColour += 1
    transparentDot.append(TWICE.TransparentDot(xPos, yPos, dxMultiplier))

    xPos += 320
    yPos += 50
    musicNote.append(TWICE.MusicNote(xPos, yPos, noteColour, dxMultiplier))
    noteColour += 1
    transparentDot.append(TWICE.TransparentDot(xPos, yPos, dxMultiplier))

    xPos += 48
    yPos -= 50
    musicNote.append(TWICE.MusicNote(xPos, yPos, noteColour, dxMultiplier))
    noteColour += 1
    transparentDot.append(TWICE.TransparentDot(xPos, yPos, dxMultiplier))

    xPos += 48
    yPos += 50
    musicNote.append(TWICE.MusicNote(xPos, yPos, noteColour, dxMultiplier))
    noteColour += 1
    transparentDot.append(TWICE.TransparentDot(xPos, yPos, dxMultiplier))

    xPos += 32
    yPos += 50
    musicNote.append(TWICE.MusicNote(xPos, yPos, noteColour, dxMultiplier))
    noteColour += 1
    transparentDot.append(TWICE.TransparentDot(xPos, yPos, dxMultiplier))

    xPos += 48
    yPos += 50
    musicNote.append(TWICE.MusicNote(xPos, yPos, noteColour, dxMultiplier))
    noteColour += 1
    transparentDot.append(TWICE.TransparentDot(xPos, yPos, dxMultiplier))

    xPos += 32
    yPos += 0
    musicNote.append(TWICE.MusicNote(xPos, yPos, noteColour, dxMultiplier))
    noteColour += 1
    transparentDot.append(TWICE.TransparentDot(xPos, yPos, dxMultiplier))

    xPos += 192
    yPos -= 50
    musicNote.append(TWICE.MusicNote(xPos, yPos, noteColour, dxMultiplier))
    noteColour += 1
    transparentDot.append(TWICE.TransparentDot(xPos, yPos, dxMultiplier))

    xPos += 96
    yPos -= 0
    musicNote.append(TWICE.MusicNote(xPos, yPos, noteColour, dxMultiplier))
    noteColour += 1
    transparentDot.append(TWICE.TransparentDot(xPos, yPos, dxMultiplier))

    xPos += 48
    yPos += 50
    musicNote.append(TWICE.MusicNote(xPos, yPos, noteColour, dxMultiplier))
    noteColour += 1
    transparentDot.append(TWICE.TransparentDot(xPos, yPos, dxMultiplier))

    xPos += 48
    yPos -= 50
    musicNote.append(TWICE.MusicNote(xPos, yPos, noteColour, dxMultiplier))
    noteColour += 1
    transparentDot.append(TWICE.TransparentDot(xPos, yPos, dxMultiplier))

    xPos += 48
    yPos += 50
    musicNote.append(TWICE.MusicNote(xPos, yPos, noteColour, dxMultiplier))
    noteColour += 1
    transparentDot.append(TWICE.TransparentDot(xPos, yPos, dxMultiplier))

    xPos += 160
    yPos += 50
    musicNote.append(TWICE.MusicNote(xPos, yPos, noteColour, dxMultiplier))
    noteColour += 1
    transparentDot.append(TWICE.TransparentDot(xPos, yPos, dxMultiplier))

    xPos += 96
    yPos -= 0
    musicNote.append(TWICE.MusicNote(xPos, yPos, noteColour, dxMultiplier))
    noteColour += 1
    transparentDot.append(TWICE.TransparentDot(xPos, yPos, dxMultiplier))

    xPos += 48
    yPos += 50
    musicNote.append(TWICE.MusicNote(xPos, yPos, noteColour, dxMultiplier))
    noteColour += 1
    transparentDot.append(TWICE.TransparentDot(xPos, yPos, dxMultiplier))

    xPos += 48
    yPos -= 50
    musicNote.append(TWICE.MusicNote(xPos, yPos, noteColour, dxMultiplier))
    noteColour += 1
    transparentDot.append(TWICE.TransparentDot(xPos, yPos, dxMultiplier))

    xPos += 48
    yPos += 50
    musicNote.append(TWICE.MusicNote(xPos, yPos, noteColour, dxMultiplier))
    noteColour += 1
    transparentDot.append(TWICE.TransparentDot(xPos, yPos, dxMultiplier))

    xPos += 160
    yPos += 50
    musicNote.append(TWICE.MusicNote(xPos, yPos, noteColour, dxMultiplier))
    noteColour += 1
    transparentDot.append(TWICE.TransparentDot(xPos, yPos, dxMultiplier))

    xPos += 96
    yPos -= 0
    musicNote.append(TWICE.MusicNote(xPos, yPos, noteColour, dxMultiplier))
    noteColour += 1
    transparentDot.append(TWICE.TransparentDot(xPos, yPos, dxMultiplier))

    xPos += 48
    yPos += 50
    musicNote.append(TWICE.MusicNote(xPos, yPos, noteColour, dxMultiplier))
    noteColour += 1
    transparentDot.append(TWICE.TransparentDot(xPos, yPos, dxMultiplier))

    xPos += 48
    yPos -= 50
    musicNote.append(TWICE.MusicNote(xPos, yPos, noteColour, dxMultiplier))
    noteColour += 1
    transparentDot.append(TWICE.TransparentDot(xPos, yPos, dxMultiplier))

    xPos += 48
    yPos += 50
    musicNote.append(TWICE.MusicNote(xPos, yPos, noteColour, dxMultiplier))
    noteColour += 1
    transparentDot.append(TWICE.TransparentDot(xPos, yPos, dxMultiplier))

    xPos += 192
    yPos += 0
    musicNote.append(TWICE.MusicNote(xPos, yPos, noteColour, dxMultiplier))
    noteColour += 1
    transparentDot.append(TWICE.TransparentDot(xPos, yPos, dxMultiplier))

    xPos += 64
    yPos += 0
    musicNote.append(TWICE.MusicNote(xPos, yPos, noteColour, dxMultiplier))
    noteColour += 1
    transparentDot.append(TWICE.TransparentDot(xPos, yPos, dxMultiplier))

    xPos += 48
    yPos += 50
    musicNote.append(TWICE.MusicNote(xPos, yPos, noteColour, dxMultiplier))
    noteColour += 1
    transparentDot.append(TWICE.TransparentDot(xPos, yPos, dxMultiplier))

    xPos += 32
    yPos += 50
    musicNote.append(TWICE.MusicNote(xPos, yPos, noteColour, dxMultiplier))
    noteColour += 1
    transparentDot.append(TWICE.TransparentDot(xPos, yPos, dxMultiplier))

    xPos += 64
    yPos -= 50
    musicNote.append(TWICE.MusicNote(xPos, yPos, noteColour, dxMultiplier))
    noteColour += 1
    transparentDot.append(TWICE.TransparentDot(xPos, yPos, dxMultiplier))

    xPos += 32
    yPos -= 50
    musicNote.append(TWICE.MusicNote(xPos, yPos, noteColour, dxMultiplier))
    noteColour += 1
    transparentDot.append(TWICE.TransparentDot(xPos, yPos, dxMultiplier))

    xPos += 192
    yPos += 0
    musicNote.append(TWICE.MusicNote(xPos, yPos, noteColour, dxMultiplier))
    noteColour += 1
    transparentDot.append(TWICE.TransparentDot(xPos, yPos, dxMultiplier))

    xPos += 64
    yPos += 0
    musicNote.append(TWICE.MusicNote(xPos, yPos, noteColour, dxMultiplier))
    noteColour += 1
    transparentDot.append(TWICE.TransparentDot(xPos, yPos, dxMultiplier))

    xPos += 48
    yPos += 50
    musicNote.append(TWICE.MusicNote(xPos, yPos, noteColour, dxMultiplier))
    noteColour += 1
    transparentDot.append(TWICE.TransparentDot(xPos, yPos, dxMultiplier))

    xPos += 32
    yPos += 50
    musicNote.append(TWICE.MusicNote(xPos, yPos, noteColour, dxMultiplier))
    noteColour += 1
    transparentDot.append(TWICE.TransparentDot(xPos, yPos, dxMultiplier))

    xPos += 64
    yPos -= 50
    musicNote.append(TWICE.MusicNote(xPos, yPos, noteColour, dxMultiplier))
    noteColour += 1
    transparentDot.append(TWICE.TransparentDot(xPos, yPos, dxMultiplier))

    xPos += 32
    yPos -= 50
    musicNote.append(TWICE.MusicNote(xPos, yPos, noteColour, dxMultiplier))
    noteColour += 1
    transparentDot.append(TWICE.TransparentDot(xPos, yPos, dxMultiplier))

    xPos += 192
    yPos += 0
    musicNote.append(TWICE.MusicNote(xPos, yPos, noteColour, dxMultiplier))
    noteColour += 1
    transparentDot.append(TWICE.TransparentDot(xPos, yPos, dxMultiplier))

    xPos += 48
    yPos += 0
    musicNote.append(TWICE.MusicNote(xPos, yPos, noteColour, dxMultiplier))
    noteColour += 1
    transparentDot.append(TWICE.TransparentDot(xPos, yPos, dxMultiplier))

    xPos += 48
    yPos += 50
    musicNote.append(TWICE.MusicNote(xPos, yPos, noteColour, dxMultiplier))
    noteColour += 1
    transparentDot.append(TWICE.TransparentDot(xPos, yPos, dxMultiplier))

    xPos += 32
    yPos += 50
    musicNote.append(TWICE.MusicNote(xPos, yPos, noteColour, dxMultiplier))
    noteColour += 1
    transparentDot.append(TWICE.TransparentDot(xPos, yPos, dxMultiplier))

    xPos += 64
    yPos -= 50
    musicNote.append(TWICE.MusicNote(xPos, yPos, noteColour, dxMultiplier))
    noteColour += 1
    transparentDot.append(TWICE.TransparentDot(xPos, yPos, dxMultiplier))

    xPos += 32
    yPos -= 50
    musicNote.append(TWICE.MusicNote(xPos, yPos, noteColour, dxMultiplier))
    noteColour += 1
    transparentDot.append(TWICE.TransparentDot(xPos, yPos, dxMultiplier))

    xPos += 192
    yPos += 0
    musicNote.append(TWICE.MusicNote(xPos, yPos, noteColour, dxMultiplier))
    noteColour += 1
    transparentDot.append(TWICE.TransparentDot(xPos, yPos, dxMultiplier))

    xPos += 48
    yPos += 0
    musicNote.append(TWICE.MusicNote(xPos, yPos, noteColour, dxMultiplier))
    noteColour += 1
    transparentDot.append(TWICE.TransparentDot(xPos, yPos, dxMultiplier))

    xPos += 48
    yPos += 50
    musicNote.append(TWICE.MusicNote(xPos, yPos, noteColour, dxMultiplier))
    noteColour += 1
    transparentDot.append(TWICE.TransparentDot(xPos, yPos, dxMultiplier))

    xPos += 32
    yPos += 50
    musicNote.append(TWICE.MusicNote(xPos, yPos, noteColour, dxMultiplier))
    noteColour += 1
    transparentDot.append(TWICE.TransparentDot(xPos, yPos, dxMultiplier))

    xPos += 48
    yPos -= 50
    musicNote.append(TWICE.MusicNote(xPos, yPos, noteColour, dxMultiplier))
    noteColour += 1
    transparentDot.append(TWICE.TransparentDot(xPos, yPos, dxMultiplier))

    xPos += 32
    yPos -= 50
    musicNote.append(TWICE.MusicNote(xPos, yPos, noteColour, dxMultiplier))
    noteColour += 1
    transparentDot.append(TWICE.TransparentDot(xPos, yPos, dxMultiplier))

    xPos += 192
    yPos += 0
    musicNote.append(TWICE.MusicNote(xPos, yPos, noteColour, dxMultiplier))
    noteColour += 1
    transparentDot.append(TWICE.TransparentDot(xPos, yPos, dxMultiplier))

    xPos += 48
    yPos -= 50
    musicNote.append(TWICE.MusicNote(xPos, yPos, noteColour, dxMultiplier))
    noteColour += 1
    transparentDot.append(TWICE.TransparentDot(xPos, yPos, dxMultiplier))

    xPos += 48
    yPos += 50
    musicNote.append(TWICE.MusicNote(xPos, yPos, noteColour, dxMultiplier))
    noteColour += 1
    transparentDot.append(TWICE.TransparentDot(xPos, yPos, dxMultiplier))

    xPos += 32
    yPos += 50
    musicNote.append(TWICE.MusicNote(xPos, yPos, noteColour, dxMultiplier))
    noteColour += 1
    transparentDot.append(TWICE.TransparentDot(xPos, yPos, dxMultiplier))

    xPos += 48
    yPos += 50
    musicNote.append(TWICE.MusicNote(xPos, yPos, noteColour, dxMultiplier))
    noteColour += 1
    transparentDot.append(TWICE.TransparentDot(xPos, yPos, dxMultiplier))

    xPos += 48
    yPos += 0
    musicNote.append(TWICE.MusicNote(xPos, yPos, noteColour, dxMultiplier))
    noteColour += 1
    transparentDot.append(TWICE.TransparentDot(xPos, yPos, dxMultiplier))

    # End of Hard Code For The Music Notes

    # Sprite Group Used To Detect Collision For Music Notes Later On
    musicNoteGroup = pygame.sprite.OrderedUpdates(musicNote)
    transparentDotGroup = pygame.sprite.OrderedUpdates(transparentDot)

    allSprites = pygame.sprite.OrderedUpdates(beach, blackBackgroundTop, \
                 scoreNames, scoreImages, playerMessage, livesMessage, \
                 musicNoteMessage, scoreMessage, timeMessage, footPrint, \
                 transparentRectangle, musicNote, musicNoteGroup, transparentDot, \
                 transparentDotGroup, player)

    # ACTION

        # Assign
    clock = pygame.time.Clock()
    keepGoing = True

        # Variables Used To Help With The Main Game Loop
    countImage = 0
    footPrintCountTime = 0
    countTime = 0
    footPrintAmount = 2
    lives = 9
    killedNote = False
    moreFootPrint = True

        # Loop
    while keepGoing:

        # Time
        clock.tick(30)

        # Events, Player Uses Arrow Keys (Up or Down) To Move Their Character
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                keepGoing = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    player.goUp(player.rect.centery)
                if event.key == pygame.K_DOWN:
                    player.goDown(player.rect.centery)

        # If Statement Used To Keep Track Of How Much Footprints To Append To The List
        if footPrintCountTime == footPrintAmount:
            footPrint.append(TWICE.FootPrint(player.rect.centerx, player.rect.centery + 30, countImage, dxMultiplier))
            allSprites = pygame.sprite.OrderedUpdates(beach, blackBackgroundTop, \
                         scoreNames, scoreImages, playerMessage, livesMessage, \
                         musicNoteMessage, scoreMessage, timeMessage, footPrint, \
                         transparentRectangle, transparentDot, transparentDotGroup, \
                         musicNote, musicNoteGroup, player)
            countImage += 1

        # If Statement To Check If The Player Has Reached The Middle Of The Screen, If Yes, Double The Amount Of Footprints Added
        if moreFootPrint:
            if player.rect.centerx == screen.get_width() / 2:
                footPrintAmount = 4
            countTime += 1
            footPrintCountTime = countTime % (footPrintAmount * 2)

        # Sprite Collision Detection Between Player Sprite And Music Sprite Along With Transparent Dot/Rectangle
        rectangleCollision = pygame.sprite.spritecollide(transparentRectangle, transparentDotGroup, True)
        noteCollision = pygame.sprite.spritecollide(player, musicNoteGroup, True)
        dotCollision = pygame.sprite.spritecollide(player, transparentDotGroup, True)
        if noteCollision:
            for musicNote in noteCollision:
                musicNoteMessage.gainNotePoints()
                scoreMessage.gainScorePoints()
                musicNote.killItSelf()
        if dotCollision:
            for transparentDot in rectangleCollision:
                transparentDot.killItSelf()
        if rectangleCollision:
            for transparentDot in rectangleCollision:
                transparentDot.killItSelf()
                lives -= 1
                livesMessage.loseLife()

        # Check To See If The Player Has Lost All Their Lives, If Yes, End The Gaming Loop
        if lives == 0:
            keepGoing = False

        if hidden:
            for note in musicNote:
                if (note.rect.centerx - player.rect.centerx) <= 300:
                    note.killItSelf()

        # Doing Certain Condtions For The Game Using A Timer
        if timeMessage.getTime() == 15.9:
            player.setImageList("SanaFlash")
            playerMessage.setPlayer("Sana")
        if timeMessage.getTime() == 16.4:
            player.setImageList("Sana")
        if timeMessage.getTime() == 23.7:
            player.setImageList("MomoFlash")
            playerMessage.setPlayer("Momo")
        if timeMessage.getTime() == 24.2:
            player.setImageList("Momo")
        if timeMessage.getTime() == 31.7:
            player.setImageList("JeongyeonFlash")
            playerMessage.setPlayer("Jeongyeon")
        if timeMessage.getTime() == 32.2:
            player.setImageList("Jeongyeon")
        if timeMessage.getTime() == 39.8:
            player.setImageList("TzuyuFlash")
            playerMessage.setPlayer("Tzuyu")
        if timeMessage.getTime() == 40.3:
            player.setImageList("Tzuyu")
        if timeMessage.getTime() == 47.7:
            player.setImageList("MinaFlash")
            playerMessage.setPlayer("Mina")
        if timeMessage.getTime() == 48.2:
            player.setImageList("Mina")
        if timeMessage.getTime() == 55.8:
            player.setImageList("JihyoFlash")
            playerMessage.setPlayer("Jihyo")
        if timeMessage.getTime() == 56.3:
            player.setImageList("Jihyo")
        if timeMessage.getTime() == 79.7:
            player.setImageList("SanaFlash")
            playerMessage.setPlayer("Sana")
        if timeMessage.getTime() == 80.2:
            player.setImageList("Sana")
        if timeMessage.getTime() == 87.7:
            player.setImageList("TzuyuFlash")
            playerMessage.setPlayer("Tzuyu")
        if timeMessage.getTime() == 88.2:
            player.setImageList("Tzuyu")
        if timeMessage.getTime() == 95.7:
            player.setImageList("MinaFlash")
            playerMessage.setPlayer("Mina")
        if timeMessage.getTime() == 96.2:
            player.setImageList("Mina")
        if timeMessage.getTime() == 103.5:
            player.setImageList("NayeonFlash")
            playerMessage.setPlayer("Nayeon")
        if timeMessage.getTime() == 104.0:
            player.setImageList("Nayeon")
        if timeMessage.getTime() == 111.5:
            player.setImageList("JeongyeonFlash")
            playerMessage.setPlayer("Jeongyeon")
        if timeMessage.getTime() == 112.0:
            player.setImageList("Jeongyeon")
        if timeMessage.getTime() == 127.6:
            player.setImageList("DahyunFlash")
            playerMessage.setPlayer("Dahyun")
        if timeMessage.getTime() == 128.1:
            player.setImageList("Dahyun")
        if timeMessage.getTime() == 135.5:
            player.setImageList("MinaFlash")
            playerMessage.setPlayer("Mina")
        if timeMessage.getTime() == 136.0:
            player.setImageList("Mina")
        if timeMessage.getTime() == 139.3:
            player.setImageList("MomoFlash")
            playerMessage.setPlayer("Momo")
        if timeMessage.getTime() == 139.8:
            player.setImageList("Momo")
        if timeMessage.getTime() == 143.5:
            player.setImageList("JihyoFlash")
            playerMessage.setPlayer("Jihyo")
        if timeMessage.getTime() == 144.0:
            player.setImageList("Jihyo")
        if timeMessage.getTime() == 166.1:
            player.setImageList("NayeonFlash")
            playerMessage.setPlayer("Nayeon")
        if timeMessage.getTime() == 166.6:
            player.setImageList("Nayeon")
        if timeMessage.getTime() == 174:
            player.setImageList("ChaeyoungFlash")
            playerMessage.setPlayer("Chaeyoung")
        if timeMessage.getTime() == 174.5:
            player.setImageList("Chaeyoung")
            player.letKeepMoving()
            beach.stopKeepMoving()
            for i in footPrint:
                i.stopKeepMoving()
                footPrintCountTime = 0
                moreFootPrint = False
        if timeMessage.getTime() == 182:
            keepGoing = False

        # Refresh screen
        allSprites.clear(screen, background)
        allSprites.update()
        allSprites.draw(screen)

        pygame.display.flip()

def showIntro():
    """This function shows the intro screen of the game"""

    # Display
    screen = pygame.display.set_mode((1280, 720))
    pygame.display.set_caption("TWICE - Dance The Night Away (8 Bit)")

    # Entities
    background = pygame.Surface(screen.get_size())
    background = background.convert()
    background.fill((255, 255, 255))
    screen.blit(background, (0, 0))

    # Background Music and Sound Effects
    pygame.mixer.music.load("Music/TWICE - Dance The Night Away (8 Bit).mp3")
    pygame.mixer.music.set_volume(0.3)
    pygame.mixer.music.play(1)

    # Sprites for: Player, MusicNote, Beach, ScoreNames, ScoreImages, ScoreKeeper, BlackTop, FootPrint
    player = TWICE.Player(screen, 0, 1.0)
    beach = TWICE.Beach(screen, 1.0)
    introMessage = TWICE.ScoreKeeper("none", 0, "intro", 1.0)
    titleMessage = TWICE.ScoreKeeper("none", 0, "title", 1.0)
    footPrint = []
    blackBackgroundTop = TWICE.BlackTop()
    controlMessage = TWICE.ScoreKeeper("none", 0, "controls", 1.0)
    upMessage = TWICE.ScoreKeeper("none", 0, "up", 1.0)
    downMessage = TWICE.ScoreKeeper("none", 0, "down", 1.0)
    modsMessage = TWICE.ScoreKeeper("none", 0, "mods", 1.0)
    hiddenInstructionMessage = TWICE.ScoreKeeper("none", 0, "hiddenInstruction", 1.0)
    doubleTimeInstructionMessage = TWICE.ScoreKeeper("none", 0, "doubleTimeInstruction", 1.0)
    hiddenMessage = TWICE.ScoreKeeper("none", 0, "hidden", 1.0)
    doubleTimeMessage = TWICE.ScoreKeeper("none", 0, "doubleTime", 1.0)

    allSprites = pygame.sprite.OrderedUpdates(beach, blackBackgroundTop, \
                                              footPrint, player, introMessage,\
                                              titleMessage, controlMessage, \
                                              upMessage, downMessage, \
                                              modsMessage, hiddenInstructionMessage, \
                                              doubleTimeInstructionMessage, \
                                              hiddenMessage, doubleTimeMessage)

    # ACTION

        # Assign
    clock = pygame.time.Clock()
    keepGoing = True
    quitGame = False
    hidden = False
    doubleTime = False

        # Variables Used To Help With The Main Game Loop
    countImage = 0
    footPrintCountTime = 0
    countTime = 0
    footPrintAmount = 2

        # Loop
    while keepGoing:

        # Time
        clock.tick(30)

        # Events, Player Uses Arrow Keys (Up or Down) To Move Their Character, Also To Turn Mods On/Off
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                keepGoing = False
                quitGame = True
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    keepGoing = False
                    quitGame = False
                if event.key == pygame.K_h:
                    if hidden:
                        hidden = False
                        hiddenMessage.isHidden = "Off"
                    else:
                        hidden = True
                        hiddenMessage.isHidden = "On"
                if event.key == pygame.K_d:
                    if doubleTime:
                        doubleTime = False
                        doubleTimeMessage.isDoubleTime = "Off"
                    else:
                        doubleTime = True
                        doubleTimeMessage.isDoubleTime = "On"
                if event.key == pygame.K_UP:
                    player.goUp(player.rect.centery)
                if event.key == pygame.K_DOWN:
                    player.goDown(player.rect.centery)

        # If Statement Used To Keep Track Of How Much Footprints To Append To The List
        if footPrintCountTime == footPrintAmount:
            footPrint.append(TWICE.FootPrint(player.rect.centerx, player.rect.centery + 30, countImage, 1.0))
            allSprites = pygame.sprite.OrderedUpdates(beach, blackBackgroundTop, \
                                                      footPrint, player, introMessage, \
                                                      titleMessage, controlMessage, \
                                                      upMessage, downMessage, modsMessage, \
                                                      hiddenInstructionMessage, doubleTimeInstructionMessage, \
                                                      hiddenMessage, doubleTimeMessage)
            countImage += 1

        # If Statement To Check If The Player Has Reached The Middle Of The Screen, If Yes, Double The Amount Of Footprints Added
        if player.rect.centerx == screen.get_width() / 2:
            footPrintAmount = 4
        countTime += 1
        footPrintCountTime = countTime % (footPrintAmount * 2)

        # Refresh screen
        allSprites.clear(screen, background)
        allSprites.update()
        allSprites.draw(screen)

        pygame.display.flip()

    # Create An Array To Hold All Return Variables
    gameData = [quitGame, hidden, doubleTime]

    # Return a True or False Value Depending On What The User Entered
    return gameData

def main():
    """The mainline logic of our program"""
    quitGame = False
    hidden = False
    doubleTime = False
    while not quitGame:
        gameData = showIntro()
        quitGame = gameData[0]
        hidden = gameData[1]
        doubleTime = gameData[2]
        if not quitGame:
            playGame(hidden, doubleTime)

    # Exit The Gaming Window
    pygame.quit()

#Call the main function
main()