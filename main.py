import tkinter as tk


class Main(tk.Frame):
    def __init__(self, root):
        super().__init__(root)
        self.init_main()


    def init_main(selfself):
        toolbar=tk.Frame(bg='#d7d8e0', bd=2)
        toolbar.pack(side=tk.TOP, fill=tk.X)


class Child(tk.Toplevel):
    def __init__(self):
        super().__init__(root)


if __name__ =='__main__':
    root = tk.Tk()
    app = Main(root)
    app.pack()
    root.title('HouseHold finance')
    root.geometry('650x450+300+200')
    root.resizable(False, False)

    root.mainloop()