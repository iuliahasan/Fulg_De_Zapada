import tkinter as tk
from tkinter import messagebox
from Services.authentication import register

class RegisterWindow:
    def __init__(self):
        self.window = tk.Toplevel()
        self.window.title("Inregistrare")
        self.window.geometry("500x300")

        tk.Label(self.window, text="Utilizator").pack(pady=5)
        self.username = tk.Entry(self.window)
        self.username.pack(fill='x' ,padx=5)

        tk.Label(self.window, text="Parola").pack(pady=5)
        self.password = tk.Entry(self.window, show='*')
        self.password.pack(fill='x', padx=5)

        tk.Label(
            self.window,
            text="Confirmare parola"
        ).pack(pady=5)
        self.confirm_password = tk.Entry(
            self.window,
            show="*"
        )
        self.confirm_password.pack(fill="x", padx=20)

        tk.Button(
            self.window,
            text="Inregistrare",
            command=self.register_user
        ).pack(pady=20)

    def register_user(self):
        username = self.username.get().strip()
        password = self.password.get().strip()
        confirm_password = self.confirm_password.get().strip()

        if not username or not password:
            messagebox.showerror("Eroare", 'Completati toate campurile')

            return

        if password != confirm_password:
            messagebox.showerror("Eroare", 'Parole diferite')

            return

        success = register(username, password)

        if success:
            messagebox.showinfo("Succes", 'Cont creat cu succes')
            self.window.destroy()
        else:
            messagebox.showerror("Eroare", 'Utilizatorul exista')