//define language reload anchors

window.onload = function() {

if (window.location.hash){
    if (window.location.hash === "#mapu"){
            lkocka.textContent = zugundata.mapuzugun.lkocka
            lkocln.textContent = zugundata.mapuzugun.lkocln
            cln.textContent = zugundata.mapuzugun.cln
            vhemvl.textContent = zugundata.mapuzugun.labhml
            hemvl.placeholder = zugundata.mapuzugun.phhml
            btnhml.value = zugundata.mapuzugun.btnhml
            vkellual.textContent = zugundata.mapuzugun.labcgt
            kellual.placeholder = zugundata.mapuzugun.phcgt
            btncgt.value = zugundata.mapuzugun.btncgt
            lkoazv.textContent = zugundata.mapuzugun.lkoazv
            azv.textContent = zugundata.mapuzugun.azv
            lkogvxam.textContent = zugundata.mapuzugun.lkogvxam
            lkogvxam1.textContent = zugundata.mapuzugun.lkogvxam1
            gvxam1.textContent = zugundata.mapuzugun.gvxam1
            gvxam2.textContent = zugundata.mapuzugun.gvxam2
            gvxam3.textContent = zugundata.mapuzugun.gvxam3
            gvxam4.textContent = zugundata.mapuzugun.gvxam4
            pelan.textContent = zugundata.mapuzugun.pelan
            wvzalgeci.textContent = zugundata.mapuzugun.wvzalgeci
            butkp.textContent = zugundata.mapuzugun.butkp
            butcp.textContent = zugundata.mapuzugun.butcp
            butgp.textContent = zugundata.mapuzugun.butgp

    }
    if (window.location.hash === "#wigka"){                  
            lkocka.textContent = zugundata.wigkazugun.lkocka
            lkocln.textContent = zugundata.wigkazugun.lkocln
            cln.textContent = zugundata.wigkazugun.cln
            vhemvl.textContent = zugundata.wigkazugun.labhml
            hemvl.placeholder = zugundata.wigkazugun.phhml
            btnhml.value = zugundata.wigkazugun.btnhml
            vkellual.textContent = zugundata.wigkazugun.labcgt
            kellual.placeholder = zugundata.wigkazugun.phcgt
            btncgt.value = zugundata.wigkazugun.btncgt
            lkoazv.textContent = zugundata.wigkazugun.lkoazv
            azv.textContent = zugundata.wigkazugun.azv
            lkogvxam.textContent = zugundata.wigkazugun.lkogvxam
            lkogvxam1.textContent = zugundata.wigkazugun.lkogvxam1
            gvxam1.textContent = zugundata.wigkazugun.gvxam1
            gvxam2.textContent = zugundata.wigkazugun.gvxam2
            gvxam3.textContent = zugundata.wigkazugun.gvxam3
            gvxam4.textContent = zugundata.wigkazugun.gvxam4
            pelan.textContent = zugundata.wigkazugun.pelan
            wvzalgeci.textContent = zugundata.wigkazugun.wvzalgeci
            butkp.textContent = zugundata.wigkazugun.butkp
            butcp.textContent = zugundata.wigkazugun.butcp
            butgp.textContent = zugundata.wigkazugun.butgp

    }
};
  const but =document.querySelectorAll('.but');
  const tbloque = document.querySelectorAll('.tbloque');    

    but.forEach( ( cadaBut , i )=>{
        but[i].addEventListener('click',()=>{
            but.forEach( ( cadaBut , i )=>{
                    but[i].classList.remove('activo')
                    tbloque[i].classList.remove('activo')
            })
            but[i].classList.add('activo')
            tbloque[i].classList.add('activo')

        })
    });

  const h4 =document.querySelectorAll('.h4');
  const abloque = document.querySelectorAll('.bloque');    

    h4.forEach( ( cadaH2 , i )=>{
        h4[i].addEventListener('click',()=>{

            if (h4[i].classList.contains('activo')){
                h4[i].classList.remove('activo')  
                abloque[i].classList.remove('activo')

            }else{
              h4[i].classList.add('activo')  
              abloque[i].classList.add('activo')
            }

        })
    });


    const h4R =document.querySelectorAll('.h4R');
    const rbloque = document.querySelectorAll('.bloqueR');    
  
      h4R.forEach( ( cadaH4R , i )=>{
          h4R[i].addEventListener('click',()=>{

            if (h4R[i].classList.contains('activo')){
              h4R[i].classList.remove('activo')  
              rbloque[i].classList.remove('activo')

          }else{
            h4R[i].classList.add('activo')  
            rbloque[i].classList.add('activo')
          }
  
          })
      });



  document.getElementById("hemvl").focus();



 

  
};






