import tkinter as tk
from tkinter.scrolledtext import ScrolledText
from Services.chatbot import get_answer

class ChatbotWindow:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title('FULG DE ZAPADA')
        self.window.geometry('500x500')

        self.chat_area = ScrolledText(self.window, wrap=tk.WORD)
        self.chat_area.pack(padx=10, pady=10, fill='both', expand=True)

        tk.Label(self.window, text='Introduceti intrebarea: ')

        self.entry = tk.Entry(self.window)
        self.entry.pack(padx=10, pady=10, fill='both', expand=True)
        self.entry.bind('<Return>', lambda e: self.send_question())

        self.send_button = tk.Button(self.window, text='Trimite', command=self.send_question)
        self.send_button.pack(pady=10)

    def send_question(self, event=None):
        question = self.entry.get().strip()

        if not question:
            return

        answer = get_answer(question)

        self.chat_area.insert(tk.END, question)
        self.chat_area.insert(tk.END, answer)
        self.entry.delete(0, tk.END)
        self.chat_area.see(tk.END)

    def run(self):
        self.window.mainloop()