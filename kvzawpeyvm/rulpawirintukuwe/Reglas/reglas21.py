#!/usr/bin/env python
# -*- coding: utf-8 -*-
import re
def rulpawe(txt): 			#UNI    RAG
	#txt=re.sub()	ex		#A,a	A,a
#	txt=re.sub('h(?<!sScC)','n_',txt)	#N_,n_	H,h
#	txt=re.sub('(?<![sScCtT])h','n_',txt)	#N_,n_	H,h
	txt=re.sub('(?<![sScCtT])h','n_',txt)	#N_,n_	H,h

	txt=re.sub('(?<![sScCtT])H','N_',txt)	#N_,n_	H,h	
#	txt=re.sub('H(?<!sScC)','N_',txt)	#N_,n_	H,h
	txt=re.sub('c(?![hH])','ch',txt)	#Ch,ch 	C,c
	txt=re.sub('C(?![hH])','Ch',txt)	#Ch,ch 	C,c
	txt=re.sub('z','d',txt)		#D,d	Z,z
	txt=re.sub('Z','D',txt)		#D,d	Z,z
	#txt=re.sub()			#E,e	E,e
	#txt=re.sub()			#F,f	F,f
	txt=re.sub('(?<![Nn])g','ng',txt)	#Ng,ng	G,g
	txt=re.sub('(?<![Nn])G','Ng',txt)	#Ng,ng	G,g
	txt=re.sub('q','g',txt)		#G,g	Q,q
	txt=re.sub('Q','G',txt)		#G,g	Q,q
	#txt=re.sub()			#I,i	I,i
	#txt=re.sub()			#K,k	K,k
	#txt=re.sub()			#L,l	L,l
	txt=re.sub('b','l_',txt)	#L_,l_	B,b
	txt=re.sub('B','L_',txt)	#L_,l_	B,b
	txt=re.sub('j','ll',txt)	#Ll,ll	J,j
	txt=re.sub('J','Ll',txt)	#Ll,ll	J,j
	#txt=re.sub()			#M,m	M,m
	#txt=re.sub()			#N,n	N,n
	#txt=re.sub()			#Ñ,ñ	Ñ,ñ

	#txt=re.sub()			#T,t	T,t
	txt=re.sub('(?<![tT])x','tr',txt)	#Tr,tr	X,x
	txt=re.sub('(?<![tT])X','Tr',txt)	#Tr,tr	X,x
	#txt=re.sub()			#U,u	U,u
	txt=re.sub('v','ü',txt)		#Ü,ü	V,v
	txt=re.sub('V','Ü',txt)		#Ü,ü	V,v
	#txt=re.sub()			#W,w	W,w
	#txt=re.sub()			#Y,y	Y,y
	return txt


def mapuchewvn(txt):
	#voc=re.compile(r'[aeiouAEIOU]')
	#cons=re.compile(r'[BCDFGHJKL(LL)(Ll)MNÑPQRSTVWXYZbcdfghjkl(ll)mnñpqrstvwxyz])
	#txt=re.sub(,txt)#A
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
	txt=re.sub('B','F',txt)#B
	txt=re.sub('b','f',txt)#B
	txt=re.sub(r'C(?=[aouAOU])','K',txt)#C
	txt=re.sub(r'c(?=[aouAOU])','k',txt)#C
	txt=re.sub(r'C(?=[eiEI])','S',txt)#C
	txt=re.sub(r'c(?=[eiEI])','s',txt)#C
	txt=re.sub('CH','C',txt)#CH	
	txt=re.sub('Ch','C',txt)#CH	
	txt=re.sub('ch','c',txt)#CH	
	txt=re.sub('Z','S',txt)#D
	txt=re.sub('z','s',txt)#D
	txt=re.sub('D','Z',txt)#D
	txt=re.sub('d','z',txt)#D
	#txt=re.sub(,txt)#F
	txt=re.sub(r'G[Uu]*[Ii]','Ki',txt)	#G
	txt=re.sub(r'g[Uu]*[Ii]','ki',txt)	#G
	txt=re.sub(r'G[Ee]','Ke',txt)	#G
	txt=re.sub(r'g[Ee]','ke',txt)	#G
	txt=re.sub(r'G[Üü]','W',txt)	
	txt=re.sub(r'gü','w',txt)
	txt=re.sub(r'G[Uu](?=[aoAO])','W',txt)
	txt=re.sub(r'g[u](?=[aoAO])','w',txt)
	txt=re.sub(r'[H][Uu]','W',txt)#H
	txt=re.sub(r'[h][Uu]','W',txt)#H
	txt=re.sub(r'H[aeioAEIO]','',txt)#H
	txt=re.sub(r'h[aeioAEIO]','',txt)#H
	#txt=re.sub(,txt)#I
	txt=re.sub('J','K',txt)#J
	txt=re.sub('j','k',txt)#J
	#txt=re.sub(,txt)#K
	#txt=re.sub(,txt)#L
	#txt=re.sub(,txt)#LL
	#txt=re.sub(,txt)#M
	#txt=re.sub(,txt)#N
	#txt=re.sub(,txt)#Ñ
	#txt=re.sub(,txt)#O
	#txt=re.sub(,txt)#P
	txt=re.sub(r'Q[uU]','K',txt)#Q
	txt=re.sub(r'q[uU]','k',txt)#Q
	txt=re.sub(r'R[Rr]','R',txt)#R[RR]
	txt=re.sub(r'r[Rr]','r',txt)#R[RR]
	txt=re.sub(r'(?=[bcdfgkpv])[r]','ür',txt)
	txt=re.sub(r'(?<=[BCDFGKPVbcdfgkpv])r','ür',txt)
	txt=re.sub(r'[sS]\s',' ',txt)#S
	txt=re.sub(r'[sS]\Z','',txt)#S
	txt=re.sub(r'[sS](?![a-zA-ZüÜáéíóúÁÉÍÓÚ])','',txt)#S
	txt=re.sub('X','Ks',txt)#X
	txt=re.sub('x','ks',txt)#X
	txt=re.sub('tr','x',txt)#T
	txt=re.sub(r'T[rR]','X',txt)#T
	#txt=re.sub(,txt)#U
	txt=re.sub('V','F',txt)#V
	txt=re.sub('v','f',txt)#V
	#txt=re.sub(,txt)#W
	#txt=re.sub(,txt)#Y
	#txt=re.sub(,txt)#Z
	return txt
