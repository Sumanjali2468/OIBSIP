from tkinter import *
import string
import random
import pyperclip


def generator():
    small_alphabets=string.ascii_lowercase
    capital_alphabets=string.ascii_uppercase
    numbers=string.digits
    special_characters=string.punctuation

    all=small_alphabets+capital_alphabets+numbers+special_characters

    password_length=int(length_box.get())

    if choice==1:
        passwordField.insert(0,random.sample(small_alphabets,password_length))

    if choice==2:
        passwordField.insert(0,random.sample(capital_alphabets,password_length))
    
    if choice==3:
        passwordField.insert(0,random.sample(all,password_length))


def copy():
    random_password=passwordField.get()
    pyperclip.copy(random_password)
   

root=Tk()
root.config(bg='gray20')
choice=IntVar()
Font=('arial',13,'bold')
passwordLabel=Label(root,text='PassWord Generator',font=('times new roman',20,'bold'),bg='gray20',fg='white')
passwordLabel.grid(pady=10)

weakradioButton=Radiobutton(root,text='weak',value=1,variable=choice,font=Font)
weakradioButton.grid(pady=5)

mediumradioButton=Radiobutton(root,text='medium',value=2,variable=choice,font=Font)
mediumradioButton.grid(pady=5)


StrongradioButton=Radiobutton(root,text='Strong',value=3,variable=choice,font=Font)
StrongradioButton.grid(pady=5)

lengthLabel=Label(root,text='PassWord Length',font=Font,bg='gray20',fg='white')
passwordLabel.grid(pady=10)

length_box=Spinbox(root,from_=5,to_=18,width=5,font=Font)
length_box.grid()

generateButton=Button(root,text='Generate',font=Font,command=generator)
generateButton.grid(pady=5)

passwordField=Entry(root,width=25,bd=2,font=Font)
passwordField.grid(pady=5)


copyButton=Button(root,text='Copy',font=Font,bg='white',fg='black')
copyButton.grid(pady=10)


root.mainloop()


