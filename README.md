# Pong
import pygame
import sys
# setup
pygame.init()

clock = pygame.time.Clock()
Black = (0, 0, 0)
White = (255, 255, 255)
Teal = (12, 201, 157)
Purple = (153, 51, 255)
Grey = (200, 200, 200)

screen_width = 500
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Pong')


def ball():
    global ball_speed_x, ball_speed_y

    ball.x += ball_speed_x
    ball.y += ball_speed_y

    if ball.top <= 0 or ball.bottom >= screen_height:
        ball_speed_y *= -1
    if ball.left <= 0 or ball.right >= screen_width:
        ball_speed_x *= -1

    if ball.colliderect(player) or ball.colliderect(opponent):
        ball_speed_x *= -1


def player():
    player.y += player_speed

    if player.top <= 0:
        player.top = 0
    if player.bottom >= screen_height:
        player.bottom = screen_height


# platforms
ball = pygame.Rect(screen_width/2 - 15, screen_height/2 - 15, 30, 30)
player = pygame.Rect(screen_width - 20, screen_width/2 - 30, 10, 140)
opponent = pygame.Rect(10, screen_height/2 - 70, 10, 140)

ball_speed_x = 7
ball_speed_y = 7
player_speed = 0

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                player_speed += 7
            if event.key == pygame.K_DOWN:
                player_speed -= 7
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_DOWN:
                player_speed -= 7
            if event.key == pygame.K_UP:
                player_speed += 7
    ball()
    player.y += player_speed
    # visuals
    screen.fill(White)
    pygame.draw.rect(screen, Teal, player)
    pygame.draw.rect(screen, Purple, opponent)
    pygame.draw.ellipse(screen, Grey, ball)
    pygame.draw.aaline(screen, Black, (screen_width/2, 0),
                       (screen_width/2, screen_height))

    pygame.display.flip()
    clock.tick(60)
