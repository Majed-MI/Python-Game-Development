# Flappy Bird Game
# importing modules
import random   #For generating random
import pygame   #For game developing
import sys       #For system module to exit when cross
from pygame.locals import *    #Basic pygame import

#Global variables for the game
FPS = 32  #framepersecond = 32
SCREENWIDTH = 320  #screenwidth = 289
SCREENHEIGHT = 511  #screenheight = 511
SCREEN = pygame.display.set_mode((SCREENWIDTH,SCREENHEIGHT))   #screen displaying through pygame module
GROUNDY = SCREENHEIGHT * 0.8   #base height declaration
GAME_SPRITES = {}       #declaring the list of the png pics
GAME_SOUNDS = {}        #declaring the list of music files
PLAYER = 'Gallery/bird2.png'  #bird pic
BACKGROUND = 'Gallery/background.png'   #bg pic
PIPE = 'Gallery/pipe.png'  #pipe pic

def welcomeScreen():
        # starting the music when welcome screen is ok
        GAME_SOUNDS['lobby'].play()
        # birds position declaring for the welcomeScreen()
        playerx = int(SCREENWIDTH / 5)
        playery = int((SCREENHEIGHT - GAME_SPRITES['player'].get_height())/2)
        # foreground pics position declaring for the welcomeScreen()
        messagex = int((SCREENWIDTH - GAME_SPRITES['message'].get_width())/2)
        messagey = int(SCREENHEIGHT * 0.13)
        # base pic position declaring for the welcomeScreen()
        basex = 0
        # while loop to continue
        while True:
            # pygame.event is a function when key is press it is working
            for event in pygame.event.get():
                #If user clicks on X button or escape then close the game
                if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                    pygame.quit()
                    sys.exit()

                # if the user press the space or up key then start the game
                elif event.type == KEYDOWN and (event.key == K_SPACE or event.key == K_UP):
                    return
                # otherwise show the screen
                else :
                    # show the screen through positioning of background, base, foreground, bird image
                    SCREEN.blit(GAME_SPRITES['background'],(0,0))
                    SCREEN.blit(GAME_SPRITES['player'],(playerx,playery))
                    SCREEN.blit(GAME_SPRITES['message'],(messagex,messagey))
                    SCREEN.blit(GAME_SPRITES['base'],(basex,GROUNDY))
                    # pygame display update function
                    pygame.display.update()
                    # frameperssecond starting and generating
                    FPSCLOCK.tick(FPS)

