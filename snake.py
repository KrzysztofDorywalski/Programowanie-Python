import pygame, sys, random, winsound
from pygame.math import Vector2

pygame.init()
GREEN = (173, 204, 96)
DARK_GREEN = (43, 51, 24)

cell_size = 30
number_of_cells = 25

class Food:
    def __init__(self):
        self.position = self.gen_random_pos()
    def draw(self):
        food_rect = pygame.Rect(self.position.x*cell_size, self.position.y*cell_size, cell_size, cell_size)
        pygame.draw.rect(screen, DARK_GREEN, food_rect)
    def gen_random_pos(self):
        x = random.randint(0, number_of_cells-1)
        y = random.randint(0, number_of_cells-1)
        position = Vector2(x,y)
        return position

class Snake:
    def __init__(self):
        self.reset()
    def draw(self):
        for segment in self.body:
            segment_rect = (segment.x*cell_size, segment.y*cell_size, cell_size, cell_size)
            pygame.draw.rect(screen, DARK_GREEN, segment_rect,0,7)
    def update(self):
        if self.add_segment == True:
            self.body.insert(0, self.body[0]+self.direction)
            self.add_segment = False
        else:
            self.body = self.body[:-1]
            self.body.insert(0, self.body[0]+self.direction)
    def reset(self):
        self.body = [Vector2(6,9), Vector2(5,9), Vector2(4,9)]
        self.direction = Vector2(1,0)
        self.add_segment = False

screen = pygame.display.set_mode((cell_size*number_of_cells, cell_size*number_of_cells ))
pygame.display.set_caption("Moj Snake")
clock = pygame.time.Clock()

food = Food()
snake = Snake()

SNAKE_UPDATE = pygame.USEREVENT
pygame.time.set_timer(SNAKE_UPDATE, 200)

def game_over():
        print('koniec')
        snake.reset()
        food.position = food.gen_random_pos()
        winsound.Beep(2500, 1000)

while True:
    for event in pygame.event.get():
        if event.type == SNAKE_UPDATE:
            snake.update()
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and snake.direction != Vector2(0,1):
                snake.direction = Vector2(0,-1)
            if event.key == pygame.K_DOWN and snake.direction != Vector2(0,-1):
                snake.direction = Vector2(0, 1)
            if event.key == pygame.K_LEFT and snake.direction != Vector2(1,0):
                snake.direction = Vector2(-1, 0)
            if event.key == pygame.K_RIGHT and snake.direction != Vector2(-1,0):
                snake.direction = Vector2(1, 0)

    screen.fill(GREEN)
    food.draw()
    snake.draw()
    #snake.update()
    
    if snake.body[0] == food.position:
        food.position = food.gen_random_pos()
        snake.add_segment = True
    if snake.body[0].x == number_of_cells or snake.body[0].x == -1:
        game_over()
    if snake.body[0].y == number_of_cells or snake.body[0].y == -1:
        game_over()
    hadless_body = snake.body[1:]
    if snake.body[0] in hadless_body:
        game_over()
    pygame.display.update()
    clock.tick(60)