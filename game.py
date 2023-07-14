import pygame
import sys
import random
import time

# Initialize Pygame
pygame.init()

# Set up some constants
WIDTH, HEIGHT = 640, 480
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Set up the display
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# Set up assets (you'll need to provide your own images)
ROCK = pygame.image.load('rock.png')
PAPER = pygame.image.load('paper.png')
SCISSORS = pygame.image.load('scissors.png')

# Set up sounds (you'll need to provide your own sounds)
WIN_SOUND = pygame.mixer.Sound('win.wav')
LOSE_SOUND = pygame.mixer.Sound('lose.wav')
TIE_SOUND = pygame.mixer.Sound('tie.wav')

# Set up fonts
FONT = pygame.font.Font(None, 36)

# Set up game variables
player_choice = None
computer_choice = None
game_over = False
winner = None
player_score = 0
computer_score = 0
countdown = 3

def draw_screen():
    screen.fill(WHITE)
    if player_choice:
        screen.blit(player_choice, (WIDTH//3, HEIGHT//2))
    if computer_choice:
        screen.blit(computer_choice, (2*WIDTH//3, HEIGHT//2))
    score_text = FONT.render(f"Score: Player {player_score} - {computer_score} Computer", True, BLACK)
    screen.blit(score_text, (WIDTH//2, HEIGHT//8))
    if game_over:
        winner_text = FONT.render(f"{winner} wins!", True, BLACK)
        screen.blit(winner_text, (WIDTH//2, HEIGHT//4))
    if countdown > 0:
        countdown_text = FONT.render(str(countdown), True, BLACK)
        screen.blit(countdown_text, (WIDTH//2, HEIGHT//2))
    pygame.display.flip()

def handle_input():
    global player_choice, game_over, winner
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if game_over:
                if event.key == pygame.K_r:
                    player_choice = None
                    computer_choice = None
                    game_over = False
                    winner = None
            else:
                if event.key == pygame.K_1:
                    player_choice = ROCK
                elif event.key == pygame.K_2:
                    player_choice = PAPER
                elif event.key == pygame.K_3:
                    player_choice = SCISSORS
                check_winner()

def computer_turn():
    global computer_choice
    # This is a very simple AI that just chooses randomly
    computer_choice = random.choice([ROCK, PAPER, SCISSORS])

def check_winner():
    global game_over, winner, player_score, computer_score
    if player_choice == ROCK and computer_choice == SCISSORS:
        game_over = True
        winner = 'Player'
        player_score += 1
        WIN_SOUND.play()
    elif player_choice == PAPER and computer_choice == ROCK:
        game_over = True
        winner = 'Player'
        player_score += 1
        WIN_SOUND.play()
    elif player_choice == SCISSORS and computer_choice == PAPER:
        game_over = True
        winner = 'Player'
        player_score += 1
        WIN_SOUND.play()
    elif computer_choice == ROCK and player_choice == SCISSORS:
        game_over = True
        winner = 'Computer'
        computer_score += 1
        LOSE_SOUND.play()
    elif computer_choice == PAPER and player_choice == ROCK:
        game_over = True
        winner = 'Computer'
        computer_score += 1
        LOSE_SOUND.play()
    elif computer_choice == SCISSORS and player_choice == PAPER:
        game_over = True
        winner = 'Computer'
        computer_score += 1
        LOSE_SOUND.play()
    elif player_choice == computer_choice:
        TIE_SOUND.play()

def game_loop():
    global countdown
    while True:
        if countdown > 0:
            draw_screen()
            pygame.time.wait(1000)
            countdown -= 1
        else:
            handle_input()
            if not game_over:
                computer_turn()
            draw_screen()
            if game_over:
                pygame.time.wait(2000)
                countdown = 3

# Run the game loop
game_loop()
