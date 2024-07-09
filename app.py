import tkinter as tk
from tkinter import messagebox
import random
import os
import pygame

# Initialize Pygame for sound effects
pygame.mixer.init()

# Load sound effects
click_sound = pygame.mixer.Sound("click.mp3")
win_sound = pygame.mixer.Sound("win.mp3")
lose_sound = pygame.mixer.Sound("lose.mp3")
tie_sound = pygame.mixer.Sound("tie.mp3")

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
        global user_score
        user_score += 1
        play_sound(win_sound)
        return "You win!"
    else:
        global computer_score
        computer_score += 1
        play_sound(lose_sound)
        return "Computer wins!"

# Function to handle user choice
def user_choice(choice):
    play_sound(click_sound)
    computer_choice = random.choice(["Rock", "Paper", "Scissors"])
    result = determine_winner(choice, computer_choice)
    result_label.config(text=f"You chose: {choice}\nComputer chose: {computer_choice}\n{result}")
    score_label.config(text=f"Score - You: {user_score} Computer: {computer_score}")

# Function to reset the game
def reset_game():
    global user_score, computer_score
    user_score = 0
    computer_score = 0
    result_label.config(text="")
    score_label.config(text=f"Score - You: {user_score} Computer: {computer_score}")

# Create main window
root = tk.Tk()
root.title("Rock-Paper-Scissors Game")

# Set up initial scores
user_score = 0
computer_score = 0

# Create labels and buttons
prompt_label = tk.Label(root, text="Choose Rock, Paper, or Scissors:", font=("Arial", 18, "bold"), fg="#333")
prompt_label.pack(pady=20)

button_frame = tk.Frame(root)
button_frame.pack(pady=20)

# Load images for buttons
rock_image = tk.PhotoImage(file="rock.png")
paper_image = tk.PhotoImage(file="paper.png")
scissors_image = tk.PhotoImage(file="scissors.png")

rock_button = tk.Button(button_frame, image=rock_image, command=lambda: user_choice("Rock"))
rock_button.grid(row=0, column=0, padx=20)

paper_button = tk.Button(button_frame, image=paper_image, command=lambda: user_choice("Paper"))
paper_button.grid(row=0, column=1, padx=20)

scissors_button = tk.Button(button_frame, image=scissors_image, command=lambda: user_choice("Scissors"))
scissors_button.grid(row=0, column=2, padx=20)

result_label = tk.Label(root, text="", font=("Arial", 16), fg="#333")
result_label.pack(pady=20)

score_label = tk.Label(root, text=f"Score - You: {user_score} Computer: {computer_score}", font=("Arial", 16, "bold"), fg="#333")
score_label.pack(pady=10)

reset_button = tk.Button(root, text="Reset Game", font=("Arial", 14), bg="#ff6666", fg="#fff", command=reset_game)
reset_button.pack(pady=20)

# Start the GUI main loop
root.mainloop()
