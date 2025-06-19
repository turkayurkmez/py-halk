import tkinter as tk
from tkinter import messagebox

class Calculator:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Basit bir hesap makinesi")
        self.window.geometry("500x500")
        self.window.configure(background="lightgray")

        self.result = ""
        self.calculation = ""
        self.create_ui()
    

    def create_ui(self):
        self.label_result = tk.Label(self.window,
                                    text="0",
                                    font=("Arial",20,"bold"),
                                    bg="darkgray",
                                    fg="white",
                                    height=3,
                                    anchor="e",
                                    padx=10 )
        
        self.label_result.pack(fill="x", padx=10, pady=10)

        button_frame = tk.Frame(self.window,bg="#cf3838")
        button_frame.pack(fill="both",expand=True,padx=10,pady=10)


        button_style ={
            "font":('Arial',16,"bold"),
            "height":2,
            "width":5,
            "bd":2,
            "relief":"raised"

        }
        button_clear = tk.Button(button_frame, command=self.clear, text="C",bg="green", fg="white",**button_style)

        button_clear.grid(row=0,column=0,columnspan=2,sticky="ew", padx=2, pady=2)
        buttons = [
            ("7",1,0), ("8",1,1), ("9",1,2), ("/",1,3),
            ("4",2,0), ("5",2,1), ("6",2,2), ("*",2,3),
            ("1",3,0), ("2",3,1), ("3",3,2), ("-",3,3),
            ("0",4,0), (".",4,1), ("=",4,2), ("+",4,3)
        ]

        for text,row, column in buttons:
            if text == "=":
                button = tk.Button(button_frame, command=self.calcuate, text=text, bg="brown", fg="white", **button_style)
            elif text in "+-*/":
                button = tk.Button(button_frame, command=lambda t=text: self.add_operation(t), text=text, bg="brown", fg="white", **button_style)
            else:
                button = tk.Button(button_frame, command=lambda t=text: self.add_number(t), text=text, bg="brown", fg="white", **button_style)
            
            button.grid(row=row, column=column,sticky="ew",padx=2,pady=2)



    def add_number(self,number):
        self.calculation += str(number)
        self.update_result()


    def update_result(self):
        if self.calculation:
            self.label_result.config(text=self.calculation)
        else:
            self.label_result.config(text="0")

    def add_operation(self, operator):
        if self.calculation and self.calculation[-1] not in "*-+/":
            self.calculation += operator
            self.update_result()

    def calcuate(self):
        try:
            if self.calculation:
                result = eval(self.calculation)
                self.result = str(result)
                self.calculation = self.result
                self.update_result()
        except:
            messagebox.showerror("HATA!","Geçersiz işlem!!")

    def clear(self):
           self.result = ""
           self.calculation = self.result
           self.update_result()



    def show(self):
        self.window.mainloop()
