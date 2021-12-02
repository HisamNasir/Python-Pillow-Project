from tkinter import*
from PIL import Image,ImageTk
def btnClick(numbers):
        global operator
        operator=operator+str(numbers)
        text_Input=set(operator)
cal=Tk()
cal.geometry('433x670')
load=Image.open('C:\\Users\\Andromeda\\Desktop\\Project\\Image\\GG.jpg')
render=ImageTk.PhotoImage(load)
img = Label(cal,image=render)
img.place(x=0,y=0)

cal.title("Hisam & Abullah Project")
operator=""
text_input=StringVar()
cal.resizable(width=False,height=False)
#empty boc where output and input will show itself
txtDisplay=Entry(cal,font=('areal',27,'bold'),textvariable=text_input,bd=15,insertwidth=4,
                  bg='silver',fg='white',justify='right').grid(columnspan=4)
# Making buttons
but0=PhotoImage(file='C:\\Users\\Andromeda\\Desktop\\Project\\Image\\0.png')
but1=PhotoImage(file='C:\\Users\\Andromeda\\Desktop\\Project\\Image\\1.png')
but2=PhotoImage(file='C:\\Users\\Andromeda\\Desktop\\Project\\Image\\2.png')
but3=PhotoImage(file='C:\\Users\\Andromeda\\Desktop\\Project\\Image\\3.png')
but4=PhotoImage(file='C:\\Users\\Andromeda\\Desktop\\Project\\Image\\4.png')
but5=PhotoImage(file='C:\\Users\\Andromeda\\Desktop\\Project\\Image\\5.png')
but6=PhotoImage(file='C:\\Users\\Andromeda\\Desktop\\Project\\Image\\6.png')
but7=PhotoImage(file='C:\\Users\\Andromeda\\Desktop\\Project\\Image\\7.png')
but8=PhotoImage(file='C:\\Users\\Andromeda\\Desktop\\Project\\Image\\8.png')
but9=PhotoImage(file='C:\\Users\\Andromeda\\Desktop\\Project\\Image\\9.png')

button1=Button(cal,padx=16,image=but1,borderwidth=0,activebackground='black',bg='black',command=lambda:btnClick(1)).grid(row=1,column=0)
button2=Button(cal,padx=16,image=but2,borderwidth=0,activebackground='black',bg='black',command=lambda:btnClick(2)).grid(row=1,column=1)
button3=Button(cal,padx=16,image=but3,borderwidth=0,activebackground='black',bg='black',command=lambda:btnClick(3)).grid(row=1,column=2)
button4=Button(cal,padx=16,image=but4,borderwidth=0,activebackground='black',bg='black',command=lambda:btnClick(4)).grid(row=2,column=0)
button5=Button(cal,padx=16,image=but5,borderwidth=0,activebackground='black',bg='black',command=lambda:btnClick(5)).grid(row=2,column=1)
button6=Button(cal,padx=16,image=but6,borderwidth=0,activebackground='black',bg='black',command=lambda:btnClick(6)).grid(row=2,column=2)
button7=Button(cal,padx=16,image=but7,borderwidth=0,activebackground='black',bg='black',command=lambda:btnClick(7)).grid(row=3,column=0)
button8=Button(cal,padx=16,image=but8,borderwidth=0,activebackground='black',bg='black',command=lambda:btnClick(8)).grid(row=3,column=1)
button9=Button(cal,padx=16,image=but9,borderwidth=0,activebackground='black',bg='black',command=lambda:btnClick(9)).grid(row=3,column=2)
button0=Button(cal,padx=16,image=but0,borderwidth=0,activebackground='black',bg='black',command=lambda:btnClick(0)).grid(row=4,column=1)
Addbutton=Button(cal,padx=27,bd=10,bg='silver',fg='black',font=('arial',20,'bold'),
               text='+',command=lambda:btnClick("+")).grid(row=1,column=3)
Subbutton=Button(cal,padx=30,bd=10,bg='silver',fg='black',font=('arial',20,'bold'),
               text='-',command=lambda:btnClick("-")).grid(row=2,column=3)
Mulbutton=Button(cal,padx=27,bd=10,bg='silver',fg='black',font=('arial',20,'bold'),
               text='x',command=lambda:btnClick("*")).grid(row=3,column=3)
Divbutton=Button(cal,padx=30,bd=10,bg='silver',fg='black',font=('arial',20,'bold'),
               text='/',command=lambda:btnClick("/")).grid(row=4,column=3)
Equalbutton=Button(cal,padx=27,bd=10,bg='silver',fg='black',font=('arial',20,'bold'),
               text='=').grid(row=5,column=3)
Clearbutton=Button(cal,padx=13,bd=10,bg='silver',fg='black',font=('Times',20,'bold'),
               text='Clear').grid(row=6,column=3)
Introbutton=Button(cal,padx=20,bd=10,bg='midnightblue',fg='white',font=('Times',20,'bold'),
               text='Hisam').grid(row=7,column=3)
cal.mainloop()