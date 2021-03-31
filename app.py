from flask import Flask, render_template, jsonify, render_template, request, redirect, url_for, flash, current_app
from kvzawpeyvm.wvzalkawe.koyam import Koyam
from kvzawpeyvm.rulpawirintukuwe.KimamWirintukun import chuchiWirintukun
from kvzawpeyvm.rulpawirintukuwe.Reglas import reglas12, reglas13, reglas21, reglas23, reglas31, reglas32
import time
import datetime
import webbrowser
import pickle
import os
import re

app = Flask(__name__)
app.secret_key = b'k#1"E/0$j&2U_9=n'

def rupaka(txt):
    return(txt)
wirintukunVy = {
                'a0'  : ('Azümchefe',            lambda w:reglas23.rulpawe(w)),
                'r0'  : ('Ragileo',              lambda w:rupaka(w)),
                'u0'  : ('Unificado',            lambda w:reglas21.rulpawe(w)),
                'av1' : ('Azümchefe + Tx -> Tr', lambda w:re.sub('tx','tr',reglas23.rulpawe(w))),
                'av2' : ('Azümchefe + G  -> Ng', lambda w:re.sub('g','ng',reglas23.rulpawe(w))),
                'rv1' : ('Ragileo + C -> Ch',    lambda w:re.sub('c','ch',w)),
                'rv2' : ('Ragileo + V -> Ü',     lambda w:re.sub('v','ü',w)),  
                'rv3' : ('Ragileo + Z -> D',     lambda w:re.sub('z','d',w)),
                'uv1' : ('Unificado + D -> Z',   lambda w:re.sub('d','z',reglas21.rulpawe(w))),
                'uv2' : ('Unificado + Tr -> Tx', lambda w:re.sub('tr','tx',reglas21.rulpawe(w)))
}

def pepikaam_hemvl(hemvl, mvlica):
    hemvl.lower()
    wirintukun= chuchiWirintukun(hemvl)
    xipaalu = dict()

    Nm=0
    koyam=None
    wirina=()
    for wirin in wirintukun:
        kkoyam = Koyam(wirin[1].lower())
        kkoyam.zewmakoyamvn()
        if Nm<len(kkoyam.kom_row):
            Nm=len(kkoyam.kom_row)
            koyam = kkoyam          
            wirina = wirin 
    if mvlica and len(wirintukun)>0 and type(koyam)!= type(None) and Nm>0:        
        xipaalu['vy'] = hemvl
        xipaalu['wirintukun'] = wirintukunVy[wirina[0]][0]
#        koyam = Koyam(hemvl.lower())
#        koyam.zewmakoyamvn()
        rr = len(koyam.kom_row)
        while True:
            koyam.kaxvrowvn()
            if rr == len(koyam.kom_row):
                break
            else:
                rr = len(koyam.kom_row)
        
        hemvlkawe = koyam.wirintuku_hemvl2()
        hemvlkawe =  [wirintukunVy[wirina[0]][1](h) for h in hemvlkawe]
        hemvlkawew = [h.split('-')[1:] for h in hemvlkawe]
        regexkawe = koyam.wirintuku_regex()
        wzkawe = koyam.wirintuku_wz()
        wzkawe = [h.split('-')[1:] for h in wzkawe]
        aux = []
        aux2 = []
        for item in regexkawe:
            if item != '^':
                aux2.append(item)
            else:
                aux.append(aux2)
                aux2 = []
        aux.append(aux2)
        regexkawe = aux
        regexkawe.pop(0)
        del aux
        del aux2
        # hemvlKoyam =koyam.wirintukukoyam()
        # hemvlKoyam = re.sub(r'\t(?=[a-zA-Z])','|__',hemvlKoyam)
        # hemvlKoyam = re.sub(r'\t','    ',hemvlKoyam)
        xapvmal = []
        xipaalu['eypial'] = 'Femgechi wüzalkafiñ'
        xipaalu['decir'] = 'Así lo separé'
        if rr==0:
            xipaalu['xipai'] = False
        else:
            xipaalu['xipai'] = True
        if len(hemvlkawe) > 0:
            for i in range(len(hemvlkawe)):
                xapvmal.append((hemvlkawe[i], regexkawe[i],wzkawe[i],hemvlkawew[i]))
            xipaalu['hemvlkawe'] = xapvmal


    else:
        xipaalu = dict()
        xipaalu['vy'] = hemvl
        xipaalu['eypial'] = 'Pelan tami nhemül, ka kiñe rupa tukulfe'
        xipaalu['decir'] = 'No encontré tu palabra, ponla nuevamente'
        xipaalu['xipai'] = False
    return xipaalu


@app.route('/', methods=['GET'])
def konwe():
    mvli = False
    pegelam_hemvl = {'vy': ''}
    return render_template('index.html', mvli=mvli, pegelam_hemvl=pegelam_hemvl)


@app.route('/wvzalkafe', methods=['POST', 'GET'])
def pegelwe():
    if 'hemvl' in request.form.keys():
        hemvl = request.form.get('hemvl')
        if len(hemvl) > 0:
            mvli = True
            pegelam_hemvl = pepikaam_hemvl(hemvl, mvli)
            mvli = pegelam_hemvl['xipai']
        else:
            mvli = False
            pegelam_hemvl = pepikaam_hemvl(hemvl, mvli)
            mvli = pegelam_hemvl['xipai']
    else:
        mvli = False
        hemvl = ''
        pegelam_hemvl = pepikaam_hemvl(hemvl, mvli)
        mvli = pegelam_hemvl['xipai']
    return render_template('index.html', mvli=mvli, pegelam_hemvl=pegelam_hemvl)


@app.route('/kellual',methods=['POST','GET'])
def werkvlal_msg():
    flash('Recibimos tu mensjae, gracias por ayudarnos / Llowfiiñ tami werkvlfiel, mañumuwiyiñ tami kellumufiel ')
    fewla = str(datetime.datetime.now())[:-7]
    eypi = url_for('static',filename='eypietew.txt')
    elkvnualkellunzugu = open(eypi[1:],'a+')
    
    if request.method == 'POST':
        kellun = request.form.get('kellun')
        fewlahemvl = request.form.get('fewlahemvl')
    msg = f'{fewla}:\t("{fewlahemvl}" nhemül mu):\t MSG: {kellun} :MSG\n'
    print(msg)
    elkvnualkellunzugu.write(msg)
    elkvnualkellunzugu.close()
    return redirect(url_for('konwe'))

@app.errorhandler(404)
def page_not_found(error):
    return '<h1> \'Na weza</h1>\n<h2>pegerkelai tati pakina </h2>'


if __name__ == '__main__':
    #app.run('0.0.0.0', 5000, debug=True)
    app.run()
