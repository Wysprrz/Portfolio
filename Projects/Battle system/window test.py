import tkinter as tk
'''
root = tk.Tk()
root.title("My first GUI")
root.geometry("500x500")
label = tk.Label(root, text="Hello World!", font=('Arial', 18))
label.pack(padx=20, pady=20)

textbox = tk.Text(root, height=3,  font=('Arial', 16))
textbox.pack(padx=10, pady=10)

buttonframe = tk.Frame(root)
buttonframe.columnconfigure(0, weight=1)
buttonframe.columnconfigure(1, weight=1)
buttonframe.columnconfigure(2, weight=1)

btn1 = tk.Button(buttonframe, text="1", font=('Arial', 18))
btn1.grid(row=0, column=0, sticky=tk.W+tk.E) #where the buttons start

btn2 = tk.Button(buttonframe, text="2", font=('Arial', 18))
btn2.grid(row=0, column=1, sticky=tk.W+tk.E) #where the buttons start

btn3 = tk.Button(buttonframe, text="3", font=('Arial', 18))
btn3.grid(row=0, column=2, sticky=tk.W+tk.E) #where the buttons start

btn4 = tk.Button(buttonframe, text="4", font=('Arial', 18))
btn4.grid(row=1, column=0, sticky=tk.W+tk.E) #where the buttons start

btn5 = tk.Button(buttonframe, text="5", font=('Arial', 18))
btn5.grid(row=1, column=1, sticky=tk.W+tk.E) #where the buttons start

btn6 = tk.Button(buttonframe, text="6", font=('Arial', 18))
btn6.grid(row=1, column=2, sticky=tk.W+tk.E) #where the buttons start

buttonframe.pack(fill='x')

anotherbtn = tk.Button(root, text="Test")
anotherbtn.place(x=200, y=200, height=100, width=100) #place exactly
root.mainloop()
'''

#functionality
class MyGui:
    def __init__(self):

        self.root = tk.Tk()
        self.label = tk.Label(self.root, text="Your message", font=('Arial', 18))
        self.label.pack(padx=10, pady=10)
        self.textbox = tk.Text(self.root, height=5, font=('Arial', 16))
        self.textbox.pack(padx=10, pady=10)

        self.check_state = tk.IntVar()
        self.check = tk.Checkbutton(self.root, text="Show Messagebox", font=('Arial', 16), variable=self.check_state)
        self.check.pack(padx=10, pady=10)

        self.button = tk.Button(self.root, text="Show Message", font=('Arial', 18), command=self.show_message)
        self.button.pack(padx=10, pady=10)

        self.root.mainloop()

    def show_message(self):
        print("Hello World")

MyGui()