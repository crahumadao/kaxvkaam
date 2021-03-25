from flask import Flask, render_template, jsonify, render_template, request
from kaxvkaam.kvzawpeyvm.wvzalkawe.koyam import *
#from kvzawpeyvm.wvzalkawe.xoy import *
import webbrowser
import pickle
import os
import re

app = Flask(__name__)


def pepikaam_hemvl(hemvl, mvlica):
    hemvl.lower()
    xipaalu = dict()
    if mvlica:
        xipaalu['vy'] = hemvl
        koyam = Koyam(hemvl.lower())
        koyam.zewmakoyamvn()
        rr = len(koyam.kom_row)
        while True:
            koyam.kaxvrowvn()
            if rr == len(koyam.kom_row):
                break
            else:
                rr = len(koyam.kom_row)
        hemvlkawe = koyam.wirintuku_hemvl2()
        regexkawe = koyam.wirintuku_regex()
        wzkawe = koyam.wirintuku_wz()
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

        if len(hemvlkawe) > 0:
            for i in range(len(hemvlkawe)):
                xapvmal.append((hemvlkawe[i], regexkawe[i],wzkawe[i]))
            xipaalu['hemvlkawe'] = xapvmal


    else:
        xipaalu = dict()
        xipaalu['vy'] = hemvl
        xipaalu['eypial'] = 'Gelay zugu, ka kiñe rupa tukulfe'
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
        else:
            mvli = False
            pegelam_hemvl = pepikaam_hemvl(hemvl, mvli)
    else:
        mvli = False
        hemvl = ''
        pegelam_hemvl = pepikaam_hemvl(hemvl, mvli)
    return render_template('index.html', mvli=mvli, pegelam_hemvl=pegelam_hemvl)


@app.errorhandler(404)
def page_not_found(error):
    return '<h1> \'Na weza</h1>\n<h2>pegerkelai tati pakina </h2>'


if __name__ == '__main__':
    app.run('0.0.0.0', 5000, debug=True)
