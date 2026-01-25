import random as r
import tkinter as tk

root = tk.Tk()
root.title("Guess the number")
root.geometry("+600+250")

tk.Label(root, text="Welcome To Guess The Number").pack()
tk.Label(root, text="This game consists of guessing the number between 1 and 10000").pack()

# -------- ESTADO DEL JUEGO -------
game_state = {
    "lives": 7,
    "number_to_guess": None
    }


# -------- UI (Se crea una sola vez) --------
info = tk.Label(root, text="")
info.pack()

tk.Label(root, text="Guess The Number!").pack()

entry = tk.Entry(root)
entry.pack()


result = tk.Label(root, text="")
result.pack()


# --------- LÓGICA DEL JUEGO ---------
def start_game():
    game_state["number_to_guess"] = r.randint(1,10000)
    game_state["lives"] = 7
    
    print(game_state["number_to_guess"])

    start_button.config(state="disabled")
    check_button.config(state="active")

    info.config(text=f"You have {game_state['lives']} lives")
    result.config(text="")
    entry.delete(0, tk.END)

def check():
    try:
        user_number = int(entry.get())
    except ValueError:
        result.config(text="Enter a valid number in a range 1-10000")
        return

    if not 1 <= user_number <= 10000:
        result.config(text="Number must be between 1 and 10000")
        return

    if user_number == game_state["number_to_guess"]:
        result.config(
            text=f"""Congratulations!!! You win with {game_state['lives']} lives left\n
            The number was {game_state['number_to_guess']}""")
        end_game()
    else:
        game_state["lives"] -= 1
        if game_state["lives"] == 0:
            result.config(
                text=f"Game Over. Lives counter = {game_state['lives']}\nThe number was {game_state['number_to_guess']}")
            end_game()
        else: # ><
            if user_number > game_state["number_to_guess"]:
                result.config(
                    text="The number is less")
                
                info.config(
                    text=f"You have {game_state['lives']} lives left to guess")
            else:
                result.config(
                    text="The number is greater")
                
                info.config(
                    text=f"You have {game_state['lives']} lives left to guess")

def end_game():
    check_button.config(state="disabled")
    start_button.config(state="active")


# -------- BOTONES -------
check_button = tk.Button(root, text="Check Number", command=check, width=15, state="disabled")
check_button.pack()

start_button = tk.Button(root, text="Start Game", command=start_game, width=25) 
start_button.pack()



root.mainloop()
































