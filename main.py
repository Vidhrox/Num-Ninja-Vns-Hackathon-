import tkinter as tk
from tkinter import ttk
from tkinter import filedialog,Label, Entry, Button
from PIL import Image, ImageTk
import matplotlib.pyplot as plt
from recentfiles import r1,r2,r3
import numpy as np
import requests

# drawing bar graph
class Function:

    @staticmethod
    def create(e, n, t):
        data_at = list(n.split(","))
        data = list(t.split(","))

        # Check if each value in data can be converted to float
        for value in data:
            if not value.strip():  # Check if the value is an empty string
                print("Error: Empty values are not allowed.")
                return

            try:
                float(value)
            except ValueError:
                print(f"Error: Could not convert string to float: '{value}'")
                return

        if len(data_at) != len(data):
            print("Note: Enter correct corresponding values!")

        # Continue with the rest of your code
        plt.pie(data, labels=data_at)
        plt.title("Portfolio")
        plt.savefig('portfolio.png')
        f = open("name.txt", "w")
        f.write(e)
        f.close()
        plt.show()
    @staticmethod
    def bar(e, n, x, y, t, res):
        folder_path = 'D:\\Downloads MSI GF63_2\\Test\\'
        file_name = t
        file_path = folder_path + file_name
        data_at = list(e.split(","))
        data = list(n.split(","))
        if len(data_at) != len(data):
            Function.bargui(res, "Note: Enter correct corresponding values!")

        plt.figure(figsize=(10, 6))

        # creating the bar plot
        plt.bar(data_at, [int(x) for x in data], color='blue', width=0.4)

        plt.xlabel(x)
        plt.ylabel(y)
        plt.title(t)
        plt.savefig(file_path)
        plt.show()

    @staticmethod
    def line(e, n, x, y, t, res):
        folder_path = 'D:\\Downloads MSI GF63_2\\Test\\'
        file_name = t
        file_path = folder_path + file_name
        data_at = list(e.split(","))
        data = list(n.split(","))
        if len(data_at) != len(data):
            Function.linegui(res, "Note: Enter correct corresponding values!")
        plt.plot([float(x) for x in data_at], [float(x) for x in data])
        plt.title(t)
        plt.xlabel(x)
        plt.ylabel(y)
        plt.savefig(file_path)
        plt.show()

    # drawing pie chart
    @staticmethod
    def pie(e, n, t, res):
        folder_path = 'D:\\Downloads MSI GF63_2\\Test\\'
        file_name = t
        file_path = folder_path + file_name
        data_at = list(e.split(","))
        data = list(n.split(","))
        if len(data_at) != len(data):
            Function.piegui(res, "Note: Enter correct corresponding values!")
        plt.pie(data, labels=data_at)
        plt.title(t)
        plt.savefig(file_path)
        plt.show()

    @staticmethod
    def calculate(income, spending):
        budget = 0
        savings = 0
        emerg = 0
        income = income.replace(',', '')
        spending = spending.replace(',', '')
        income = float(income)
        spending = float(spending)
        tax = 0
        if spending >= income:
            print(spending)
            print(income)
            screen_width = root.winfo_screenwidth()
            screen_height = root.winfo_screenheight()
            Gui.mm(f"{screen_width}x{screen_height}", "Spending exceeds income. Can't provide data")
        else:
            if income <= 250000:
                budget = income - spending
                savings = budget / 5
                emerg = budget / 10
                budget = budget - (savings + emerg)
                print(f"You have to save {savings}, keep {emerg} for emergency funds and invest {budget}")
            elif income >= 1000000:
                tax = 30 / 100 * float(income)
                income = income - tax
                budget = income - spending
                savings = budget / 5
                emerg = budget / 10
                budget = budget - (savings + emerg)
                print(f"You have to save {savings}, keep {emerg} for emergency funds and invest {budget}")
            else:
                tax = 20 / 100 * float(income)
                income = income - tax
                budget = income - spending
                savings = budget / 5
                emerg = budget / 10
                budget = budget - (savings + emerg)
                print(f"You have to save {savings}, keep {emerg} for emergency funds and invest {budget}")

        data = np.array([savings, emerg, budget, spending, tax])
        name = ["Savings Quota", "Emergency Funds", "Investment", "Spendings", "Taxes"]

        plt.pie(data, labels=[f"{name[i]}: {data[i]}" for i in range(len(name))])
        plt.title("Money Management")
        plt.show()

