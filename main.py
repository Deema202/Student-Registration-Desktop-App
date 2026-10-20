import tkinter as tk
from RegistrationForm import RegistrationForm

# create a main class

class MainApplication(tk.Tk):

    def __init__(self):
        super().__init__()
        self.geometry("500x600")
        self.title("Student Registration")
        self.create_widgets()

    def create_widgets(self):
        self.label = tk.Label(self, text="Student Registration", font=("Arial", 16, "bold"))
        self.label.pack(pady=10)

        self.registration_form = RegistrationForm(self)
        self.registration_form.pack(pady=10)

# execute application

if __name__ == "__main__":
    app = MainApplication()
    app.mainloop()
