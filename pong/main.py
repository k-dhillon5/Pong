import pygame
import sys
import random
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


def move_ball():
    global ball_speed_x, ball_speed_y, playerScore, oppScore

    ball.x += ball_speed_x
    ball.y += ball_speed_y

    if ball.top <= 0 or ball.bottom >= screen_height:
        ball_speed_y *= -1

    if ball.left <= 0:
        playerScore += 1
        ball_restart()

    if ball.right >= screen_width:
        ball_restart()
        oppScore += 1

    if ball.colliderect(player) or ball.colliderect(opponent):
        ball_speed_x *= -1


def move_player():
    player.y += player_speed

    if player.top <= 0:
        player.top = 0
    if player.bottom >= screen_height:
        player.bottom = screen_height


def auto_opp():
    if opponent.top < ball.y:
        opponent.top += opponent_speed
    if opponent.bottom > ball.y:
        opponent.bottom -= opponent_speed
    if opponent.top <= 0:
        opponent.top = 0
    if opponent.bottom >= screen_height:
        opponent.bottom = screen_height


def ball_restart():
    global ball_speed_x, ball_speed_y

    ball.center = (screen_width/2, screen_height/2)
    ball_speed_y *= random.choice((1, -1))
    ball_speed_x *= random.choice((1, -1))


# platforms
ball = pygame.Rect(screen_width/2 - 15, screen_height/2 - 15, 30, 30)
player = pygame.Rect(screen_width - 20, screen_width/2 - 30, 10, 140)
opponent = pygame.Rect(10, screen_height/2 - 70, 10, 140)

ball_speed_x = 6
ball_speed_y = 6
player_speed = 0
opponent_speed = 7

playerScore = 0
oppScore = 0
scoretext = pygame.font.Font("freesansbold.ttf", 30)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                player_speed -= 6
            if event.key == pygame.K_DOWN:
                player_speed += 6
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_DOWN:
                player_speed -= 6
            if event.key == pygame.K_UP:
                player_speed += 6
    move_ball()
    move_player()
    auto_opp()
    # visuals
    screen.fill(White)
    pygame.draw.rect(screen, Teal, player)
    pygame.draw.rect(screen, Purple, opponent)
    pygame.draw.ellipse(screen, Grey, ball)
    pygame.draw.aaline(screen, Black, (screen_width/2, 0),
                       (screen_width/2, screen_height))

    playerText = scoretext.render(f"{playerScore}", False, Grey)
    screen.blit(playerText, (280, 30))

    oppText = scoretext.render(f"{oppScore}", False, Grey)
    screen.blit(oppText, (200, 30))

    pygame.display.flip()
    clock.tick(60)
