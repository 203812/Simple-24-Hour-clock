import tkinter as tk
from time import strftime

root = tk.Tk()
root.title("Digital 24-Hour Clock")
root.geometry("800x400")
root.configure(bg="#0f172a")
root.resizable(False, False)

def update_clock():
    current_time = strftime("%H:%M:%S")
    current_date = strftime("%d-%m-%Y")
    current_day = strftime("%A")

    time_label.config(text=current_time)
    date_label.config(text=f"{current_day} | {current_date}")

    root.after(1000, update_clock)

main_frame = tk.Frame(root, bg="#1e293b")
main_frame.place(relx=0.5, rely=0.5, anchor="center")

time_label = tk.Label(
    main_frame,
    font=("Consolas", 90, "bold"),
    bg="#1e293b",
    fg="#38bdf8",
    padx=30,
    pady=20
)
time_label.pack()

date_label = tk.Label(
    main_frame,
    font=("Segoe UI", 28),
    bg="#1e293b",
    fg="#f8fafc"
)
date_label.pack()

update_clock()
root.mainloop()