# maingame function declaration
def mainGame():
        # initializing score as 0
        score = 0
        # positioning bird and base
        playerx = int(SCREENWIDTH / 5)
        playery = int(SCREENWIDTH / 2)
        basex = 0

        #Create 2 pipes for blitting in the screen
        newPipe1 = getRandomPipe()
        newPipe2 = getRandomPipe()

        # Mylist for upperpipes
        upperPipes = [
            {'x': SCREENWIDTH + 200, 'y':newPipe1[0]['y']},
            {'x': SCREENWIDTH + 200 +(SCREENWIDTH / 2), 'y':newPipe2[0]['y']}
        ]

        # Mylist for lowerpipes
        lowerPipes = [
            {'x': SCREENWIDTH + 200, 'y':newPipe1[1]['y']},
            {'x': SCREENWIDTH + 200 +(SCREENWIDTH / 2), 'y':newPipe2[1]['y']}
        ]

        # positioning pipe in the screen
        pipeVelX = -4

        # player positioning is declared through the values
        playerVelY = -9
        playerMaxVelY = 10
        playerMinVelY = -8
        playerAccY = 1

        playerFlapAccv = -8   #Velocity while flapping
        playerFlapped = False  #It is true only when the bird flaps

        # while loop to continue
        while True:
            # pygame event works when key is pressed
            for event in pygame.event.get():
                # if user want to quit while playing game then X button or escape
                if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                    pygame.quit()
                    sys.exit()
                # user playing the game through space button and up button
                if event.type == KEYDOWN and (event.key == K_SPACE or event.key == K_UP):
                    # if bird is up from the actual position that means game starts
                    if playery > 0:
                        # bird will flap according to its velocity
                        playerVelY = playerFlapAccv
                        # bird flapping will be true when its up from its actual position
                        playerFlapped = True
                        # sound of wing plays
                        GAME_SOUNDS['wing'].play()
                if event.type == KEYDOWN and event.key==K_v:
                    score+=10

            # Function which will return true if it crashes
            crashTest = isCollide(playerx, playery, upperPipes, lowerPipes)  #isCollide function
            if crashTest:
                return

            # Check score
            #bird positioning is declared
            playerMidPos = playerx + GAME_SPRITES['player'].get_width()/2
            #when bird crosses each and every upperpipes
            for pipe in upperPipes:
                # when bird is between the upperpipe and lowerpipe which means crossing the pipe
                pipeMidPos = pipe['x'] + GAME_SPRITES['pipe'][0].get_width()/2
                # when bird position is less than pipe position then score increases
                if pipeMidPos <= playerMidPos < pipeMidPos + 4:
                    score += 1
                    print(f"Your score is {score}")
                    # point music plays when each score is gained
                    GAME_SOUNDS['point'].play()

            # if the bird velocity is less than its max and also it is not flapped then increment the
            # bird acceleration which means the bird will fallmore quickly due to gravity
            if playerVelY < playerMaxVelY and not playerFlapped:
                playerVelY += playerAccY

            # when bird flaps one time and untill it flaps the playerFlapped is false
            if playerFlapped:
                playerFlapped = False

            # playerHeight is the value which determine the bird position exactly at that moment
            playerHeight = GAME_SPRITES['player'].get_height()
            # declaring the playery value again newly to get the actual playerheight which does not
            # collide with the base too
            playery = playery + min(playerVelY,GROUNDY - playery - playerHeight)

            # move pipes to the left
            for upperPipe,lowerPipe in zip(upperPipes,lowerPipes):
                upperPipe['x'] += pipeVelX
                lowerPipe['x'] += pipeVelX

            # Adding a new pipe when the first pipe is about to left the screen
            if 0 < upperPipes[0]['x'] < 5:
                # again getting new pipe when the old one is about to left
                newPipe = getRandomPipe()
                # upperpipe and lowerpipe appending newpipe
                upperPipes.append(newPipe[0])
                lowerPipes.append(newPipe[1])

            # if the pipe is out of the screen remove it
            if upperPipes[0]['x'] < -GAME_SPRITES['pipe'][0].get_width():
                upperPipes.pop(0)
                lowerPipes.pop(0)

            # lets blit our sprites now which means show the pics in the screen
            SCREEN.blit(GAME_SPRITES['background'],(0,0))
            for upperPipe,lowerPipe in zip(upperPipes,lowerPipes):
                SCREEN.blit(GAME_SPRITES['pipe'][0],(upperPipe['x'],upperPipe['y']))
                SCREEN.blit(GAME_SPRITES['pipe'][1],(lowerPipe['x'],lowerPipe['y']))

            SCREEN.blit(GAME_SPRITES['base'],(basex,GROUNDY))
            SCREEN.blit(GAME_SPRITES['player'],(playerx,playery))


            # declaring digit for the screen
            myDigits = [int(x) for x in list(str(score))]
            width = 0
            # showing digit one by one in the screen
            for digit in myDigits:
                width += GAME_SPRITES['numbers'][digit].get_width()
            xOffset = (SCREENWIDTH - width) / 2

            # showing the number png pics one by one which shows the score
            for digit in myDigits:
                SCREEN.blit(GAME_SPRITES['numbers'][digit],(xOffset,SCREENHEIGHT * 0.12))
                xOffset += GAME_SPRITES['numbers'][digit].get_width()

            # pygame display update and framepersecond clock is also updated
            pygame.display.update()
            FPSCLOCK.tick(FPS)