class PlaceholderEntry(tk.Entry):
    def __init__(self, master=None, placeholder="Enter text", color='grey', *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        self.placeholder = placeholder
        self.placeholder_color = color
        self.default_fg_color = self['fg']

        self.insert(0, self.placeholder)
        self.bind("<FocusIn>", self.on_focus_in)
        self.bind("<FocusOut>", self.on_focus_out)

    def on_focus_in(self, event):
        if self.get() == self.placeholder:
            self.delete(0, tk.END)
            self.config(fg=self.default_fg_color)

    def on_focus_out(self, event):
        if not self.get():
            self.insert(0, self.placeholder)
            self.config(fg=self.placeholder_color)

class Gui:
    @staticmethod
    def upload_image():
        image_path = filedialog.askopenfilename(filetypes=[("Image files", ".png;.jpg;.jpeg;.gif")])

        if image_path:
            pfp = Image.open(image_path)
            pfp_path = "pfp.jpg"
            pfp.save(pfp_path)

    @staticmethod
    def updpfgui(res, err):
        win = tk.Tk()
        win.geometry("900x450")
        win.title("Edit Portfolio")
        win.configure(bg='#1f1f23')

        label = tk.Label(win, fg='white', bg="#1f1f23", text="Edit Portfolio", font=("Arial", 30), borderwidth=0)
        label.pack()

        canvas_with_border = tk.Canvas(win, width=385, height=70, bd=0, relief=tk.SOLID, bg='#1f1f23')
        canvas_with_border.place(x=30, y=50)

        heading_label = tk.Label(win, text='Name:', font=("Helevatica", 16), fg='white', bg='#1f1f23')
        heading_label.place(x=40, y=60)

        entry1 = PlaceholderEntry(win, placeholder="Enter your name", width=30, font=("Arial", 16))
        entry1.focus_set()
        entry1.place(x=40, y=90)

        canvas_with_border1 = tk.Canvas(win, width=385, height=70, bd=0, relief=tk.SOLID, bg='#1f1f23')
        canvas_with_border1.place(x=460, y=50)

        heading_label = tk.Label(win, text='Profile Picture:', font=("Helevatica", 16), fg='white', bg='#1f1f23')
        heading_label.place(x=475, y=60)

        upload_button = tk.Button(win, width=50, text="Upload Image", command=res.upload_image)
        upload_button.place(x=475, y=90)

        heading_label = tk.Label(win, text='Investment Spread', font=("Helevatica", 20), fg='white', bg='#1f1f23')
        heading_label.place(x=319, y=138)

        canvas_with_border1 = tk.Canvas(win, width=700, height=100, bd=0, relief=tk.SOLID, bg='#1f1f23')
        canvas_with_border1.place(x=100, y=175)

        heading_label = tk.Label(win, text='Investment Names', font=("Helevatica", 16), fg='white', bg='#1f1f23')
        heading_label.place(x=110, y=200)

        entrys = PlaceholderEntry(win, placeholder="Eg:- Tesla,Bugatti,Porsche", width=30, font=("Arial", 14))
        entrys.place(x=110, y=240)

        heading_label = tk.Label(win, text='Amount Of Investment', font=("Helevatica", 16), fg='white', bg='#1f1f23')
        heading_label.place(x=460, y=200)

        amt = PlaceholderEntry(win, placeholder="Eg:-10000,20000,50000", width=30, font=("Arial", 14))
        amt.place(x=460, y=240)

        inp = tk.Button(win, text="Submit", width=35, height=1,
                        command=lambda: Function.create(entry1.get(), entrys.get(), amt.get()))
        inp.place(x=319, y=290)
        win.mainloop()
    @staticmethod
    def bargui(res, err):
        win = tk.Tk()
        win.configure(bg='black')
        win.geometry(res)
        win.title("Data Entry")
        label = tk.Label(win, pady=15, fg='black', bg='black', text="")
        label.pack()
        label = tk.Label(win, pady=15, fg='white', bg='black', text="Bar Graph", font=("Arial", 25))
        label.pack()
        label = tk.Label(win, text="Enter X axis values", font=30, fg='white', bg='black', pady=20)
        label.pack()

        entry = tk.Entry(win, width=50)
        entry.focus_set()
        entry.pack()

        label = tk.Label(win, text="Enter Y axis values", pady=20, font=22, fg='white', bg='black')
        label.pack()

        entrys = tk.Entry(win, width=50)
        entrys.pack()

        label = tk.Label(win, text="Enter X axis(Category of data's attribute)", pady=20, font=22, fg='white', bg='black')
        label.pack()

        x = tk.Entry(win, width=50)
        x.pack()

        label = tk.Label(win, text="Enter Y axis(Ex: number of hours taken)", pady=20, font=22, fg='white', bg='black')
        label.pack()

        y = tk.Entry(win, width=50)
        y.pack()

        label = tk.Label(win, text="Enter title for the graph", pady=20, font=22, fg='white', bg='black')
        label.pack()

        title = tk.Entry(win, width=50)
        title.pack()

        label = tk.Label(win, text="", pady=10, fg='black', bg='black')
        label.pack()

        inp = tk.Button(win, text="Submit", width=20,
                        command=lambda: Function.bar(entry.get(), entrys.get(), x.get(), y.get(), title.get(), res))
        inp.pack()
        label = tk.Label(win, text=err, pady=25, font=25, fg='white', bg='black')
        label.pack()
        win.mainloop()

    # gui for line graph
    @staticmethod
    def linegui(res, err):
        win = tk.Tk()
        win.configure(bg='black')
        win.geometry(res)
        win.title("Data Entry")
        label = tk.Label(win, pady=15, fg='black', bg='black', text="")
        label.pack()
        label = tk.Label(win, pady=15, fg='white', bg='black', text="Line Graph", font=("Arial", 25))
        label.pack()
        label = tk.Label(win, text="Enter X axis values", font=30, fg='white', bg='black', pady=20)
        label.pack()

        entry = tk.Entry(win, width=50)
        entry.focus_set()
        entry.pack()

        label = tk.Label(win, text="Enter Y axis values", pady=20, font=22, fg='white', bg='black')
        label.pack()

        entrys = tk.Entry(win, width=50)
        entrys.pack()

        label = tk.Label(win, text="Enter X axis(Category of data's attribute)", pady=20, font=22, fg='white', bg='black')
        label.pack()

        x = tk.Entry(win, width=50)
        x.pack()

        label = tk.Label(win, text="Enter Y axis(Ex: number of hours taken)", pady=20, font=22, fg='white', bg='black')
        label.pack()

        y = tk.Entry(win, width=50)
        y.pack()

        label = tk.Label(win, text="Enter title for the graph", pady=20, font=22, fg='white', bg='black')
        label.pack()

        title = tk.Entry(win, width=50)
        title.pack()

        label = tk.Label(win, text="", pady=10, fg='black', bg='black')
        label.pack()

        inp = tk.Button(win, text="Submit", width=20,
                        command=lambda: Function.line(entry.get(), entrys.get(), x.get(), y.get(), title.get(), res))
        inp.pack()
        label = tk.Label(win, text=err, pady=25, font=25, fg='white', bg='black')
        label.pack()
        win.mainloop()

    @staticmethod
    def calcgui(res, err):
        window = tk.Tk()
        window.title("Finance Calculator")
        window.configure(bg='#1E1E1E')  # Set background color
        screen_width = window.winfo_screenwidth()
        screen_height = window.winfo_screenheight()
        total = f"{screen_width}x{screen_height}"
        window.geometry(total)
        # Create and place widgets for Simple and Compound Interest
        Label(window, text="Simple and Compound Interest Calculator", font=("Helvetica", 16), fg='white',
              bg='#1E1E1E').pack(pady=10)

        Label(window, text="Principal Amount:", font=("Helvetica", 12), fg='white', bg='#1E1E1E').pack(pady=5)
        entry_principal = Entry(window, font=("Helvetica", 12))
        entry_principal.pack(pady=5)

        Label(window, text="Annual Interest Rate (%):", font=("Helvetica", 12), fg='white', bg='#1E1E1E').pack(pady=5)
        entry_rate = Entry(window, font=("Helvetica", 12))
        entry_rate.pack(pady=5)

        Label(window, text="Time (years):", font=("Helvetica", 12), fg='white', bg='#1E1E1E').pack(pady=5)
        entry_time = Entry(window, font=("Helvetica", 12))
        entry_time.pack(pady=5)

        def on_calculate():
            principal = float(entry_principal.get())
            rate = float(entry_rate.get()) / 100  # Convert percentage to decimal
            time = float(entry_time.get())

        calculate_button = Button(window, text="Calculate Simple and Compound Interest", font=("Helvetica", 12),
                                  command=on_calculate)
        calculate_button.pack(pady=10)

        def calculate_simple_interest(principal, rate, time):
            return principal * (1 + rate * time)

        def calculate_compound_interest(principal, rate, time):
            return principal * (1 + rate) ** time

            simple_interest = calculate_simple_interest(principal, rate, time)
            compound_interest = calculate_compound_interest(principal, rate, time)

            result_label.config(
                text=f"Simple Interest: {simple_interest:.2f}\nCompound Interest: {compound_interest:.2f}")

        def convert():
            fro = from_cur.get().upper()
            to = to_cur.get().upper()
            sum = float(amt.get())
            response = requests.get(
                f"https://api.frankfurter.app/latest?amount={sum}&from={fro}&to={to}")
            result.config(text=f"{sum} {fro} is {response.json()['rates'][to]} {to}")

        result_label = Label(window, text="", font=("Helvetica", 12), fg='white', bg='#1E1E1E')
        result_label.pack(pady=5)

        # ui for currency exchange

        Label(window, text="Currency Converter", font=("Helvetica", 16), fg='white', bg='#1E1E1E').pack(pady=10)

        Label(window, text="Amount:", font=("Helvetica", 12), fg='white', bg='#1E1E1E').pack(pady=5)
        amt = Entry(window, font=("Helvetica", 12))
        amt.pack(pady=5)

        Label(window, text="From Currency:", font=("Helvetica", 12), fg='white', bg='#1E1E1E').pack(pady=5)
        from_cur = Entry(window, font=("Helvetica", 12))
        from_cur.pack(pady=5)

        Label(window, text="To Currency:", font=("Helvetica", 12), fg='white', bg='#1E1E1E').pack(pady=5)
        to_cur = Entry(window, font=("Helvetica", 12))
        to_cur.pack(pady=5)

        convert_button = Button(window, text="Convert Currency", font=("Helvetica", 12), command=convert)
        convert_button.pack(pady=10)

        result = Label(window, text="", font=("Helvetica", 12), fg='white', bg='#1E1E1E')
        result.pack(pady=5)

    # gui for pie chart
    @staticmethod
    def piegui(res, err):
        win = tk.Tk()
        win.configure(bg='black')
        win.geometry(res)
        win.title("Data Entry")
        label = tk.Label(win, pady=15, fg='black', bg='black', text="")
        label.pack()
        label = tk.Label(win, pady=15, fg='white', bg='black', text="Pie Chart", font=("Arial", 25))
        label.pack()
        label = tk.Label(win, text="Enter data's attribute", font=30, fg='white', bg='black', pady=20)
        label.pack()

        entry = tk.Entry(win, width=50)
        entry.focus_set()
        entry.pack()

        label = tk.Label(win, text="Enter data separated by commas(%)", pady=20, font=22, fg='white', bg='black')
        label.pack()

        entrys = tk.Entry(win, width=50)
        entrys.pack()

        label = tk.Label(win, text="Enter title for the graph", pady=20, font=22, fg='white', bg='black')
        label.pack()

        title = tk.Entry(win, width=50)
        title.pack()

        label = tk.Label(win, text="", pady=4, fg='black', bg='black')
        label.pack()

        inp = tk.Button(win, text="Submit", width=20,
                        command=lambda: Function.pie(entry.get(), entrys.get(), title.get(), res))
        inp.pack()
        label = tk.Label(win, text=err, pady=25, font=25, fg='white', bg='black')
        label.pack()
        win.mainloop()

    @staticmethod
    def mm(res, err):
        win = tk.Tk()
        win.configure(bg='black')
        win.geometry(res)
        win.title("Data Entry")
        label = tk.Label(win, pady=15, fg='black', bg='black', text="")
        label.pack()
        label = tk.Label(win, pady=15, fg='white', bg='black', text="Money Management", font=("Arial", 25))
        label.pack()
        label = tk.Label(win, text="Income per year", font=30, fg='white', bg='black', pady=20)
        label.pack()

        entry = tk.Entry(win, width=50)
        entry.focus_set()
        entry.pack()

        label = tk.Label(win, text="Spending per year", pady=20, font=22, fg='white', bg='black')
        label.pack()

        entrys = tk.Entry(win, width=50)
        entrys.pack()



        label = tk.Label(win, text="", pady=10, fg='black', bg='black')
        label.pack()

        inp = tk.Button(win, text="Submit", width=20,
                        command=lambda: Function.calculate(entry.get(), entrys.get()))
        inp.pack()
        label = tk.Label(win, text=err, pady=25, font=25, fg='white', bg='black')
        label.pack()
        win.mainloop()


class NumNinjaWelcomeScreen:
    @staticmethod
    def button_click(no, res):
        if no == 1:
            Gui.bargui(res, "")
        elif no == 2:
            Gui.mm(res,"")
        elif no == 3:
            Gui.linegui(res, "")
        elif no == 4:
            Gui.piegui(res, "")
        elif no == 5:
            r1.show()
        elif no == 6:
            r2.show()
        elif no == 7:
            r3.show()
        elif no == 8:
            Gui.updpfgui(res, "")
        elif no == 9:
            Gui.calcgui(res,"")
        else:
            pass

    def __init__(self, root, pfp_path):
        self.root = root
        self.root.title("NumNinja Welcome Screen")

        self.root = root
        self.pfp_path = pfp_path

        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()

        # Calculate sizes as percentages of the screen size
        left_container_width = int(screen_width * 0.25)
        right_container_width = screen_width - left_container_width
        left_content_width = left_container_width
        total = f"{screen_width}x{screen_height}"

        # Left background
        self.left_container = tk.Frame(root, width=left_container_width, height=screen_height, background='#2a2c30')
        self.left_container.grid(row=0, column=0, sticky="ns")

        # Left Content
        self.left_content = tk.Frame(root, width=left_content_width, height=screen_height, background='#2a2c30')
        self.left_content.grid(row=0, column=0, sticky="ns")

        # Right side
        self.right_container = tk.Frame(root, width=right_container_width, height=screen_height, background='#1f1f23')
        self.right_container.grid(row=0, column=1, sticky="nsew")

        # Create a Notebook for the right side
        self.notebook = ttk.Notebook(self.right_container, width=right_container_width, height=screen_height)
        self.notebook.grid(row=0, column=0, sticky="nsew")

        # Create tabs for the Notebook
        self.tab1 = tk.Frame(self.notebook, background='#1f1f23')
        self.tab3 = tk.Frame(self.notebook, background='#1f1f23')

        self.notebook.add(self.tab1, text="")
        self.notebook.hide(self.tab1)
        self.notebook.add(self.tab3, text="")
        self.notebook.hide(self.tab3)

        #headding
        heading_label = tk.Label(self.left_content, text='NumNinja', font=("Bell MT", 52, "bold"), fg='white',
                                 bg='#2a2c30')
        heading_label.place(x=35, y=50)
        # Button 1
        self.button_statistics = tk.Button(self.left_content, text='Statistics', font=("Helvetica", 36), fg='white', bg='#2a2c30', anchor="w", borderwidth=0, relief=tk.GROOVE, activebackground='#4e4f52', command=self.show_tab1)
        self.button_statistics.place(x=70, y=320)
        #button 2
        self.button_finance = tk.Button(self.left_content, text='Finance', font=("Helvetica", 36), fg='white',bg='#2a2c30', anchor="w", borderwidth=0, relief=tk.GROOVE, activebackground='#4e4f52', command=self.show_tab3)
        self.button_finance.place(x=70, y=420)

        # Images in tab1 (replace with your image paths)
        img1 = Image.open("bargraph.jpg")
        img1 = img1.resize((275, 275), Image.BICUBIC)
        img1 = ImageTk.PhotoImage(img1)
        button_img1 = tk.Button(self.tab1, image=img1, command=lambda: self.button_click(1, total), borderwidth=0)
        button_img1.image = img1
        button_img1.place(x=120, y=45)

        img2 = Image.open("linegraph.jpg")
        img2 = img2.resize((275, 275), Image.BICUBIC)
        img2 = ImageTk.PhotoImage(img2)
        button_img2 = tk.Button(self.tab1, image=img2, command=lambda: self.button_click(3, total), borderwidth=0)
        button_img2.image = img2
        button_img2.place(x=440, y=45)

        img3 = Image.open("piechart.jpg")
        img3 = img3.resize((275, 275), Image.BICUBIC)
        img3 = ImageTk.PhotoImage(img3)
        button_img3 = tk.Button(self.tab1, image=img3, command=lambda: self.button_click(4, total), borderwidth=0)
        button_img3.image = img3
        button_img3.place(x=760, y=45)

        heading_label = tk.Label(self.tab1, text='Recents:', font=("Helevatica", 36, "bold"), fg='white',bg='#1f1f23')
        heading_label.place(x=120, y=380)

        img4 = Image.open(r1)
        img4 = img4.resize((275, 275), Image.BICUBIC)
        img4 = ImageTk.PhotoImage(img4)
        button_img4 = tk.Button(self.tab1, image=img4, command=lambda: self.button_click(5, total), borderwidth=0)
        button_img4.image = img4
        button_img4.place(x=120, y=450)

        img5 = Image.open(r2)
        img5 = img5.resize((275, 275), Image.BICUBIC)
        img5 = ImageTk.PhotoImage(img5)
        button_img5 = tk.Button(self.tab1, image=img5, command=lambda: self.button_click(6, total), borderwidth=0)
        button_img5.image = img5
        button_img5.place(x=440, y=450)

        img6 = Image.open(r3)
        img6 = img6.resize((275, 275), Image.BICUBIC)
        img6 = ImageTk.PhotoImage(img6)
        button_img6 = tk.Button(self.tab1, image=img6, command=lambda: self.button_click(7, total), borderwidth=0)
        button_img6.image = img6
        button_img6.place(x=760, y=450)

        # Configure grid weights
        self.root.columnconfigure(0, weight=1)
        self.root.columnconfigure(1, weight=3)

        canvas_with_border = tk.Canvas(self.tab3, width=400, height=700, bd=0, relief=tk.SOLID, bg='#1f1f23')
        canvas_with_border.place(x=20, y=32)

        canvas_label1 = tk.Label(self.tab3, text='User Portfolio', font=("Helvetica", 22), fg='white',bg='#2a2c30', anchor="w", borderwidth=0, relief=tk.GROOVE,activebackground='#4e4f52')
        canvas_label1.place(x=123, y=50)

        if self.pfp_path:

            img10 = Image.open(self.pfp_path)
            img10 = img10.resize((180, 180), Image.BICUBIC)
            img10 = ImageTk.PhotoImage(img10)
            label_img10 = tk.Label(self.tab3, image=img10)
            label_img10.image = img10
            label_img10.place(x=123, y=100)

        canvas_label2 = tk.Label(self.tab3, text='Name: Daksh', font=("Helvetica BOLD", 20), fg='white',bg='#1f1f23', anchor="w", borderwidth=0, relief=tk.GROOVE,activebackground='#1f1f23')
        canvas_label2.place(x=120,y=332)

        canvas_label3 = tk.Label(self.tab3, text='Investment Spread', font=("Helvetica", 20), fg='white', bg='#1f1f23',anchor="w", borderwidth=0, relief=tk.GROOVE, activebackground='#1f1f23')
        canvas_label3.place(x=97, y=383)

        img11 = Image.open("portfolio.png")
        img11 = img11.resize((300,300), Image.BICUBIC)
        img11 = ImageTk.PhotoImage(img11)
        button_img11 = tk.Button(self.tab3, image=img11, borderwidth=0)
        button_img11.image = img11
        button_img11.place(x=70, y=420)

        img7 = Image.open("moneymanagement.png")
        img7 = img7.resize((450, 130), Image.BICUBIC)
        img7 = ImageTk.PhotoImage(img7)
        button_img7 = tk.Button(self.tab3, image=img7, command=lambda: self.button_click(2, total), borderwidth=0)
        button_img7.image = img7
        button_img7.place(x=560, y=120)

        img9 = Image.open("updpf.png")
        img9 = img9.resize((450, 130), Image.BICUBIC)
        img9 = ImageTk.PhotoImage(img9)
        button_img9 = tk.Button(self.tab3, image=img9, command=lambda: self.button_click(8, total), borderwidth=0)
        button_img9.image = img9
        button_img9.place(x=560, y=300)

        img13 = Image.open("fc.png")
        img13 = img13.resize((450, 130), Image.BICUBIC)
        img13 = ImageTk.PhotoImage(img13)
        button_img13 = tk.Button(self.tab3, image=img13, command=lambda: self.button_click(9, total), borderwidth=0)
        button_img13.image = img13
        button_img13.place(x=560, y=500)

        #grid wieght
        self.root.columnconfigure(0, weight=1)
        self.root.columnconfigure(1, weight=3)

    def show_tab1(self):
        self.notebook.select(self.tab1)
        self.button_statistics.config(bg='#4e4f52')
        self.button_finance.config(bg='#2a2c30')
    def show_tab3(self):
        self.notebook.select(self.tab3)
        self.button_statistics.config(bg='#2a2c30')
        self.button_finance.config(bg='#4e4f52')


if __name__ == "__main__":
    root = tk.Tk()
    pfp_path = "pfp.jpg"
    app = NumNinjaWelcomeScreen(root, pfp_path)
    root.geometry(f"{root.winfo_screenwidth()}x{root.winfo_screenheight()}")
    root.mainloop()
