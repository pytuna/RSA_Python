try:
	from tkinter import *
	import random
	from tkinter import ttk
	import todo as test
	import enc
	import dec
	root=Tk()
	root.title("RSA - Tang Ho Trung Nam")
	root.geometry('550x700+20+10')
	root.configure(bg='#FFFFFF')
	root.resizable(0,0)
	root.iconbitmap('Untitled-1.ico')

	def randoms():
		fr=Frame(root,width=550,height=100,bg='#FFFFFF')
		fr.place(x=0,y=200)
		primes = test.primes2(3,1000)
		p = random.choice(primes)
		q = random.choice(primes)
		key.set(p)
		key2.set(q)
		pn=(p-1)*(q-1)
		n=p*q
		lst=test.primes(3,pn,pn,0)
		e=random.choice(lst)
		gotodo(e,p,q,pn,n)
		
	def listbox2():
		p=key.get()
		q=key2.get()
		
		if p.isnumeric() and q.isnumeric():
			nameq=Label(root,text='						',bg='#FFFFFF',bd=1,justify=LEFT,font=('Calibri'))
			nameq.place(x=300,y=160)
			p=int(p)
			q=int(q)
			pn=(p-1)*(q-1)
			n=p*q
			
		else:
			nameq=Label(root,text='SAI CÚ PHÁP!!!',bg='#FFFFFF',bd=1,justify=LEFT,font=('Calibri'))
			nameq.place(x=300,y=160)
			return 0
		lst=test.primes(3,pn,pn,1)
		size=[]
		if len(lst)<5000:
			size=str()
			size='ALL'
		elif len(lst)>5000:
			i=0
			s=len(lst)
			j=5000
			while(1):
				if s<5000:
					size.append("{}-{}".format(lst[i],lst[i+s-1]))
					break
				size.append("{}-{}".format(lst[i],lst[j-1]))
				j+=5000
				i+=5000
				s-=5000

		
		def getsize(xxx):
			t=cb.get()
			
			if t=='ALL':
				
				combo.config(value=lst)
			else:

				vt=t.find('-')
				y=lst.index(int(t[:vt]))
				x=lst.index(int(t[vt+1:]))
				combo.config(value=lst[y:x])
			
			try:
				combo.current(0)
			except:
				nameq=Label(root,text='SAI CÚ PHÁP!!! e',bg='#FFFFFF',bd=1,justify=LEFT,font=('Calibri'))
				nameq.place(x=300,y=160)


			
			
			
		
		cb=ttk.Combobox(root,value=size,width=15,font=('Calibri',11))
		cb.place(x=150,y=210)
		cb.current(0)
		cb.bind("<<ComboboxSelected>>",getsize)
		
		namee=Label(root,text='CHỌN E:',bg='#FFFFFF',bd=1,justify=CENTER,font=('Calibri',12,'italic'))
		namee.place(x=50,y=210)
		combo=ttk.Combobox(root,width=15,font=('Calibri',11))
		combo.place(x=350,y=210)
		combo.config(value=lst[:5000])
		combo.current(0)
		def goto(fl=0):
			e=combo.get()
			gotodo(int(e),p,q,pn,n)
		combo.bind("<<ComboboxSelected>>",goto)
		'''
		button_ok2=Button(root,text="Chọn",width=10,height=1,command=goto,bg='#f49b00',fg='#ffffff',bd=0,font=('Calibri (Body)',11,'bold italic'),compound='bottom')
		button_ok2.place(x=390,y=206)
		button_ok2.config(activebackground='#f49b00')
		button_ok2.config(activeforeground='#ffffff')'''


	def gotodo(e,p,q,pn,n):
		fr=Frame(root,width=550,height=490,bg='#FFFFFF')
		fr.place(x=0,y=260)

		z,ht=test.ecu(pn,e)

		button_ok2=Button(root,text="Hiện Bảng",command=lambda:test.hienthi(*ht),width=10,height=1,bg='#f49b00',fg='#ffffff',bd=0,font=('Calibri (Body)',11,'bold italic'),compound='bottom')
		button_ok2.place(x=390,y=260)
		button_ok2.config(activebackground='#f49b00')
		button_ok2.config(activeforeground='#ffffff')
		
		d=test.check(z[2],pn)

		label01=Label(root,text='n = (p*q) = {}'.format(n),bg='#FFFFFF',bd=1,justify=CENTER,font=('Calibri')).place(x=50,y=260)
		label02=Label(root,text='φ(n) = (p-1)*(q-1) = {}'.format(pn),bg='#FFFFFF',bd=1,justify=CENTER,font=('Calibri')).place(x=50,y=310)
		label01=Label(root,text='e = {}'.format(e),bg='#FFFFFF',bd=1,justify=CENTER,font=('Calibri')).place(x=50,y=360)
		label1=Label(root,text='T = {}'.format(z[2]),bg='#FFFFFF',bd=1,justify=CENTER,font=('Calibri')).place(x=50,y=410)
		label2=Label(root,text='S = {}'.format(z[1]),bg='#FFFFFF',bd=1,justify=CENTER,font=('Calibri')).place(x=150,y=410)
		label3=Label(root,text='{}{}'.format('T1>0 d = t1 = 'if z[2]>0 else'T1<0 d = Pn+T1 = ',d),bg='#FFFFFF',bd=1,justify=CENTER,font=('Calibri')).place(x=50,y=460)
		label4=Label(root,text='Public key = (n,e) = ({},{})'.format(n,e),bg='#FFFFFF',bd=1,justify=CENTER,font=('Calibri')).place(x=50,y=510)
		label4=Label(root,text='Private key = (n,d) = ({},{})'.format(n,d),bg='#FFFFFF',bd=1,justify=CENTER,font=('Calibri')).place(x=50,y=560)

		button_ok2=Button(root,text="Mã hóa",command=lambda:enc.mains(pu=(n,e),pr=(n,d)),width=10,height=1,bg='#f49b00',fg='#ffffff',bd=0,font=('Calibri (Body)',11,'bold italic'),compound='bottom')
		button_ok2.place(x=50,y=610)
		button_ok2.config(activebackground='#f49b00')
		button_ok2.config(activeforeground='#ffffff')

		button_ok2=Button(root,text="Giải mã",command=lambda:dec.mains(pu=(n,e),pr=(n,d)),width=10,height=1,bg='#f49b00',fg='#ffffff',bd=0,font=('Calibri (Body)',11,'bold italic'),compound='bottom')
		button_ok2.place(x=200,y=610)
		button_ok2.config(activebackground='#f49b00')
		button_ok2.config(activeforeground='#ffffff')

	key=StringVar()
	key2=StringVar()

	logo=Label(root,text='R S A'.upper(),fg="black",bd=0,bg='#FFFFFF',justify=CENTER)
	logo.config(font=('Calibri',28,'bold'))
	logo.pack()

	nameq=Label(root,text='Nhập P:',bg='#FFFFFF',bd=1,justify=CENTER,font=('Calibri (Body)',11,'bold italic'))
	namep=Label(root,text="Nhập Q:",bg='#FFFFFF',bd=1,justify=CENTER,font=('Calibri (Body)',11,'bold italic'))
	nameq.place(x=50,y=60)
	namep.place(x=50,y=110)

	name2=Entry(root,textvariable=key,justify='left',relief=SUNKEN,font=('Calibri (Body)',12),width=30).place(x=150,y=60)
	pass2=Entry(root,textvariable=key2,justify='left',relief=SUNKEN,font=('Calibri (Body)',12),width=30).place(x=150,y=110)
	button_ok=Button(root,text="Ok",width=10,height=1,command=listbox2,bg='#f49b00',fg='#ffffff',bd=0,font=('Calibri (Body)',11,'bold italic'))
	button_ok.place(x=50,y=160)
	button_ok.config(activebackground='#f49b00')
	button_ok.config(activeforeground='#ffffff')
	button_ok=Button(root,text="Tự động",width=10,height=1,command=randoms,bg='#f49b00',fg='#ffffff',bd=0,font=('Calibri (Body)',11,'bold italic'))
	button_ok.place(x=180,y=160)
	button_ok.config(activebackground='#f49b00')
	button_ok.config(activeforeground='#ffffff')
	root.mainloop()
except Exception as e:
	print(e)
input()
