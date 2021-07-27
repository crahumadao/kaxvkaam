from joblib import load
import os
import re

def sort_(s, n):
    for i in range(1, n):

        temp = s[i]
        # Insert s[j] at its correct position
        j = i - 1

        while j >= 0 and len(s[j]) > len(temp):
            s[j + 1] = s[j]
            j -= 1

        s[j + 1] = temp


#set_verbo = load('ziksionario.map')
try:
    set_verbo = load('ziksionario.map')
except:
    set_verbo = load('ziksionario.map')

verbo_vy = list(set_verbo.keys())

# sort(verbo_vy,len(verbo_vy))
verbo_vy.reverse()
verbo_regex = []

for verbo in verbo_vy:
    fewladef = set_verbo[verbo]
    vocales = ['a', 'e', 'i', 'o', 'u', 'v']
    if '(' in verbo:
        meturegexgenon = [a for a in re.split('[()]', verbo) if len(a) > 0]
        if len(meturegexgenon) == 2:
            op1 = meturegexgenon[0]
            if op1[-1] not in vocales:
                op1 += 'v{0,1}'
            op2 = meturegexgenon[0] + meturegexgenon[1]
            if op2[-1] not in vocales:
                op2 += 'v{0,1}'
            verbo = op1 + '|' + op2
        elif len(meturegexgenon) == 3:
            op1 = meturegexgenon[0] + meturegexgenon[2]
            if op1[-1] not in vocales:
                op1 += 'v{0,1}'
            op2 = meturegexgenon[0] + meturegexgenon[1] + meturegexgenon[2]
            if op2[-1] not in vocales:
                op2 += 'v{0,1}'
            verbo = op1 + '|' + op2

    verbo_regex.append([verbo,fewladef])

vidx=0
towrite=''
for regex in verbo_regex:
    if 'vi '  in regex[1].lower() or 'vtr '  in regex[1].lower() or  'vi. ' not in regex[1].lower() or 'vtr. '  in regex[1].lower():
        towrite = towrite + f"Xoy('{'Vi'+str(vidx)}', '{regex[0]}', False,0,True, '{regex[1]}',False,0),\n"
        vidx+=1


towritealt = ''
vidx=0
for regex in verbo_regex:
    if 'vi ' not in regex[1].lower() and 'vtr ' not in regex[1].lower() and  'vi. ' not in regex[1].lower() and 'vtr. ' not in regex[1].lower():
        towritealt = towritealt + f"Xoy('{'SA'+str(vidx)}', '{regex[0]}', False,0,True, '{regex[1]}',False,0),\n"
        vidx+=1
    
print(towrite)
#print(towritealt)


