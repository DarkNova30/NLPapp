from tkinter import *
from mydb import DataBase
from tkinter import messagebox
from myapi import API

# from tkmacosx import Button


class NLPapp:

    def __init__(self):

        # creating db object
        self.emo_result = None
        self.emo_input = None
        self.sent_input = None
        self.dbo = DataBase()
        # api obj
        self.apio = API()
        self.pw_input = None
        self.name_input = None
        self.email_input = None
        self.root = Tk()  # object of Tk class
        self.root.title("NLP app")

        self.clr = "#1f0447"
        self.root.iconbitmap('venv/favicon-3.ico')
        self.root.geometry("355x610")  # size of opening window 350x600
        self.root.configure(bg=self.clr)
        # original colour  #34495f

        self.login_gui()
        self.root.mainloop()  # Loads and holds the GUI

    def login_gui(self):
        self.email_input = "  "
        self.pw_input = "  "
        self.clear()
        self.root.configure(bg=self.clr)
        heading = Label(self.root, text="NLP App", bg=self.clr, fg="white")
        heading.pack(pady=(30, 30))
        heading.configure(font=('verdana', 24, 'bold'))

        label1 = Label(self.root, text="Enter Email", bg=self.clr)  # just creates a label
        label1.pack(pady=(10, 10))  # label1.configure(font=("ariel", 13))  # to display
        self.email_input = Entry(self.root, width=30, border=1)  # entry class for user input
        self.email_input.pack(pady=(5, 10), ipady=4)

        label2 = Label(self.root, text="Enter Password", bg=self.clr)  # just creates a label
        label2.pack(pady=(10, 10))  # to display
        # label2.configure(font=("ariel", 13)
        self.pw_input = Entry(self.root, width=25, border=1, show="*")  # entry class for user input
        self.pw_input.pack(pady=(5, 10), ipady=2.5)

        login_button = Button(self.root, text="Login", width=16, height=1, borderwidth=2, bg="#344001",
                              command=self.perform_login)
        login_button.pack(pady=(15, 15), ipady=1)

        label3 = Label(self.root, text="Not a member?", width=10, bg=self.clr)
        label3.pack(pady=(28, 3))
        reg_button = Button(self.root, text="Register Now", background=self.clr, borderwidth=2,
                            command=self.register_gui)
        reg_button.pack(ipady=1)

    def register_gui(self):  # REGISTRATION MODULE
        # first we clear the existing gui
        self.clear()
        self.root.configure(bg="#34695f")

        heading = Label(self.root, text="NLP App\nRegistration Page", bg="#34695f", fg="white")
        heading.pack(pady=(30, 35))
        heading.configure(font=('verdana', 24, 'bold'))

        label0 = Label(self.root, text="Enter Name", bg="#34695f")  # just creates a label
        label0.pack(pady=(10, 10))  # label1.configure(font=("ariel", 13))  # to display
        self.name_input = Entry(self.root, width=30, border=1)  # entry class for user input
        self.name_input.pack(pady=(5, 10), ipady=4)

        label1 = Label(self.root, text="Enter Email", bg="#34695f")  # just creates a label
        label1.pack(pady=(10, 10))  # label1.configure(font=("ariel", 13))  # to display
        self.email_input = Entry(self.root, width=30, border=1)  # entry class for user input
        self.email_input.pack(pady=(5, 10), ipady=4)

        label2 = Label(self.root, text="Enter Password", bg="#34695f")  # just creates a label
        label2.pack(pady=(10, 10))  # to display
        # label2.configure(font=("ariel", 13)
        self.pw_input = Entry(self.root, width=25, border=1, show="*")  # entry class for user input
        self.pw_input.pack(pady=(5, 10), ipady=2.5)

        reg_button = Button(self.root, text="Register", width=16, foreground="#344001", command=self.perform_reg)
        reg_button.pack(pady=(15, 15), ipady=1.5)

        label3 = Label(self.root, text="Already a Member?", width=15, bg="#34695f")
        label3.pack(pady=(28, 3))

        redirect_button = Button(self.root, text="Login Now", background="#34695f", command=self.login_gui)
        redirect_button.pack(pady=(10, 10), ipady=1)

    def clear(self):
        for i in self.root.pack_slaves():
            i.destroy()

    def perform_reg(self):
        # fetch data from gui
        name = self.name_input.get()  # get will fetch name from the name_input object
        mail = self.email_input.get()
        pw = self.pw_input.get()

        response = self.dbo.add_data(name, mail, pw)
        if response == 1:
            messagebox.showinfo('success', 'Registration successful, you can login now')
            # print("Registration successful")
        else:
            messagebox.showerror('Error', 'Email already exists')
            # print("Email already exists")

    def perform_login(self):

        mail = self.email_input.get()
        pw = self.pw_input.get()
        print(mail, pw)
        response = self.dbo.search(mail, pw)
        if response:
            messagebox.showinfo('success', "Login successful")
            self.home_gui()
        else:
            messagebox.showerror('error', "password or email wrong")

    def home_gui(self):
        self.clear()

        self.root.configure(bg="#041647")

        heading = Label(self.root, text="NLP App\nHome Page", bg="#041647")
        heading.pack(pady=(30, 40))
        heading.configure(font=('verdana', 24, 'bold'))

        # sentiment
        sentiment_button = Button(self.root, text="Sentiment Analysis", bg="red", activebackground="blue", width=24,
                                  height=3, border=2, command=self.sentiment_gui)
        sentiment_button.pack(pady=(20, 15), ipady=2)
        sentiment_button.configure(font=('verdana', 16, 'bold'))

        # Ner
        # ner_button = Button(self.root, text="Named Entity Recognition", width=24, height=3, border=2,
        #                     command=self.perform_reg)
        # ner_button.pack(pady=(20, 15), ipady=2)
        # ner_button.configure(font=('verdana', 16, 'bold'))
        # emotion
        emotion_button = Button(self.root, text="Emotion Prediction", width=24, height=3, border=2,
                                command=self.emo_gui)
        emotion_button.pack(pady=(20, 15), ipady=2)
        emotion_button.configure(font=('verdana', 16, 'bold'))
        # go back
        go_back = Label(self.root, text="Go back to Login Page", width=15, bg="#041647")
        go_back.pack(pady=(35, 5))
        # heading.configure(font=('verdana', 12, 'bold'))
        goback_btn = Button(self.root, text="Login Page", command=self.login_gui)
        goback_btn.pack(pady=(10, 10), ipady=1.5)

    # sentiment portal
    def sentiment_gui(self):
        self.clear()

        heading = Label(self.root, text="NLP App\n", bg="#041647")
        heading.pack(pady=(30, 10))
        heading.configure(font=('verdana', 24, 'bold'))

        heading2 = Label(self.root, text=' Sentiment Analysis +/- ', bg='#1740b0', fg='white', border=3, borderwidth=3,
                         relief='groove')
        heading2.pack(pady=(10, 10), ipady=2)
        heading2.configure(font=('verdana', 20))

        label1 = Label(self.root, text="Enter the text to analyse", bg="#041647")
        label1.pack(pady=(20, 5))

        self.sent_input = Entry(self.root, width=35)
        self.sent_input.pack(pady=(5, 10), ipady=12)

        sent_button = Button(self.root, text="✨Analyse Sentiment ✨", width=18, borderwidth=3, command=self.do_sent_analysis)
        sent_button.pack(pady=(10, 10), ipady=4)
        sent_button.configure(font=('verdana', 14), fg="black", highlightbackground="#1740b0")

        self.sent_result = Label(self.root, text="", bg="#041647", fg="white")
        self.sent_result.pack(pady=(10, 10))
        self.sent_result.configure(font=('verdana', 16))

        goback_button = Button(self.root, text="Go back", borderwidth=2, command=self.home_gui)
        goback_button.pack(pady=(30, 10), ipady=3)

    def emo_gui(self):
        self.clear()

        heading = Label(self.root, text="NLP App\n", bg="#041647")
        heading.pack(pady=(30, 10))
        heading.configure(font=('verdana', 24, 'bold'))

        heading2 = Label(self.root, text=' Emotion analysis :) ', bg="#6417b0", fg='white', border=3, borderwidth=3,
                         relief='groove')
        heading2.pack(pady=(10, 14), ipady=2)
        heading2.configure(font=('verdana', 20))

        label1 = Label(self.root, text="Enter the text to analyse\n\n Anger😡 | Disgust🥴 | Fear😰 \n Joy🤩 | Sadness😔 | Surprise😯", bg="#041647")
        label1.pack(pady=(20, 5))
        label1.configure(font=8)

        self.emo_input = Entry(self.root, width=35)
        self.emo_input.pack(pady=(5, 10), ipady=12)

        emo_button = Button(self.root, text="✨Analyse Emotion ✨", width=18, borderwidth=3, command=self.do_emo_analysis)
        emo_button.pack(pady=(10, 10), ipady=4)
        emo_button.configure(font=('verdana', 14), fg="black", highlightbackground="#6417b0")

        self.emo_result = Label(self.root, text="", bg="#041647", fg="white")
        self.emo_result.pack(pady=(10, 10))
        self.emo_result.configure(font=('verdana', 16))

        goback_button = Button(self.root, text="Go back", borderwidth=2, command=self.home_gui)
        goback_button.pack(pady=(30, 10), ipady=3)

    def do_sent_analysis(self):
        text = self.sent_input.get()
        result = self.apio.sentiment_analysis(text)

        self.sent_result["text"] = result

    def do_emo_analysis(self):
        # self.clear()
        emotext = self.emo_input.get()
        emo_response = self.apio.emotion_analysis(emotext)
        self.emo_result["text"] = emo_response

nlp = NLPapp()
