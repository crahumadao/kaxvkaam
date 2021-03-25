#!/usr/bin/env python
# -*- coding: utf-8 -*-
import re #(CAMBIAR ORDEN)
def rulpawe(txt): 			#RAG    AZÜ
	txt=re.sub('nh','h',txt)	#H,h	Nh,nh
	txt=re.sub('Nh','H',txt)	#H,h	Nh,nh
	txt=re.sub('NH','H',txt)	#H,h	Nh,nh
	#txt=re.sub()			#A,a	A,a
	txt=re.sub('ch','c',txt)	#C,c	Ch,ch
	txt=re.sub('Ch','C',txt)	#C,c 	Ch,ch
	txt=re.sub('CH','C',txt)	#C,c 	Ch,ch
	#txt=re.sub()			#Z,z	Z,Z
	#txt=re.sub()			#E,e	E,e
	#txt=re.sub()			#F,f	F,f
	#txt=re.sub()			#Q,q	Q,q
	#txt=re.sub()			#I,i	I,i
	#txt=re.sub()			#K,k	K,k
	#txt=re.sub()			#L,l	L,l
	txt=re.sub('lh','b',txt)	#B,b	Lh,lh
	txt=re.sub('Lh','B',txt)	#B,b	Lh,lh
	txt=re.sub('LH','B',txt)	#B,b	Lh,lh
	txt=re.sub('ll','j',txt)	#J,j	Ll,ll
	txt=re.sub('Ll','J',txt)	#J,j	Ll,ll
	txt=re.sub('LL','J',txt)	#J,j	Ll,ll
	#txt=re.sub()			#M,m	M,m
	#txt=re.sub()			#N,n	N,n
	#txt=re.sub()			#Ñ,ñ	Ñ,ñ
	#txt=re.sub()			#G,g	G,g
	#txt=re.sub()			#O,o	O,o
	#txt=re.sub()			#P,p	P,p
	#txt=re.sub()			#R,r	R,r
	#txt=re.sub('sh','s',txt)	#S,s	Sh,sh
	#txt=re.sub('Sh','S',txt)	#S,s	Sh,sh
	#txt=re.sub('SH','S',txt)	#S,s	Sh,sh
	#txt=re.sub()			#T,t	T,t
	txt=re.sub('tx','x',txt)	#X,x	Tx,tx
	txt=re.sub('Tx','X',txt)	#X,x	Tx,tx
	txt=re.sub('TX','X',txt)	#X,x	Tx,tx
	#txt=re.sub()			#---	T',t'*****
	#txt=re.sub()			#U,u	U,u
	txt=re.sub('ü','v',txt)		#V,v	Ü,ü
	txt=re.sub('Ü','V',txt)		#V,v	Ü,ü
	#txt=re.sub()			#W,w	W,w
	#txt=re.sub()			#Y,y	Y,y
	return txt


def mapuchewvn(txt):
	txt=re.sub('Á','A',txt)
	txt=re.sub('á','a',txt)
	txt=re.sub('É','E',txt)
	txt=re.sub('é','e',txt)
	txt=re.sub('Í','I',txt)
	txt=re.sub('í','i',txt)
	txt=re.sub('Ó','O',txt)
	txt=re.sub('ó','o',txt)
	txt=re.sub('Ú','U',txt)
	txt=re.sub('ú','u',txt)
	#txt=re.sub() #A
	txt=re.sub(r'B','F',txt) #B
	txt=re.sub(r'b','f',txt) #B
	txt=re.sub(r'C(?=[aouAOU])','K',txt)#C
	txt=re.sub(r'c(?=[aouAOU])','k',txt)#C
	txt=re.sub(r'C(?=[eiEI])','S',txt)#C
	txt=re.sub(r'c(?=[eiEI])','s',txt)#C
	txt=re.sub(r'[sS]\Z','',txt)#S
	txt=re.sub(r'[sS](?![a-zA-ZüÜáéíóúÁÉÍÓÚ])','',txt)#S
	#txt=re.sub()	#CH
	txt=re.sub(r'Z','S',txt)#Z
	txt=re.sub(r'z','s',txt)#Z
	txt=re.sub(r'D','Z',txt)	#D
	txt=re.sub(r'd','z',txt)	#D
	#txt=re.sub()	#E
	#txt=re.sub()	#F
	txt=re.sub(r'G[Uu]*[Ii]','Ki',txt)	#G
	txt=re.sub(r'g[Uu]*[Ii]','ki',txt)	#G
	txt=re.sub(r'G[Ee]','Ke',txt)	#G
	txt=re.sub(r'g[Ee]','ke',txt)	#G
	txt=re.sub(r'G[Üü]','W',txt)	
	txt=re.sub(r'gü','w',txt)
	txt=re.sub(r'G[Uu](?=[aoAO])','W',txt)
	txt=re.sub(r'g[u](?=[aoAO])','w',txt)
	txt=re.sub(r'[^cC][H][Uu]','W',txt)#H
	txt=re.sub(r'[^cC][h][Uu]','W',txt)#H
	txt=re.sub(r'[^Cc]H[aeioAEIO]','',txt)#H
	txt=re.sub(r'[^Cc]h[aeioAEIO]','',txt)#H
	#txt=re.sub()	#I
	txt=re.sub(r'J','K',txt)	#J
	txt=re.sub(r'j','k',txt)	#J
	#txt=re.sub()	#K
	#txt=re.sub()	#L
	#txt=re.sub()	#LL
	#txt=re.sub()	#M
	#txt=re.sub()	#N
	#txt=re.sub()	#Ñ
	#txt=re.sub()	#O
	#txt=re.sub()	#P
	txt=re.sub(r'Q[uU]','K',txt)#Q
	txt=re.sub(r'q[uU]','k',txt)#Q
	txt=re.sub(r'R[Rr]','R',txt)#R[RR]
	txt=re.sub(r'r[Rr]','r',txt)#R[RR]
	txt=re.sub(r'(?=[bcdfgkpv])[r]','ür',txt)
	txt=re.sub(r'(?<=[BCDFGKPVbcdfgkpv])r','ür',txt)
	txt=re.sub(r'X','Ks',txt)#X
	txt=re.sub(r'x','ks',txt)#X
	txt=re.sub(r'T[rR]','Tx',txt)	#T
	txt=re.sub(r'tr','tx',txt)	#T
	#txt=re.sub()	#U
	txt=re.sub(r'V','F',txt)#V
	txt=re.sub(r'v','f',txt)#V
	#txt=re.sub()	#W
	#txt=re.sub()	#X
	#txt=re.sub()	#Y
	return txt	

