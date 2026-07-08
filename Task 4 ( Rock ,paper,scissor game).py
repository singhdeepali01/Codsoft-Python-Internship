import tkinter as tk
from tkinter import messagebox
import random

# ---------------- COLORS ----------------
BG_COLOR = "#FFE4E8"
BTN_COLOR = "#F4A6B8"
HEADER_COLOR = "#E57C9A"
TEXT_COLOR = "#5A2A36"

# ---------------- VARIABLES ----------------
history = []
player1_score = 0
player2_score = 0

symbols = {
    "Rock": "🪨",
    "Paper": "📄",
    "Scissors": "✂️"
}

# ---------------- CREATE WINDOW FIRST ----------------
root = tk.Tk()
root.title("Rock Paper Scissors")
root.geometry("750x800")
root.configure(bg=BG_COLOR)

# -------- NOW CREATE TK VARIABLES --------
mode = tk.StringVar(value="computer")
player1_choice = tk.StringVar(value="Rock")
player2_choice = tk.StringVar(value="Rock")


# ---------------- FUNCTIONS ----------------
def decide_winner(choice1, choice2):
    if choice1 == choice2:
        return "Draw"

    if (
        (choice1 == "Rock" and choice2 == "Scissors") or
        (choice1 == "Paper" and choice2 == "Rock") or
        (choice1 == "Scissors" and choice2 == "Paper")
    ):
        return "Player1"

    return "Player2"


def update_history(c1, c2, winner):
    history.append(f"{c1} vs {c2}  -->  {winner}")

    if len(history) > 10:
        history.pop(0)

    history_box.delete(0, tk.END)

    for item in history:
        history_box.insert(tk.END, item)


def play_with_computer(choice):
    global player1_score, player2_score

    player_name = player1_entry.get().strip()

    if player_name == "":
        player_name = "Player"

    computer_choice = random.choice(
        ["Rock", "Paper", "Scissors"]
    )

    result = decide_winner(choice, computer_choice)

    if result == "Player1":
        player1_score += 1
        winner_text = f"{player_name} Wins!"
    elif result == "Player2":
        player2_score += 1
        winner_text = "Computer Wins!"
    else:
        winner_text = "Draw Match!"

    score_label.config(
        text=f"Score : {player_name} = {player1_score} | Computer = {player2_score}"
    )

    result_label.config(text=winner_text)

    player_display.config(
        text=f"{player_name}: {symbols[choice]}"
    )

    opponent_display.config(
        text=f"Computer: {symbols[computer_choice]}"
    )

    update_history(choice, computer_choice, winner_text)


def play_with_friend():
    global player1_score, player2_score

    name1 = player1_entry.get().strip()
    name2 = player2_entry.get().strip()

    if name1 == "" or name2 == "":
        messagebox.showerror(
            "Error",
            "Please enter both player names."
        )
        return

    choice1 = player1_choice.get()
    choice2 = player2_choice.get()

    result = decide_winner(choice1, choice2)

    if result == "Player1":
        player1_score += 1
        winner_text = f"{name1} Wins!"
    elif result == "Player2":
        player2_score += 1
        winner_text = f"{name2} Wins!"
    else:
        winner_text = "Draw Match!"

    score_label.config(
        text=f"Score : {name1} = {player1_score} | {name2} = {player2_score}"
    )

    result_label.config(text=winner_text)

    player_display.config(
        text=f"{name1}: {symbols[choice1]}"
    )

    opponent_display.config(
        text=f"{name2}: {symbols[choice2]}"
    )

    update_history(choice1, choice2, winner_text)


def change_mode():
    if mode.get() == "computer":
        friend_frame.pack_forget()
        computer_frame.pack(pady=15)
    else:
        computer_frame.pack_forget()
        friend_frame.pack(pady=15)


# ---------------- TITLE ----------------
title = tk.Label(
    root,
    text="🪨 📄 ✂️ ROCK PAPER SCISSORS ✂️ 📄 🪨",
    bg=HEADER_COLOR,
    fg="white",
    font=("Arial", 18, "bold"),
    pady=10
)

