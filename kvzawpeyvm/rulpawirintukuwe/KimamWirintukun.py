#Identificador

#Cargar Reglas AZVMCEFE UNIFICADO RAGILEO
import re
from kvzawpeyvm.rulpawirintukuwe.Reglas import reglas12, reglas13, reglas21, reglas23, reglas31, reglas32



def ragileo1ca(txt):
    txt2 = reglas21.rulpawe(txt)
    txt1 = reglas12.rulpawe(txt2)
#    print(f'r1:{txt}->{txt2}->{txt1} >>{txt==txt1}')
    if txt == txt1:
        return True	
    else:
        return False
    
def ragileo2ca(txt):
    txt2 = reglas23.rulpawe(txt)
    txt1 = reglas32.rulpawe(txt2)
#    print(f'r2:{txt}->{txt2}->{txt1} >>{txt==txt1}')
    if txt == txt1:
        return True	
    else:
        return False


def unificado1ca(txt):
    txt2 = reglas12.rulpawe(txt)
    txt1 = reglas21.rulpawe(txt2)
#    print(f'u1:{txt}->{txt2}->{txt1} >>{txt==txt1}')
    if txt == txt1:
        return True	
    else:
        return False
    
def unificado2ca(txt):
    txt2 = reglas13.rulpawe(txt)
    txt1 = reglas31.rulpawe(txt2)
#    print(f'u2:{txt}->{txt2}->{txt1} >>{txt==txt1}')
    if txt == txt1:
        return True	
    else:
        return False

def azvmcefe1ca(txt):
    txt2 = reglas32.rulpawe(txt)
    txt1 = reglas23.rulpawe(txt2)
#    print(f'a1:{txt}->{txt2}->{txt1} >>{txt==txt1}')
    if txt == txt1:
        return True	
    else:
        return False

def azvmcefe2ca(txt):
    txt2 = reglas31.rulpawe(txt)
    txt1 = reglas13.rulpawe(txt2)
#    print(f'a2:{txt}->{txt2}->{txt1} >>{txt==txt1}')
    if txt == txt1:
        return True	
    else:
        return False

def chuchiWirintukun(txt):
    ## CODIGO
    ## Unificado = 'u0'
    ## Ragileo   = 'r0'
    ## Azvmcefe  = 'a0'
    wirintukun = []  
    
    #Unificado mu wirintukugei?
    UN1 = unificado1ca(txt)
    UN2 = unificado2ca(txt)
	#Ragileo mu wirintukugei?
    RA1 = ragileo1ca(txt)
    RA2 = ragileo2ca(txt)    
    #Azvmcefe mu wirintukugei?
    AZ1 = azvmcefe1ca(txt)
    AZ2 = azvmcefe2ca(txt)

    UNgey=UN1 and UN2
    RAgey=RA1 and RA2
    AZgey=AZ1 and AZ2
    
    if AZgey:
        wirintukun.append(('a0',reglas32.rulpawe(txt)))
        print('Azvmcefe')
    if UNgey:
        wirintukun.append(('u0',reglas12.rulpawe(txt)))
        print('Unificado',)  

    if RAgey:
        wirintukun.append(('r0',txt))
        print('Ragileo')

    if not (UNgey or RAgey or AZgey):   
        print('Ninguno')
        
        txtalt =txt
        txtalt=re.sub('ch','c',txtalt)
        RA1 = ragileo1ca(txtalt)
        RA2 = ragileo2ca(txtalt)    
        RAgey = RA1 and RA2 
        if RAgey:
            wirintukun.append(('rv1',txtalt))
            print('ragileo nielu CH')
            
        txtalt = txt
        txtalt=re.sub('ü','v',txtalt)
        RA1 = ragileo1ca(txtalt)
        RA2 = ragileo2ca(txtalt)
        RAgey = RA1 and RA2
        if RAgey:
            wirintukun.append(('rv2',txtalt))
            print('ragileo nielu Ü')
        
        txtalt =txt
        txtalt=re.sub('d','z',txtalt)
        RA1 = ragileo1ca(txtalt)
        RA2 = ragileo2ca(txtalt)
        RAgey = RA1 and RA2
        if RAgey:
            wirintukun.append(('rv3',txtalt))
            print('ragileo nielu D')

        #Unificado nielu Z
        txtalt =txt
        txtalt=re.sub('z','d',txtalt)
        UN1 = unificado1ca(txtalt)
        UN2 = unificado2ca(txtalt) 
        UNgey = UN1 and UN2
        if UNgey:
            wirintukun.append(('uv1',reglas12.rulpawe(txtalt)))
            print('Unificado nielu Z')



        #Unificado nielu tx
        txtalt =txt
        txtalt=re.sub('tx','tr',txtalt)
        UN1 = unificado1ca(txtalt)
        UN2 = unificado2ca(txtalt)    
        UNgey = UN1 and UN2 
        if UNgey:
            wirintukun.append(('uv2',reglas12.rulpawe(txtalt)))
            print('Unificado nielu tx')

        #Azvmcefe nielu Tr
        txtalt =txt
        txtalt=re.sub('tr','tx',txtalt)
        AZ1 = unificado1ca(txtalt)
        AZ2 = unificado2ca(txtalt)    
        AZgey = AZ1 and AZ2 
        if AZgey:
            wirintukun.append(('av1',reglas32.rulpawe(txtalt)))
            print('Azvmcefe nielu tr')

        #Azvmcefe nielu Ng
        txtalt =txt
        txtalt=re.sub('(?<!n)g','q',txtalt)
        txtalt=re.sub('ng','g',txtalt)
        txtalt=re.sub('g','',txtalt)
        AZ1 = unificado1ca(txtalt)
        AZ2 = unificado2ca(txtalt)    
        AZgey = AZ1 and AZ2 
        if AZgey:
            wirintukun.append(('av2',reglas32.rulpawe(txtalt)))
            print('Unificado nielu ng')
    if len(wirintukun)==0:  
        print('azvmgelai tati wirintukun')
    return(wirintukun)        
        
'''        
import os        
while True:
    os.system('clear')
    txt = input('hemvl\n')
    txt = txt.strip().lower()
    txt = re.sub('[0-9\W]','',txt)

    if len(txt)>=1:
        chuchiWirintukun(txt)
        input()
    else:
        print('cew mvli tami hemvl?')
        continue
        
'''
