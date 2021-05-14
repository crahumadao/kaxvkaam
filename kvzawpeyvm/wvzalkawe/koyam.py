import re
from joblib import load
import os
from kvzawpeyvm.wvzalkawe.xoy import *

class Koyam:  # "Roble" // Tree
    def __init__(self, hemvl, rakin_row=0, xoys='', r_xoy=0, wecun_amci=False, folil_amci=True, chumte=0,
                 tvfacihemvl=('', ''), chaw=None, xoy=Xoy()):

        self.hemvl = hemvl  # "hemvl" tati mvlewelu / "Palabra"  lo que queda // Word what lasts
        self.tvfacihemvl = tvfacihemvl
        self.kom_row = []  # "todas las ramas" // all branches
        self.wecun_amci = wecun_amci  # "final?" // end?
        self.folil_amci = folil_amci  # "raiz?" // root?
        self.rakin_row = rakin_row  # "cuenta rama" Nivel // "count branches" Level
        self.xoys = xoys  # "parte" sufijo // "part" suffix
        self.xoy = xoy
        self.r_xoy = r_xoy  # rakin xoy kvme azkvunuam tati txoy zugun // "cuenta parte" sufijo para ordenarlos bien //
        self.chumte = chumte  # chumten xoy /número de sufijo actual
        self.chaw = chaw  # iñi tañi yaj


    def __repr__(self):
        if self.folil_amci:
            return self.hemvl
        else:
            return self.xoys

    def __str__(self):
        return self.hemvl

    def __eq__(self, kagelu):
        r_hemvl = self.hemvl == kagelu.hemvl
        r_rakin_row = self.rakin_row == kagelu.rakin_row
        r_xoys = self.xoys == kagelu.xoys
        r_xoy = self.xoy == kagelu.xoy
        if r_hemvl and r_rakin_row and r_xoy and r_xoys:
            return True
        else:
            return False
#    def __del__(self):
#        print(f'Entugei ti {self.xoys} aliwen mu')
        

    def zewmakoyamvn(self,pre_xoy=[],folil = True):  # zewmaam tati koyam
        tachirakinid=[]
        pre_xoy =pre_xoy+ [self.xoy]
        if len(self.hemvl) <= 0:  # prueba si es que el largo es 0 para la palabra
            self.wecun_amci = True  # No hay palabra => se llego al tope
            return
        if self.wecun_amci:
            return
        
        elif '$' in self.xoy.regex :
            return
        if self.xoy.inafeyu_verbo:
            for xoy in verbo_regex:  # Se buscan coincidencias con cada expresion regular de la lista de verbos
                if not  xoy.cemkeci == 1010 or (xoy.cemkeci==1010 and self.folil_amci):     
                    if xoy not in pre_xoy or not xoy.kineupa:
                        rr = len(self.kom_row)
                        self.rowgetui(xoy,True,pre_xoy)
                        if rr< len(self.kom_row):
                            tachirakinid.append(xoy.id)
            if self.folil_amci and self.rakin_row == 0:
                for xoy in sustantivosAdjetivos:  # Se buscan coincidencias con cada expresion regular de la lista de verbos
                    if not  xoy.cemkeci == 1010 or (xoy.cemkeci==1010 and self.folil_amci):     
                        if xoy not in pre_xoy or not xoy.kineupa :
                            rr = len(self.kom_row)
                            self.rowgetui(xoy,True,pre_xoy)
                            if rr< len(self.kom_row):
                                tachirakinid.append(xoy.id)
                         

        if not self.folil_amci :
            for xoy_set in slotsIneke:  # Se buscan coincidencias con cada lista de expresiones regulares de

                    for xoy in xoy_set: # Se buscan coincidencias con cada expresion regular de la lista de
                        if xoy.id not in tachirakinid:    
                            if self.xoy.rakin <= xoy.rakin:  # que no puede ser inferor en la proxima recursión
                                if xoy not in pre_xoy or not xoy.kineupa:   
                                    rr = len(self.kom_row)
                                    self.rowgetui(xoy,True,pre_xoy)
                                    if rr< len(self.kom_row):
                                        tachirakinid.append(xoy.id)

            for xoy in desinenciasInd:  # Se buscan coincidenciais con cada expresión regular de la lista de
                if xoy.id not in tachirakinid:
                    rr = len(self.kom_row)
                    self.rowgetui(xoy,pre = pre_xoy)
