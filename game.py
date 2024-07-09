import pygame
import random
import time

# Initialize Pygame
pygame.init()

# Screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)

# Load images
rock_image = pygame.image.load('rock.png')
paper_image = pygame.image.load('paper.png')
scissors_image = pygame.image.load('scissors.png')

# Resize images
rock_image = pygame.transform.scale(rock_image, (150, 150))
paper_image = pygame.transform.scale(paper_image, (150, 150))
scissors_image = pygame.transform.scale(scissors_image, (150, 150))

# Load sounds
click_sound = pygame.mixer.Sound("click.mp3")
win_sound = pygame.mixer.Sound("win.mp3")
lose_sound = pygame.mixer.Sound("lose.mp3")
tie_sound = pygame.mixer.Sound("tie.mp3")

# Function to display text on the screen
def display_text(screen, text, size, color, x, y):
    font = pygame.font.Font(None, size)
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect(center=(x, y))
    screen.blit(text_surface, text_rect)

# Function to play sound
def play_sound(sound):
    pygame.mixer.Sound.play(sound)

# Function to determine the winner
def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        play_sound(tie_sound)
        return "It's a tie!"
    elif (user_choice == "Rock" and computer_choice == "Scissors") or \
         (user_choice == "Paper" and computer_choice == "Rock") or \
         (user_choice == "Scissors" and computer_choice == "Paper"):
        play_sound(win_sound)
        return "You win!"
    else:
        play_sound(lose_sound)
        return "Computer wins!"

# Main game function
def game_loop():
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Rock-Paper-Scissors Game")
    
    user_score = 0
    computer_score = 0
    
    clock = pygame.time.Clock()
    running = True
    
    while running:
        screen.fill(WHITE)
        
        # Display instructions
        display_text(screen, "Choose Rock, Paper, or Scissors", 36, BLACK, SCREEN_WIDTH // 2, 50)
        
        # Calculate positions for images
        rock_position = (100, 200)
        paper_position = (325, 200)
        scissors_position = (550, 200)
        
        # Display images as buttons
        screen.blit(rock_image, rock_position)
        screen.blit(paper_image, paper_position)
        screen.blit(scissors_image, scissors_position)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = event.pos
                if rock_position[0] <= mouse_x <= rock_position[0] + 150 and rock_position[1] <= mouse_y <= rock_position[1] + 150:
                    play_sound(click_sound)
                    user_choice = "Rock"
                elif paper_position[0] <= mouse_x <= paper_position[0] + 150 and paper_position[1] <= mouse_y <= paper_position[1] + 150:
                    play_sound(click_sound)
                    user_choice = "Paper"
                elif scissors_position[0] <= mouse_x <= scissors_position[0] + 150 and scissors_position[1] <= mouse_y <= scissors_position[1] + 150:
                    play_sound(click_sound)
                    user_choice = "Scissors"
                else:
                    continue
                
                computer_choice = random.choice(["Rock", "Paper", "Scissors"])
                result = determine_winner(user_choice, computer_choice)
                
                # Display choices and result with animation
                for _ in range(30):
                    screen.fill(WHITE)
                    display_text(screen, f"You chose: {user_choice}", 30, BLACK, SCREEN_WIDTH // 2, 350)
                    display_text(screen, f"Computer chose: {computer_choice}", 30, BLACK, SCREEN_WIDTH // 2, 400)
                    pygame.display.update()
                    time.sleep(0.01)
                
                display_text(screen, result, 36, BLACK, SCREEN_WIDTH // 2, 450)
                if result == "You win!":
                    user_score += 1
                elif result == "Computer wins!":
                    computer_score += 1
                
                display_text(screen, f"Score - You: {user_score} Computer: {computer_score}", 30, BLACK, SCREEN_WIDTH // 2, 500)
                pygame.display.update()
                time.sleep(2)
        
        # Display current score
        display_text(screen, f"Score - You: {user_score} Computer: {computer_score}", 30, BLACK, SCREEN_WIDTH // 2, 550)
        
        pygame.display.update()
        clock.tick(60)
    
    pygame.quit()

if __name__ == "__main__":
    game_loop()
