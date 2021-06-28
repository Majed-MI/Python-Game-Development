# Snake & Apple Game
import pygame
from pygame.locals import *
import time
import random

SIZE = 40
BACKGROUND_COLOR = (110, 110, 5)

class Apple:
    def __init__(self,parent_screen):
        self.image = pygame.image.load("Gallery/apple.jpg").convert()
        self.parent_screen = parent_screen
        self.x = 120
        self.y = 120

    def draw(self):
        self.parent_screen.blit(self.image, (self.x, self.y))
        pygame.display.flip()

    def move(self):
        self.x = random.randint(1,18)*SIZE
        self.y = random.randint(1,12)*SIZE

class Snake:
    def __init__(self,parent_screen):
        self.parent_screen = parent_screen
        self.image = pygame.image.load("Gallery/block.jpg").convert()
        self.direction = 'down'
        self.length = 1
        self.x = [40]
        self.y = [40]

    def move_left(self):
        self.direction = 'left'

    def move_right(self):
        self.direction = 'right'

    def move_down(self):
        self.direction = 'down'

    def move_up(self):
        self.direction = 'up'

    def walk(self):
        for i in range(self.length-1,0,-1):
            self.x[i] = self.x[i-1]
            self.y[i] = self.y[i-1]

        if self.direction == 'up':
            self.y[0] -= SIZE
        if self.direction == 'down':
            self.y[0] += SIZE
        if self.direction == 'left':
            self.x[0] -= SIZE
        if self.direction == 'right':
            self.x[0] += SIZE
        self.draw()

    def draw(self):
        for i in range(self.length):
            self.parent_screen.blit(self.image, (self.x[i], self.y[i]))
        pygame.display.flip()

    def increase_length(self):
        self.length += 1
        self.x.append(-1)
        self.y.append(-1)

class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption("Snake & Apple Game")
        pygame.mixer.init()
        self.play_background_music()
        self.surface = pygame.display.set_mode((800,560))  # Setting the screen
        self.snake = Snake(self.surface)
        self.snake.draw()
        self.apple = Apple(self.surface)
        self.apple.draw()

    def play_background_music(self):
        pygame.mixer.music.load("Musics/bg_music.mp3")
        pygame.mixer.music.play(-1,0)

    def is_collision(self,x1,y1,x2,y2):
        if x1 >= x2 and x1 < x2 + SIZE:
            if y1 >= y2 and y1 < y2 + SIZE:
                return True
        return False

    def render_background(self):
        bg = pygame.image.load("Gallery/background.jpg")
        self.surface.blit(bg,(0,0))

    def play(self):
        self.render_background()
        self.snake.walk()
        self.apple.draw()
        self.display_score()
        pygame.display.flip()

        #Snake colliding with apple
        if self.is_collision(self.snake.x[0],self.snake.y[0],self.apple.x,self.apple.y):
            point = pygame.mixer.Sound("Musics/point.wav")
            pygame.mixer.Sound.play(point)
            # print("Collision Occured")
            self.snake.increase_length()
            self.apple.move()

        # Snake Colliding with its body
        for i in range(3,self.snake.length):
            if self.is_collision(self.snake.x[0],self.snake.y[0],self.snake.x[i],self.snake.y[i]):
                hit = pygame.mixer.Sound("Musics/hit.wav")
                pygame.mixer.Sound.play(hit)
                raise "Collision Occured"

        # Snake colliding with boundary
        if not (0 <= self.snake.x[0] <= 800 and 0 <= self.snake.y[0] <= 560):
            hit = pygame.mixer.Sound("Musics/hit.wav")
            pygame.mixer.Sound.play(hit)
            raise "Hit the boundry error"

    def show_game_over(self):
        self.render_background()
        font = pygame.font.SysFont("arial",30)
        line1 = font.render(f"Game is over", True, (255, 255, 255))
        self.surface.blit(line1,(320,190))
        line2 = font.render(f"----- Your Score is : {self.snake.length-1} -----", True, (255, 255, 255))
        self.surface.blit(line2,(255,240))
        line3 = font.render(f"To Play press Enter and to Exit press Escape", True,(255,255,255))
        self.surface.blit(line3,(170,290))
        pygame.mixer.music.pause()
        pygame.display.flip()

    def reset(self):
        self.snake = Snake(self.surface)
        self.apple = Apple(self.surface)

    def display_score(self):
        font = pygame.font.SysFont("arial",30)
        score = font.render(f"Score : {self.snake.length-1}", True,(200,200,200))
        self.surface.blit(score,(680,10))

    def run(self):
        # declare running as True so untillit is false it will be running the game
        running = True
        pause = False
        # while loop to conitnue
        while running:
            for event in pygame.event.get():
                # if it is any other key it will be ok unless it is escape key
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        running = False
                    if event.key == K_RETURN:
                        pygame.mixer.music.unpause()
                        pause = False
                    if not pause:
                        if event.key == K_u:
                            self.snake.move_up()
                        if event.key == K_j:
                            self.snake.move_down()
                        if event.key == K_h:
                            self.snake.move_left()
                        if event.key == K_k:
                            self.snake.move_right()

                # when the user clicks X button then close it
                elif event.type == QUIT:
                    running = False
            try:
                if not pause:
                    self.play()

            except Exception as e:
                self.show_game_over()
                pause = True
                self.reset()

            time.sleep(0.1)


if __name__ == '__main__':
    game = Game()
    game.run()






