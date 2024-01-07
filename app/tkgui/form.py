import tkinter as tk
import tkinter.ttk as ttk

from . import funcs


root_window = tk.Tk()
root_window.title("Boosty CSV parser")
root_window.geometry("800x600")

root_window.columnconfigure(0, weight=1)
root_window.columnconfigure(1, weight=0)
root_window.rowconfigure(0, weight=0)
root_window.rowconfigure(1, weight=1)

path_label = ttk.Label(root_window, text="Path to CSV")
label_filename = funcs.FileName(target=path_label)

choose_btn = ttk.Button(
    root_window, text="Choose CSV", command=label_filename.fill_output
)

output_text = tk.Text(
    root_window,
    relief="flat",
    borderwidth=2,
    wrap="word",
    highlightthickness=0,
    font=("Menlo", 12, "normal"),
)
label_filename.text_field = output_text

path_label.grid(row=0, column=0, padx=10, pady=10)
choose_btn.grid(row=0, column=1, padx=10, pady=10, sticky="ew")
output_text.grid(row=1, column=0, columnspan=2, padx=10, pady=10, sticky="nsew")
