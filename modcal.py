from tkinter import *
import tkinter.font as font

# ---------- Functions ----------
def press(key):
    global expr
    expr += str(key)
    display.set(expr)

def equal():
    global expr
    try:
        result = str(eval(expr))
        display.set(result)
        expr = result  # keep result so user can continue
    except Exception:
        display.set("error")
        expr = ""

def clear():
    global expr
    expr = ""
    display.set("")

def backspace():
    global expr
    expr = expr[:-1]
    display.set(expr)

def on_enter(e):
    e.widget['bg'] = e.widget.hover_bg

def on_leave(e):
    e.widget['bg'] = e.widget.normal_bg

def make_button(master, text, row, col, colspan=1, cmd=None,
                bg="#3b3b3b", fg="white"):
    btn = Button(
        master, text=text, fg=fg, bg=bg, bd=0,
        font=calc_font, relief="flat", activeforeground=fg,
        activebackground=bg, height=2
    )
    btn.normal_bg = bg
    btn.hover_bg = "#555555"
    btn.bind("<Enter>", on_enter)
    btn.bind("<Leave>", on_leave)
    if cmd is None:
        btn.config(command=lambda t=text: press(t))
    else:
        btn.config(command=cmd)
    btn.grid(row=row, column=col, columnspan=colspan,
             padx=5, pady=5, sticky="nsew")
    return btn

# ---------- Main window ----------
root = Tk()
root.title("Modern Calculator - Mini Project")
root.geometry("320x420")
root.configure(bg="#1e1e2f")
root.resizable(False, False)

# Fonts
calc_font = font.Font(family='Segoe UI', size=13, weight='bold')
display_font = font.Font(family='Consolas', size=22, weight='bold')

# ---------- Display ----------
display = StringVar()
expr = ""

display_frame = Frame(root, bg="#1e1e2f")
display_frame.pack(expand=True, fill="both")

entry = Entry(
    display_frame, textvariable=display, font=display_font,
    justify='right', bd=0, bg="#25253a", fg="#ecf0f1",
    relief="flat", insertbackground="white"
)
entry.pack(expand=True, fill="both", padx=12, pady=15, ipady=12)

# ---------- Buttons area ----------
btn_frame = Frame(root, bg="#1e1e2f")
btn_frame.pack(expand=True, fill="both")

for i in range(5):
    btn_frame.grid_rowconfigure(i, weight=1)
for i in range(4):
    btn_frame.grid_columnconfigure(i, weight=1)

# Color theme
num_bg = "#34495e"
op_bg = "#ff7675"
spec_bg = "#636e72"
eq_bg = "#00b894"

# First row: C, ⌫, %, /
make_button(btn_frame, "C", 0, 0, cmd=clear, bg=spec_bg)
make_button(btn_frame, "⌫", 0, 1, cmd=backspace, bg=spec_bg)
make_button(btn_frame, "%", 0, 2, bg=op_bg)
make_button(btn_frame, "/", 0, 3, bg=op_bg)

# Second row: 7 8 9 *
make_button(btn_frame, "7", 1, 0, bg=num_bg)
make_button(btn_frame, "8", 1, 1, bg=num_bg)
make_button(btn_frame, "9", 1, 2, bg=num_bg)
make_button(btn_frame, "*", 1, 3, bg=op_bg)

# Third row: 4 5 6 -
make_button(btn_frame, "4", 2, 0, bg=num_bg)
make_button(btn_frame, "5", 2, 1, bg=num_bg)
make_button(btn_frame, "6", 2, 2, bg=num_bg)
make_button(btn_frame, "-", 2, 3, bg=op_bg)

# Fourth row: 1 2 3 +
make_button(btn_frame, "1", 3, 0, bg=num_bg)
make_button(btn_frame, "2", 3, 1, bg=num_bg)
make_button(btn_frame, "3", 3, 2, bg=num_bg)
make_button(btn_frame, "+", 3, 3, bg=op_bg)

# Fifth row: 00 0 . =
make_button(btn_frame, "00", 4, 0, bg=num_bg)
make_button(btn_frame, "0", 4, 1, bg=num_bg)
make_button(btn_frame, ".", 4, 2, bg=num_bg)
make_button(btn_frame, "=", 4, 3, cmd=equal, bg=eq_bg)

root.mainloop()
