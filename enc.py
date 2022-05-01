from tkinter import *
from PIL import ImageTk,Image
from tkinter import filedialog

def mains(pu=0,pr=0):
	def button1():
		a=root2.filename=filedialog.askopenfilename(initialdir='C:/',title='Mở file txt',filetypes=(("txt files","*.txt"),("all files",'*.*')))
		link.set(a)
	def gotodo():
		a=link.get()
		b=key.get()
		
		try:
			num=b.rfind('(')
			b=eval(b[num:])
			with open(a,'r',encoding='utf8') as f:
				z=f.read()
				x=mahoa(b,z)
				
				l=a=a[:a.find('.txt')]+"_mahoa.txt"
				link2.set(l)
				with open(l,'w+',encoding='utf8') as ff:
					frame=Frame(root2,height=25,width=500,bg='#FFFFFF')
					frame.place(x=150,y=170)
					ff.write(x)
					label1=Label(root2,text="SUCCESSFULL!!!",bg='#FFFFFF',bd=1,justify=CENTER,font=('Calibri (Body)',12,'italic')).place(x=150,y=170)
		except :
			frame=Frame(root2,height=25,width=500,bg='#FFFFFF')
			frame.place(x=150,y=170)
			label1=Label(root2,text="ERROR!!!",bg='#FFFFFF',bd=1,justify=CENTER,font=('Calibri (Body)',12,'italic')).place(x=150,y=170)
	def gotodo2():
		link.set('')	
		link2.set('')
		frame=Frame(root2,height=25,width=500,bg='#FFFFFF')
		frame.place(x=150,y=170)

	root2=Toplevel()
	root2.title("Mã Hóa RSA - Tang Ho Trung Nam")
	root2.geometry('750x350+650+200')
	root2.configure(bg='#FFFFFF')
	root2.resizable(0,0)
	root2.iconbitmap('Untitled-1.ico')
	link=StringVar()
	key=StringVar()
	link2=StringVar()
	key.set('(n,e)={}'.format(pu))
	box1=Entry(root2,textvariable=link,justify='left',relief=SUNKEN,font=('Calibri (Body)',11),width=55).place(x=150,y=20)
	box1=Entry(root2,textvariable=key,justify='left',relief=SUNKEN,font=('Calibri (Body)',11),width=55).place(x=150,y=70)
	box1=Entry(root2,textvariable=link2,justify='left',relief=SUNKEN,font=('Calibri (Body)',11),width=55).place(x=150,y=120)
	button_ok=Button(root2,text="Load file",width=10,height=1,bg='#f49b00',fg='#ffffff',bd=0,font=('Calibri (Body)',11,'bold italic'),command=button1)
	button_ok.place(x=20,y=20)
	button_ok.config(activebackground='#f49b00')
	button_ok.config(activeforeground='#ffffff')
	button_ok=Label(root2,text="Public key",width=10,height=1,bg='#ffffff',fg='black',bd=0,font=('Calibri (Body)',11,'bold italic'))
	button_ok.place(x=20,y=70)
	
	button_ok2=Button(root2,text="Ghi file",width=10,height=1,bg='#f49b00',fg='#ffffff',bd=0,font=('Calibri (Body)',11,'bold italic'),command=gotodo)
	button_ok2.place(x=20,y=120)
	button_ok2.config(activebackground='#f49b00')
	button_ok2.config(activeforeground='#ffffff')

	button_ok3=Button(root2,text="RESET",width=10,height=1,bg='#f49b00',fg='#ffffff',bd=0,font=('Calibri (Body)',11,'bold italic'),command=gotodo2)
	button_ok3.place(x=20,y=170)
	button_ok3.config(activebackground='#f49b00')
	button_ok3.config(activeforeground='#ffffff')
	
	root2.mainloop()


def mahoa(pukey,b):
	str_enc=str()
	b=[ord(x) for x in b] 
	for x in b: 
		c=(x**pukey[1])%pukey[0]
		str_enc+=chr(c)
	return str_enc
def main():
	mains()
if __name__=="__main__":

	main()
