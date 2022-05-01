import sys
from PyQt5.QtWidgets import *
import math

app=QApplication(sys.argv)
qw=QWidget()
qw.setWindowTitle('Bảng hiện thị RSA')
qw.resize(1300,300)
layout=QVBoxLayout()
tablew=QTableWidget()
tablew.setColumnCount(10)

def ecu(pn,e):
	lr1,lr2,lr,lq,ls1,ls2,ls,lt1,lt2,lt=[[] for x in range(10)]
	r1=pn
	r2=e
	t2,s1=1,1
	t1,s2=0,0
	lr1.append(r1)
	lr2.append(r2)
	ls1.append(s1)
	ls2.append(s2)
	lt1.append(t1)
	lt2.append(t2)	
	while(r2>0):

		q=int(r1/r2)
		r=r1-q*r2
		s=s1-q*s2
		t=t1-q*t2
	
		r1,r2=r2,r
		
		s1,s2=s2,s
		
		t1,t2=t2,t
		

		
		lq.append(q)

		lr1.append(r1)
		lr2.append(r2)
		lr.append(r)

		ls1.append(s1)
		ls2.append(s2)
		ls.append(s)

		lt1.append(t1)
		lt2.append(t2)
		lt.append(t)
	return (r1,s1,t1),(lq,lr1,lr2,lr,ls1,ls2,ls,lt1,lt2,lt)

def hienthi(lq,lr1,lr2,lr,ls1,ls2,ls,lt1,lt2,lt):
	tablew.setHorizontalHeaderItem(0,QTableWidgetItem("q"))
	tablew.setHorizontalHeaderItem(1,QTableWidgetItem("r1"))
	tablew.setHorizontalHeaderItem(2,QTableWidgetItem("r2"))
	tablew.setHorizontalHeaderItem(3,QTableWidgetItem("r"))
	tablew.setHorizontalHeaderItem(4,QTableWidgetItem("s1"))
	tablew.setHorizontalHeaderItem(5,QTableWidgetItem("s2"))
	tablew.setHorizontalHeaderItem(6,QTableWidgetItem("s"))
	tablew.setHorizontalHeaderItem(7,QTableWidgetItem("t1"))
	tablew.setHorizontalHeaderItem(8,QTableWidgetItem("t2"))
	tablew.setHorizontalHeaderItem(9,QTableWidgetItem("t"))
	idem=0
	i=0
	while(1):
		
		if lr2[i]==0:
			tablew.setRowCount(idem+1)
			
			tablew.setItem(idem,1,QTableWidgetItem(str(lr1[i])))
			tablew.setItem(idem,2,QTableWidgetItem(str(lr2[i])))
			
			tablew.setItem(idem,4,QTableWidgetItem(str(ls1[i])))
			tablew.setItem(idem,5,QTableWidgetItem(str(ls2[i])))
			
			tablew.setItem(idem,7,QTableWidgetItem(str(lt1[i])))
			tablew.setItem(idem,8,QTableWidgetItem(str(lt2[i])))
			
			break
		else:
			tablew.setRowCount(idem+2)
			tablew.setItem(idem,0,QTableWidgetItem(str(lq[i])))
			tablew.setItem(idem,1,QTableWidgetItem(str(lr1[i])))
			tablew.setItem(idem,2,QTableWidgetItem(str(lr2[i])))
			tablew.setItem(idem,3,QTableWidgetItem(str(lr[i])))
			tablew.setItem(idem,4,QTableWidgetItem(str(ls1[i])))
			tablew.setItem(idem,5,QTableWidgetItem(str(ls2[i])))
			tablew.setItem(idem,6,QTableWidgetItem(str(ls[i])))
			tablew.setItem(idem,7,QTableWidgetItem(str(lt1[i])))
			tablew.setItem(idem,8,QTableWidgetItem(str(lt2[i])))
			tablew.setItem(idem,9,QTableWidgetItem(str(lt[i])))
			idem+=1
			i+=1
		
	layout.addWidget(tablew)
	qw.show()
	qw.setLayout(layout)

def primes(start,end,pn,en):

    out = list()
    sieve = [True] * (end+1)
    for p in range(3, end+1,2):
        if (sieve[p]) and math.gcd(p,pn)==1 :
            out.append(p)
            for i in range(p, end+1, p):
                sieve[i] = False
    return out
def primes2(start,end):

    out = list()
    sieve = [True] * (end+1)
    for p in range(3, end+1,2):
        if (sieve[p]):
            out.append(p)
            for i in range(p, end+1, p):
                sieve[i] = False
    return out   
def check(t1,pn):
	if t1>0:
		return t1
	elif t1<0:
		return pn+t1


def main(p,q):
	
	n=p*q
	pn=(p-1)*(q-1)
	lstprime=findprime(2,pn,pn)
	#print(lstprime)
	z=ecu(pn,7)
	#print(z)
	d=check(z[2],pn)
	print(d)
	layout.addWidget(tablew)
	qw.show()
	qw.setLayout(layout)

	#sys.exit(app.exec_())