title.pack(fill="x")

# ---------------- MODE ----------------
mode_frame = tk.Frame(root, bg=BG_COLOR)
mode_frame.pack(pady=10)

tk.Radiobutton(
    mode_frame,
    text="Play With Computer",
    variable=mode,
    value="computer",
    bg=BG_COLOR,
    command=change_mode
).pack(side="left", padx=15)

tk.Radiobutton(
    mode_frame,
    text="Play With Friend",
    variable=mode,
    value="friend",
    bg=BG_COLOR,
    command=change_mode
).pack(side="left", padx=15)

# ---------------- NAME ENTRY ----------------
name_frame = tk.Frame(root, bg=BG_COLOR)
name_frame.pack(pady=10)

tk.Label(
    name_frame,
    text="Player 1 Name:",
    bg=BG_COLOR,
    fg=TEXT_COLOR,
    font=("Arial", 11, "bold")
).grid(row=0, column=0, padx=10)

player1_entry = tk.Entry(name_frame, width=20)
player1_entry.grid(row=0, column=1)

tk.Label(
    name_frame,
    text="Player 2 Name:",
    bg=BG_COLOR,
    fg=TEXT_COLOR,
    font=("Arial", 11, "bold")
).grid(row=0, column=2, padx=10)

player2_entry = tk.Entry(name_frame, width=20)
player2_entry.grid(row=0, column=3)

# ---------------- SCORE ----------------
score_label = tk.Label(
    root,
    text="Score : Player = 0 | Computer = 0",
    bg=BG_COLOR,
    fg=TEXT_COLOR,
    font=("Arial", 14, "bold")
)

score_label.pack(pady=10)

# ---------------- RESULT ----------------
result_label = tk.Label(
    root,
    text="Choose your move",
    bg=BG_COLOR,
    fg="red",
    font=("Arial", 16, "bold")
)

result_label.pack()

player_display = tk.Label(
    root,
    text="Player:",
    bg=BG_COLOR,
    font=("Arial", 18)
)

player_display.pack()

opponent_display = tk.Label(
    root,
    text="Opponent:",
    bg=BG_COLOR,
    font=("Arial", 18)
)

opponent_display.pack()

# ---------------- COMPUTER MODE BUTTONS ----------------
computer_frame = tk.Frame(root, bg=BG_COLOR)
computer_frame.pack(pady=15)

for option in ["Rock", "Paper", "Scissors"]:
    tk.Button(
        computer_frame,
        text=f"{symbols[option]}\n{option}",
        bg=BTN_COLOR,
        width=12,
        height=3,
        font=("Arial", 12, "bold"),
        command=lambda x=option: play_with_computer(x)
    ).pack(side="left", padx=10)

# ---------------- FRIEND MODE ----------------
friend_frame = tk.Frame(root, bg=BG_COLOR)

tk.Label(
    friend_frame,
    text="Player 1 Choice",
    bg=BG_COLOR
).grid(row=0, column=0)

tk.OptionMenu(
    friend_frame,
    player1_choice,
    "Rock",
    "Paper",
    "Scissors"
).grid(row=1, column=0, padx=20)

tk.Label(
    friend_frame,
    text="Player 2 Choice",
    bg=BG_COLOR
).grid(row=0, column=1)

tk.OptionMenu(
    friend_frame,
    player2_choice,
    "Rock",
    "Paper",
    "Scissors"
).grid(row=1, column=1, padx=20)

tk.Button(
    friend_frame,
    text="Play Match",
    bg=BTN_COLOR,
    font=("Arial", 12, "bold"),
    command=play_with_friend
).grid(row=2, column=0, columnspan=2, pady=15)

# ---------------- HISTORY ----------------
history_title = tk.Label(
    root,
    text="Match History (Last 10 Matches)",
    bg=BG_COLOR,
    fg=TEXT_COLOR,
    font=("Arial", 13, "bold")
)

history_title.pack(pady=10)

history_box = tk.Listbox(
    root,
    width=50,
    height=10,
    font=("Arial", 10)
)

history_box.pack()

root.mainloop()