from tkinter import *
from  mydb import Database
from  tkinter import messagebox
from myapi import API

class NLPApp:
    def __init__(self):

        self.dbo=Database()
        self.apio=API()

        self.root=Tk()
        self.root.title("This is my first NLPapp")
        self.root.iconbitmap('Resources/favicon.ico')
        self.root.geometry('350x650')
        self.root.configure(bg='#aa9af1')
        self.login_gui()


        self.root.mainloop()



    def login_gui(self):

        self.clear()
        heading = Label(self.root,text='NLPApp',bg='#aa9af1',fg="black")
        heading.pack(pady=(30,30))
        heading.configure(font=('Algerian',24,'bold'))

        label1=Label(self.root,text='Enter Email')
        label1.pack(pady=(10,10))

        self.email_input=Entry(self.root,width=50)
        self.email_input.pack(pady=(10,10),ipady=3)

        label2=Label(self.root,text='Enter Password')
        label2.pack(pady=(10,10))

        self.password_input=Entry(self.root,width=50,show="*")
        self.password_input.pack(pady=(10,10),ipady=3)

        login_btn=Button(self.root,text='Login',height=1,command=self.perforn_login)
        login_btn.pack(pady=(10,10))

        label3=Label(self.root,text='Ragister Email')
        label3.pack(pady=(10,10))

        redirect_btn=Button(self.root,text='Not a member yet',command=self.register_gui)
        redirect_btn.pack(pady=(10,10))

    def register_gui(self):
        self.clear()

        heading = Label(self.root,text='NLPApp',bg='#aa9af1',fg="black")
        heading.pack(pady=(30,30))
        heading.configure(font=('Algerian',24,'bold'))

        label0 = Label(self.root, text='Enter Name')
        label0.pack(pady=(10, 10))

        self.name_input = Entry(self.root, width=50)
        self.name_input.pack(pady=(10, 10), ipady=3)

        label1=Label(self.root,text='Enter Email')
        label1.pack(pady=(10,10))

        self.email_input=Entry(self.root,width=50)
        self.email_input.pack(pady=(10,10),ipady=3)

        label2=Label(self.root,text='Enter Password')
        label2.pack(pady=(10,10))

        self.password_input=Entry(self.root,width=50,show="*")
        self.password_input.pack(pady=(10,10),ipady=3)



        register_btn =Button(self.root,text='Ragister now',height=1,command=self.perform_registration)
        register_btn .pack(pady=(10,10))

        label3 = Label(self.root, text='Already a member?')
        label3.pack(pady=(20, 10))

        login_btn=Button(self.root,text='Login',height=1,command=self.login_gui)
        login_btn.pack(pady=(10,10))






    def clear(self):
        for i in self.root.pack_slaves():
            i.destroy()
        # clear the existing  gui

    def perform_registration(self):
        name=self.name_input.get()
        email = self.email_input.get()
        password = self.password_input.get()
        responce=self.dbo.add_data(name,email,password)

        if responce:
            messagebox.showinfo("Success",'Registration success you can logging now')
            self.home_gui()
        else:
            messagebox.showerror("error",'email already exist')
        print(name)

    def perforn_login(self):
        email = self.email_input.get()
        password = self.password_input.get()

        responce=self.dbo.search(email,password)

        if responce:
            messagebox.showinfo("success",'Login successful')
            self.home_gui()
        else:
            messagebox.showerror('error','Incorrect Email/password')

    def home_gui(self):
        self.clear()

        heading = Label(self.root, text='NLPApp', bg='#aa9af1', fg="black")
        heading.pack(pady=(30, 30))
        heading.configure(font=('Algerian', 24, 'bold'))

        sentiment_btn = Button(self.root, text='Sentiment_Analysis', height=1,command=self.sentiment_gui)
        sentiment_btn.pack(pady=(20, 20))

        ner_btn = Button(self.root, text='Name Entity Recognition', height=1,command=self.named_entity_recognition_gui)
        ner_btn.pack(pady=(20, 20))

        emotion_btn = Button(self.root, text='logout', height=1,command=self.login_gui)
        emotion_btn.pack(pady=(20, 20))

    def sentiment_gui(self):

        self.clear()

        heading = Label(self.root, text='NLPApp', bg='#aa9af1', fg="black")
        heading.pack(pady=(30, 30))
        heading.configure(font=('Algerian', 24, 'bold'))

        heading2 = Label(self.root, text='SENTIMENT ANALYSIS', bg='#aa9af1', fg="black")
        heading2.pack(pady=(30, 30))
        heading2.configure(font=('Algerian', 20))

        label1 = Label(self.root, text='Enter the text')
        label1.pack(pady=(20, 10))

        self.sentiment_input=Entry(self.root,width=50)
        self.sentiment_input.pack(pady=(5,10),ipady=4)

        sentiment_btn=Button(self.root,text='Analysis Sentiment',command=self.do_sentiment_analysis)
        sentiment_btn.pack(pady=(10,10))

        self.sentiment_result=Label(self.root,text="",bg='#34495E',fg='white')
        self.sentiment_result.pack(pady=(10,10))
        self.sentiment_result.configure(font=('verdana',16))

        go_back=Button(self.root,text='Go back',command=self.home_gui)
        go_back.pack(pady=(10,10))

    def do_sentiment_analysis(self):
        text=self.sentiment_input.get()
        result=self.apio.sentiment_analysis(text)

        self.sentiment_result['text']=result

    def named_entity_recognition_gui(self):

        self.clear()

        heading = Label(self.root, text='NLPApp', bg='#aa9af1', fg="black")
        heading.pack(pady=(30, 30))
        heading.configure(font=('Algerian', 24, 'bold'))

        heading2 = Label(self.root, text='Named_Entity_Recognition', bg='#aa9af1', fg="black")
        heading2.pack(pady=(30, 30))
        heading2.configure(font=('Algerian', 20))

        label1 = Label(self.root, text='Enter the text')
        label1.pack(pady=(20, 10))

        self.named_entity_recognition_input=Entry(self.root,width=50)
        self.named_entity_recognition_input.pack(pady=(5,10),ipady=4)

        sentiment_btn=Button(self.root,text='Analysis Sentiment',command=self.do_named_entity_recognition_analysis)
        sentiment_btn.pack(pady=(10,10))

        self.sentiment_result=Label(self.root,text="",bg='#34495E',fg='white')
        self.sentiment_result.pack(pady=(10,10))
        self.sentiment_result.configure(font=('verdana',16))

        go_back=Button(self.root,text='Go back',command=self.home_gui)
        go_back.pack(pady=(10,10))

    def do_named_entity_recognition_analysis(self):
        text = self.named_entity_recognition_input.get()
        result = self.apio.named_entity_recognition(text)

        self.sentiment_result['text'] = result



















nlp=NLPApp()
