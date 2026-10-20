import tkinter as tk
from DataBaseHandler import DataBaseHandler
import matplotlib.pyplot as plt
from tkinter import messagebox

class RegistrationForm(tk.Frame):

    def __init__(self, parent):
        super().__init__(parent, bg="#f8f9fa", padx=20, pady=20)

        # ===== Title  =====
        tk.Label(self, text="Student Registration Form", font=("Arial", 16, "bold"), bg="#f8f9fa").pack(pady=(0, 20))

        # ===== Name =====
        tk.Label(self, text="Full Name:", font=("Arial", 12), bg="#f8f9fa").pack(anchor="w")
        self.Entry_name = tk.Entry(self, width=40, font=("Arial", 11))
        self.Entry_name.pack(pady=(0, 10))

        # ===== Email =====
        tk.Label(self, text="Email:", font=("Arial", 12), bg="#f8f9fa").pack(anchor="w")
        self.Entry_email = tk.Entry(self, width=40, font=("Arial", 11))
        self.Entry_email.pack(pady=(0, 10))

        # ===== Gender =====
        tk.Label(self, text="Gender:", font=("Arial", 12), bg="#f8f9fa").pack(anchor="w")
        self.Entry_gender = tk.StringVar(value="male")

        gender_frame = tk.Frame(self, bg="#f8f9fa")
        gender_frame.pack(pady=(0, 15))
        tk.Radiobutton(gender_frame, text='Male', variable=self.Entry_gender, value='male', bg="#f8f9fa").pack(side="left", padx=10)
        tk.Radiobutton(gender_frame, text='Female', variable=self.Entry_gender, value='female', bg="#f8f9fa").pack(side="left", padx=10)

        # ===== submit =====
        button_frame = tk.Frame(self, bg="#f8f9fa")
        button_frame.pack(pady=15)

        self.Submit_button = tk.Button(button_frame, text='Submit', command=self.submit_form, width=15, bg="#007BFF", fg="white", font=("Arial", 11))
        self.Submit_button.pack(side="left", padx=10)

        self.Visualize_button = tk.Button(button_frame, text='Visualize Gender Distribution', command=self.visualize_gender_distribution, width=25, bg="#28A745", fg="white", font=("Arial", 11))
        self.Visualize_button.pack(side="left", padx=10)


    def submit_form(self):
        name = self.Entry_name.get()
        email = self.Entry_email.get()
        gender = self.Entry_gender.get()

        if name and email and gender:
            DataBaseHandler.insert_student(name, email, gender)
            messagebox.showinfo('Success', 'The data added successfully')
            self.Entry_name.delete(0, tk.END)
            self.Entry_email.delete(0, tk.END)
        else:
            messagebox.showwarning('Warning', 'Please enter all the fields')

    def visualize_gender_distribution(self):
        count_male = 0
        count_female = 0

        for student in DataBaseHandler.get_all_students():
            gender = str(student[3]).lower()
            if gender == 'male':
                count_male += 1
            elif gender == 'female':
                count_female += 1

        total = count_male + count_female

        if total == 0:
            messagebox.showinfo('Info', 'No student data available yet!')
            return

        # create a pie chart
        labels = ['Male', 'Female']
        colors = ['skyblue', 'lightpink']
        size = [count_male, count_female]

        plt.figure(figsize=(5, 5))
        plt.title('Gender Distribution Of Students')
        plt.pie(size, labels=labels, colors=colors, autopct='%1.1f%%')
        plt.axis('equal')
        plt.show()
