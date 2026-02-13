import tkinter as tk 

class Calculator:

    def __init__(self, root):
        self.root = root
        self.root.title("Calculator")
        self.root.geometry("300x350")

        self.expression = ""
        self.input_text = tk.StringVar()

        self.create_display()
        self.create_Buttons()

    def create_display(self):
        frame = tk.Frame(self.root)
        frame.pack()

        entry = tk.Entry(frame, textvariable=self.input_text,
                         font=("Arial", 18), justify="right")
        entry.pack(fill="both", ipadx=8, ipady=15)

    def create_Buttons(self):
        frame = tk.Frame(self.root)
        frame.pack()

        buttons = [
            ('7',1,0),('8',1,1),('9',1,2),('/',1,3),
            ('4',2,0),('5',2,1),('6',2,2),('*',2,3),
            ('1',3,0),('2',3,1),('3',3,2),('-',3,3),
            ('0',4,0),('.',4,1),('=',4,2),('+',4,3)
        ]
        
        for text,row,col in buttons:
            if text == "=":
                btn = tk.Button(frame, text=text, width=5, height=2,
                                command=self.maths)
            else:
                btn = tk.Button(frame, text=text, width=5, height=2,
                                command=lambda t=text: self.press(t))
            btn.grid(row=row, column=col)

        tk.Button(frame, text="C", width=22, height=2,
                  command=self.clear).grid(row=5, column=0, columnspan=4)

    def press(self, value):
        self.expression += str(value)
        self.input_text.set(self.expression)

    def maths(self):
        try:
            result = str(eval(self.expression))
            self.expression = result
            self.input_text.set(result)
        except:
            self.input_text.set("Error")
            self.expression = ""

    def clear(self):
        self.expression = ""
        self.input_text.set("")


root = tk.Tk()
Calculator(root)
root.mainloop()