# function to determine if the bird collides or not
def isCollide (playerx, playery, upperPipes, lowerPipes):
    # if the bird is down from the actual position from the welcome screen or from the base then it crashed
    if playery > GROUNDY-25 or playery<0:
        # hit music plays
        GAME_SOUNDS['hit'].play()
        # return true which means it crashes
        return True
    # if the bird hits upperpipe then return true
    for pipe in upperPipes:
        # declaring pipeHeight
        pipeHeight = GAME_SPRITES ['pipe'][0].get_height()
        # if bird is less than the pipeheight  than it hits and hit music plays
        if(playery < pipeHeight + pipe['y'] and
           abs(playerx - pipe['x']) < GAME_SPRITES['pipe'][0].get_width()):
            GAME_SOUNDS['hit'].play()
            return True
    # if the bird hits lowerpipe then return true
    for pipe in lowerPipes:
        if (playery + GAME_SPRITES['player'].get_height() > pipe['y'] and
            abs(playerx - pipe['x']) < GAME_SPRITES['pipe'][0].get_width()):
            GAME_SOUNDS['hit'].play()
            return True
    # if the above three conditions not ok!, then return false which means it does not crash
    return False

# randomPipe getting function
def getRandomPipe():
        #generating two position of pipes one forward another reverse blitting in the screen
        pipeHeight = GAME_SPRITES['pipe'][0].get_height()
        # pipe height is almost screen's 3 times smaller
        offset = SCREENHEIGHT / 3
        # getting random pipe in range of the offset
        y2 = offset + random.randrange(0,int(SCREENHEIGHT - GAME_SPRITES['base'].get_height() - 1.2 * offset))
        pipex = SCREENWIDTH + 10
        y1 = pipeHeight - y2 + offset
        pipe = [
            {'x':pipex, 'y':-y1},  #Upper pipe
            {'x':pipex, 'y':y2}   #lower pipe
        ]
        # returning pipe in the screen from the randomPipe function
        return pipe

# only applicable when under these function
if __name__ == '__main__':
    pygame.init()   #initializing pygame module
    FPSCLOCK = pygame.time.Clock()   #pygame clock running function initialize which controls FPS
    pygame.display.set_caption("Flappy Bird By Majed")        #pygame caption title name set
    # number png pic loading
    GAME_SPRITES ['numbers'] = (
        pygame.image.load('Gallery/0.png').convert_alpha(),
        pygame.image.load('Gallery/1.png').convert_alpha(),
        pygame.image.load('Gallery/2.png').convert_alpha(),
        pygame.image.load('Gallery/3.png').convert_alpha(),
        pygame.image.load('Gallery/4.png').convert_alpha(),
        pygame.image.load('Gallery/5.png').convert_alpha(),
        pygame.image.load('Gallery/6.png').convert_alpha(),
        pygame.image.load('Gallery/7.png').convert_alpha(),
        pygame.image.load('Gallery/8.png').convert_alpha(),
        pygame.image.load('Gallery/9.png').convert_alpha(),
    )

    GAME_SPRITES ['message'] = pygame.image.load('Gallery/foreground.png').convert_alpha()
    GAME_SPRITES ['base'] = pygame.image.load('Gallery/base.png').convert_alpha()
    GAME_SPRITES ['pipe'] = (
        pygame.image.load(PIPE).convert_alpha(),
        pygame.transform.rotate(pygame.image.load(PIPE).convert_alpha(),180),
    )
    GAME_SPRITES ['background'] = pygame.image.load(BACKGROUND).convert_alpha()
    GAME_SPRITES ['player'] = pygame.image.load(PLAYER).convert_alpha()

    # music files setting
    GAME_SOUNDS ['die'] = pygame.mixer.Sound('Musics/die.wav')
    GAME_SOUNDS ['hit'] = pygame.mixer.Sound('Musics/hit.wav')
    GAME_SOUNDS ['point'] = pygame.mixer.Sound('Musics/point.wav')
    GAME_SOUNDS ['wing'] = pygame.mixer.Sound('Musics/wing.wav')
    GAME_SOUNDS ['swoosh'] = pygame.mixer.Sound('Musics/swoosh.wav')
    GAME_SOUNDS ['lobby'] = pygame.mixer.Sound('Musics/lobby.mp3')

    # when everything is ok while is true then continue the loop
    while True:
         welcomeScreen()  #shows the screen untill the user presses a button
         mainGame()    #this is the main game function
