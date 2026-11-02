import tkinter as tk
import random
import string

SYMBOLS = string.ascii_uppercase + string.digits
HEX_DIGITS = "0123456789ABCDEF"

def generate_key():
    hex_part = hex_entry.get().upper()
    dec_number = int(hex_part, 16)
    digits = str(dec_number)
    first_three = digits[:3]
    last_two = digits[-2:]
    blocks = []
    for i in range(3):
        block = []
        position = random.randrange(5)
        for j in range(5):
            if j == position:
                block.append(first_three[i])
            else:
                block.append(random.choice(SYMBOLS))
        blocks.append("".join(block))
    key = "-".join(blocks) + " " + last_two
    key_entry.delete(0, tk.END)
    key_entry.insert(0, key)


window = tk.Tk()
window.geometry("520x320")
window.resizable(False, False)

bg_image = tk.PhotoImage(file="witcher.png")
background = tk.Label(window, image=bg_image)
background.place(x=0, y=0)

title_label = tk.Label(
    window,
    text="KEYGEN",
    font=("Georgia", 16, "bold"),
    fg="#e6e6fa",
    bg="#1b1b2f"
)
title_label.place(x=0, y=20, relwidth=1)

hex_label = tk.Label(
    window,
    text="Введите HEX-число (5 знаков):",
    font=("Verdana", 11),
    fg="white",
    bg="#1b1b2f"
)
hex_label.place(x=40, y=110)

hex_entry = tk.Entry(
    window,
    width=12,
    font=("Consolas", 16),
    justify="center"
)
hex_entry.place(x=40, y=140)

generate_button = tk.Button(
    window,
    text="Сгенерировать ключ",
    font=("Verdana", 11, "bold"),
    bg="#4b0082",
    fg="white",
    command=generate_key
)
generate_button.place(x=260, y=138, width=220, height=32)

key_label = tk.Label(
    window,
    text="Сгенерированный ключ:",
    font=("Verdana", 11),
    fg="white",
    bg="#1b1b2f"
)
key_label.place(x=40, y=210)

key_entry = tk.Entry(
    window,
    width=25,
    font=("Consolas", 16),
    justify="center",
)
key_entry.place(x=40, y=240, width=440, height=34)

window.mainloop()