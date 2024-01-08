import tkinter as tk
import random

window = tk.Tk()
window.title("Symulator Rzutu Kostką")
window.geometry("500x500")

result_label = tk.Label(window, text="Wynik: ", height=7, font=("arial",30))
result_label.pack()


def roll_die():
    result = random.randint(1, 6)
    result_label.config(text=f"Wynik: {result}")


roll_button = tk.Button(
    window,
    text="Rzuć kostką",
    command=roll_die,
    font=("Arial", 18, "bold"),
    fg="white",
    bg="#3498db",
    relief=tk.FLAT,
    padx=20,
    pady=10,
    borderwidth=2,
    activeforeground="white",
    activebackground="#2980b9",
)


roll_button.pack()

window.mainloop()
