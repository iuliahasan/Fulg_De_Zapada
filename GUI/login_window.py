import tkinter as tk
from tkinter import messagebox
from GUI.chatbot_window import ChatbotWindow
from GUI.register_window import RegisterWindow

class LoginWindow:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title('Autentificare')
        self.window.geometry('500x500')

        tk.Label(self.window, text='Utilizator: ').pack(pady=(20, 5))

        self.username_entry = tk.Entry(self.window)
        self.username_entry.pack(fill='x', pady=20)
        tk.Label(self.window, text='Parola: ').pack(pady=(20, 5))

        self.password_entry = tk.Entry(self.window, show='*')
        self.password_entry.pack(fill='x', padx=20)

        self.login_button = tk.Button(self.window, text='Login', command=self.login)
        self.login_button.pack(pady=20)

        self.register_button = tk.Button(self.window, text='Register', command=self.register)
        self.register_button.pack(pady=20)

    def login(self):
        username = self.username_entry.get().strip()
        password = self.password_entry.get().strip()

        if not username or not password:
            messagebox.showerror('Eroare', 'Completati campurile de logare!')
            return

        if username == 'user' and password == 'password':
            messagebox.showinfo('Felicitari', 'Te-ai logat cu succes!')
            self.window.destroy()

            import chatbot_window
        else:
            messagebox.showerror('Eroare', 'Utilizator sau parola incorecta!')

    def register(self):
        RegisterWindow()

    def run(self):
        self.window.mainloop()