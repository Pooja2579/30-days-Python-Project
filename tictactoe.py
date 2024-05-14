import tkinter as tk
from tkinter import messagebox #For messagebox

def check_winner():
    for combo in [[0,1,2], [3,4,5], [6,7,8], [0,3,6], [1,4,7], [2,5,8], [0,4,8], [2,4,6]]:
        if buttons[combo[0]]["text"] == buttons[combo[1]]["text"] == buttons[combo[2]]["text"] !="":
            buttons[combo[0]].config(bg="green")
            buttons[combo[1]].config(bg="green")
            buttons[combo[2]].config(bg="green")
            messagebox.showinfo("Tic-Tac-Toe", f"Player {buttons[combo[0]]['text']} wins!")
            root.quiet()

def button_click(index):
    if buttons[index]["text"] == "" and not winner:
       buttons[index]["text"] = current_palyer
       check_winner()
       toggle_player()

#crearting toggle_player
def toggle_player():
    global current_palyer
    current_palyer = "X" if current_palyer == "O" else "O"
    label.config(text=f"player {current_palyer}'s turn")

#making root
root = tk.Tk()
root.title("Tic-Tac_Toe")

buttons = [tk.Button(root, text="", font=("normal", 25), width=6, height=2, command=lambda i =i: button_click(i)) for i in range(9)]


for i, button in enumerate(buttons):
    button.grid(row=i //3, column=i % 3)

#making cuurent player

current_palyer = "X"
winner = False
label = tk.Label(root, text=f"Player {current_palyer}'s turn", font={"normaal", 16})
label.grid(row=3, column = 0, columnspan=3)

root.mainloop()