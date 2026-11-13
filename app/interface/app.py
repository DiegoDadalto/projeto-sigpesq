import tkinter as tk
from app.interface.login import TelaLogin

class SigPesq(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("SigPesq")
        self.geometry("1280x720")

        self.login = TelaLogin(self)

        self.login.pack(
            fill="both",
            expand=True
        )