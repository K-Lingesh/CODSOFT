import tkinter as tk
from PIL import Image, ImageTk
import random


def get_computer_choice():
    return random.choice(["Rock", "Paper", "Scissors"])

def determine_winner(user, computer):
    if user == computer:
        return "It's a tie!"
    elif (user == "Rock" and computer == "Scissors") or \
         (user == "Scissors" and computer == "Paper") or \
         (user == "Paper" and computer == "Rock"):
        return "You win!"
    else:
        return "Computer wins!"

def play(choice):
    global user_score, computer_score

    computer_choice = get_computer_choice()
    result = determine_winner(choice, computer_choice)

    if result == "You win!":
        user_score += 1
    elif result == "Computer wins!":
        computer_score += 1

    user_choice_label.config(text=f"Your Choice: {choice}")
    computer_choice_label.config(text=f"Computer's Choice: {computer_choice}")
    result_label.config(text=result)
    score_label.config(text=f"Score - You: {user_score} | Computer: {computer_score}")

    play_again_button.config(state="normal")

def reset_round():
    user_choice_label.config(text="Your Choice: ")
    computer_choice_label.config(text="Computer's Choice: ")
    result_label.config(text="")
    play_again_button.config(state="disabled")


user_score = 0
computer_score = 0


root = tk.Tk()
root.title("Rock, Paper, Scissors")
root.geometry("500x600")
root.config(bg="#f5f7fa")

heading = tk.Label(root, text="Rock, Paper, Scissors", font=("Helvetica", 22, "bold"), bg="#f5f7fa", fg="#333")
heading.pack(pady=20)


rock_img = Image.open("rock.png").resize((100, 100))
rock_photo = ImageTk.PhotoImage(rock_img)

paper_img = Image.open("paper.png").resize((100, 100))
paper_photo = ImageTk.PhotoImage(paper_img)

scissors_img = Image.open("scissors.png").resize((100, 100))
scissors_photo = ImageTk.PhotoImage(scissors_img)


button_frame = tk.Frame(root, bg="#f5f7fa")
button_frame.pack(pady=10)

rock_button = tk.Button(button_frame, image=rock_photo, command=lambda: play("Rock"), bd=0, bg="#f5f7fa", activebackground="#d1e7dd")
rock_button.grid(row=0, column=0, padx=20)

paper_button = tk.Button(button_frame, image=paper_photo, command=lambda: play("Paper"), bd=0, bg="#f5f7fa", activebackground="#fff3cd")
paper_button.grid(row=0, column=1, padx=20)

scissors_button = tk.Button(button_frame, image=scissors_photo, command=lambda: play("Scissors"), bd=0, bg="#f5f7fa", activebackground="#f8d7da")
scissors_button.grid(row=0, column=2, padx=20)


user_choice_label = tk.Label(root, text="Your Choice: ", font=("Helvetica", 16), bg="#f5f7fa", fg="#555")
user_choice_label.pack(pady=15)

computer_choice_label = tk.Label(root, text="Computer's Choice: ", font=("Helvetica", 16), bg="#f5f7fa", fg="#555")
computer_choice_label.pack(pady=15)

result_label = tk.Label(root, text="", font=("Helvetica", 18, "bold"), bg="#f5f7fa", fg="#0d6efd")
result_label.pack(pady=20)

score_label = tk.Label(root, text="Score - You: 0 | Computer: 0", font=("Helvetica", 16), bg="#f5f7fa", fg="#333")
score_label.pack(pady=10)


play_again_button = tk.Button(root, text="Play Again", font=("Helvetica", 14), bg="#0d6efd", fg="white",
                              activebackground="#0b5ed7", activeforeground="white",
                              padx=20, pady=5, command=reset_round, state="disabled")
play_again_button.pack(pady=20)

root.mainloop()