//traducciones
const zugundata = {  
    mapuzugun: {
                    lkocka:"Nhemül Wüzalkawe",
                    lkocln:"Mari mari!",
                    cln:"Ta mu elkünul-aeyu kiñe küzawpeyüm tami kelluaetew zoy kim mapuzugual, pewmagen mai tüfa mu zoy azümneaimi tüfachi zugun llemai (tati zoy kümelu).",
                    labhml:"Nhemül",
                    phhml:"Tüfa mu tukulfe tami nhemül.",
                    btnhml:"Wüzalkafige",
                    labcgt:"Tami chumgentufiel tati küzawpeyüm.",
                    phcgt:"Tüfa mu wirintukufe chumgechi zoy kümeleafel taiñ küzawpeyüm.",
                    btncgt:"Werkülfige",
                    lkoazv:"Azümam",
                    azv:"Tüfa mülei kiñeke nhemül tami azümafiel chumgechi püneafiel tüfachi küzawpeyüm.",
                    lkogvxam:"Ka femgechi,Tüfa mu elkünugeai kiñe wirintukun tami entual nhemül tami püneafiel küzawpeyüm mu.",
                    lkogvxam1:"Gütxam",
                    gvxam2:"Chillkatumen kiñe koneltun mew. Iñche amuken Temuco mew, welu tüfachi txipantu amulan, walüg mew ​ pemean​ tañi reñma Temuco mew.",
                    gvxam3:"Mülelu gorbea mew, Nütxamkan kiñeke ​ che inchiñ, feyegün ka chillkatukeigün mapuzugun. Kakelu che kim ​ mapuzugukelu​.",
                    gvxam1:"Mari mari pu peñi pu lamgen. Iñche Juan pigen. Nütxamkaw​aiñ tañi pukem ürkütun mew. Iñche amun willi mew, gorbea püle.",
                    gvxam4:"Fanten mew iñche zoy kimün mapuzugun, feymew petu ayiwkülen.",

                    pelan: "Tüfachi nhemül pelafiñ, ka kiñe rupa  tukulfe.",
                    wirintukun:"Wirintukugelu {{hemvla['wirintukun']}} mu txokifiñ.",
                    wvzalgeci:"Femgechi wüzalkafiñ:",
                    butkp:"Küzawpeyüm",
                    butcp:"Chumgechi püneafiel",
                    butgp:"Gütxam püneafiel tüfa mu"
                 },
    wigkazugun:{
                    lkocka:"Separador de Palabras",
                    lkocln:"Hola!",
                    cln:"Aquí te dejo una herramienta para que te ayude a aprender más Mapuzugun, espero que con esto entiendas más este idioma (el mejor).",
                    labhml:"Palabra",
                    phhml:"Aquí pon tu palabra.",
                    btnhml:"Sepáralo",
                    labcgt:"Comentario",
                    phcgt:"Aquí escribe como podría ser mejor nuestra herramienta",
                    btncgt:"Envíalo",
                    lkoazv:"Ejemplo",
                    azv:"Aquí hay algunas palabras de ejemplo para que entiendas como usar esta herramienta.",
                    lkogvxam:"También, Aquí se dejará un texto para que saques palabras y las uses en la herramienta. ",
                    lkogvxam1:"Conversa",
                    gvxam1:"Hola hermanos hermanas. Yo me llamo Juan. Conversaremos de mi descanso de invierno (vacaciones). Yo fui al sur, por Gorbea.",
                    gvxam2:"Fui a estudiar en un koneltun*(internado de mapuzugun). Yo voy a temuco habitualmente, pero este año no fui, en el verano iré a ver a mi familia a temico.",
                    gvxam3:" Cuando estaba en Gorbea, hable con algunas personas, ell@s también estudian mapuzugun. Otras personas saben hablar mapuzugun.",
                    gvxam4:"Ahora yo se más mapuzugun, así que todavía estoy feliz.",
                    pelan: "No encontré esta palabra, ponla denuevo.",
                    wirintukun:"Creo que está escrito en {{hemvla['wirintukun']}}.",
                    wvzalgeci:"Así lo separé:",
                    butkp:"Herramienta",
                    butcp:"Como usarla",
                    butgp:"Texto para usar aquí"
                 }
    }




// define language reload onclick illiteration

function reloadPage() {
  setTimeout(function () {
    location.reload();
  }, 100);
}