#                    print(xoy.regex, self.hemvl)
                    if rr< len(self.kom_row):

                        tachirakinid.append(xoy.id)

            for xoy in transicionInd:  # Se buscan coincidenciais con cada expresión regular de la lista de
                if xoy.id not in tachirakinid:
                    rr = len(self.kom_row)
                    self.rowgetui(xoy,pre = pre_xoy)
                    if rr< len(self.kom_row):
                        tachirakinid.append(xoy.id)


            for xoy in desinenciasCond:  # Se buscan coincidenciais con cada expresión regular de la lista de
                if xoy.id not in tachirakinid:
                    rr = len(self.kom_row)
                    self.rowgetui(xoy,pre = pre_xoy)
                    if rr< len(self.kom_row):
                        tachirakinid.append(xoy.id)


            for xoy in transicionCond:  # Se buscan coincidenciais con cada expresión regular de la lista de
                if xoy.id not in tachirakinid:
                    rr = len(self.kom_row)
                    self.rowgetui(xoy,pre = pre_xoy)
                    if rr< len(self.kom_row):
                        tachirakinid.append(xoy.id)


            for xoy in desinenciasImpe:  # Se buscan coincidenciais con cada expresión regular de la lista de
                if xoy.id not in tachirakinid:
                    rr = len(self.kom_row)
                    self.rowgetui(xoy,pre = pre_xoy)
                    if rr< len(self.kom_row):
                        tachirakinid.append(xoy.id)


            for xoy in transicionImpe:  # Se buscan coincidenciais con cada expresión regular de la lista de
                if xoy.id not in tachirakinid:
                    rr = len(self.kom_row)
                    self.rowgetui(xoy,pre = pre_xoy)
                    if rr< len(self.kom_row):
                        tachirakinid.append(xoy.id)


            for xoy in otrasDesinencias:  # Se buscan coincidenciais con cada expresión regular de la lista de
                if xoy.id not in tachirakinid:
                    rr = len(self.kom_row)
                    self.rowgetui(xoy,pre = pre_xoy)
                    if rr< len(self.kom_row):
                        tachirakinid.append(xoy.id)


        return

    def rowgetui(self, xoy, verbyslot = False,pre=[]):

        if xoy.mvli(self.hemvl):
            xoys, mvlewelu = xoy.wvzage(self.hemvl)
            wac = len(mvlewelu)==0 
            if not wac and xoy.cemkeci ==2:
                return
            if verbyslot:
                wac = False
            #print(pre,xoys)            
            kellu_koyam = Koyam(mvlewelu, rakin_row=self.rakin_row + 1, xoys=xoys,
                    folil_amci=False, wecun_amci=wac, chaw = self, xoy=xoy)
            kellu_koyam.zewmakoyamvn(pre)
            if kellu_koyam not in self.kom_row:
                self.kom_row.append(kellu_koyam)





    def kaxvrowvn(self):        

 
            if len(self.kom_row)!=0:
                for row in self.kom_row:        

                    if len(row.kom_row)==0:
                        if len(row.hemvl)>0:

                            try:
                                del self.kom_row[self.kom_row.index(row)]
                            except:
                                print('gewelai')
                            
                        #else:
                        #    if not row.xoy.wecun and row.xoy.rakin>0:
                        #        try:                                
                        #            del self.kom_row[self.kom_row.index(row)]
                        #        except:
                        #            print('gewelai')
        
                
                    else:
                        for srow in row.kom_row:
                            srow.kaxvrowvn()
                            
                        row.kaxvrowvn()                        
                            
                        if len(row.kom_row)==0 and row.hemvl != '':
                            try:                                
                                del self.kom_row[self.kom_row.index(row)]
                            except:
                                print('gewelai')
#                        elif len(row.kom_row)==0 and row.hemvl =='':
                            

                               
            elif len(self.kom_row)==0:

                if len(self.hemvl)>0 and not self.folil_amci:
                    del self.chaw.kom_row[self.chaw.kom_row.index(self)]

    def wirintuku_hemvl(self):
        wirintukual = ''
        if len(self.kom_row) == 0:
            return str(self)  + self.xoys + '\n'
        for row in self.kom_row:
            if self.folil_amci:
                wirintukual += self.xoys + row.wirintuku_hemvl()
            else:
                wirintukual += self.xoys + '-' + row.wirintuku_hemvl()
        return wirintukual


    def wirintuku_hemvl2(self,pre=''):
        hemvlkvf=[]
        if len(self.kom_row)==0:
            return [pre+self.xoys]
        for row in self.kom_row:
                hemvlkvf.extend(row.wirintuku_hemvl2(pre+self.xoys+'-'))
        return hemvlkvf


    def wirintuku_regex(self,pre=[]):
        hemvlkvf=[]
        if len(self.kom_row)==0:
            return pre+[self.xoy.regex]

        for row in self.kom_row:
            hemvlkvf+=row.wirintuku_regex(pre+[self.xoy.regex])
        return hemvlkvf

    def wirintuku_wz(self,pre=''):
        hemvlkvf=[]
        if len(self.kom_row)==0:
            return [pre+self.xoy.wigkazugun]
        for row in self.kom_row:
                hemvlkvf.extend(row.wirintuku_wz(pre+self.xoy.wigkazugun+'-'))
        return hemvlkvf
 




    def wirintukukoyam(self):
        for row in self.kom_row:
            pegelam=row.rakin_row * '\t' + row.xoys+'\n'
            for srow in row.kom_row:
                if len(srow.kom_row)>0 :
                    pegelam+=srow.rakin_row*'\t'+ srow.xoys+'\n'
                    aa = srow.wirintukukoyam()
                    if aa:
                        pegelam +=aa
                else:
                    pegelam+=srow.rakin_row*'\t'+srow.xoys+'\n'
                    #print(   srow.rakin_row*'\t'+srow.xoy)
        return pegelam


    def rakiamwecun(self):
        a = 1
        if len(self.kom_row)==0:
            return 1
        for row in self.kom_row:
            a+=rakiamwecun()
        return a


   
