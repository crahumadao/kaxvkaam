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
                    lkocka:"Nhem??l W??zalkawe",
                    lkocln:"Mari mari!",
                    cln:"Ta mu elk??nul-aeyu ki??e k??zawpey??m tami kelluaetew zoy kim mapuzugual, pewmagen mai t??fa mu zoy az??mneaimi t??fachi zugun llemai (tati zoy k??melu).",
                    labhml:"Nhem??l",
                    phhml:"T??fa mu tukulfe tami nhem??l.",
                    btnhml:"W??zalkafige",
                    labcgt:"Tami chumgentufiel tati k??zawpey??m.",
                    phcgt:"T??fa mu wirintukufe chumgechi zoy k??meleafel tai?? k??zawpey??m.",
                    btncgt:"Werk??lfige",
                    lkoazv:"Az??mam",
                    azv:"T??fa m??lei ki??eke nhem??l tami az??mafiel chumgechi p??neafiel t??fachi k??zawpey??m.",
                    lkogvxam:"Ka femgechi,T??fa mu elk??nugeai ki??e wirintukun tami entual nhem??l tami p??neafiel k??zawpey??m mu.",
                    lkogvxam1:"G??txam",
                    gvxam2:"Chillkatumen ki??e koneltun mew. I??che amuken Temuco mew, welu t??fachi txipantu amulan, wal??g mew ??? pemean??? ta??i re??ma Temuco mew.",
                    gvxam3:"M??lelu gorbea mew, N??txamkan ki??eke ??? che inchi??, feyeg??n ka chillkatukeig??n mapuzugun. Kakelu che kim ??? mapuzugukelu???.",
                    gvxam1:"Mari mari pu pe??i pu lamgen. I??che Juan pigen. N??txamkaw???ai?? ta??i pukem ??rk??tun mew. I??che amun willi mew, gorbea p??le.",
                    gvxam4:"Fanten mew i??che zoy kim??n mapuzugun, feymew petu ayiwk??len.",

                    pelan: "T??fachi nhem??l pelafi??, ka ki??e rupa  tukulfe.",
                    wirintukun:"Wirintukugelu {{hemvla['wirintukun']}} mu txokifi??.",
                    wvzalgeci:"Femgechi w??zalkafi??:",
                    butkp:"K??zawpey??m",
                    butcp:"Chumgechi p??neafiel",
                    butgp:"G??txam p??neafiel t??fa mu"
                 },
    wigkazugun:{
                    lkocka:"Separador de Palabras",
                    lkocln:"Hola!",
                    cln:"Aqu?? te dejo una herramienta para que te ayude a aprender m??s Mapuzugun, espero que con esto entiendas m??s este idioma (el mejor).",
                    labhml:"Palabra",
                    phhml:"Aqu?? pon tu palabra.",
                    btnhml:"Sep??ralo",
                    labcgt:"Comentario",
                    phcgt:"Aqu?? escribe como podr??a ser mejor nuestra herramienta",
                    btncgt:"Env??alo",
                    lkoazv:"Ejemplo",
                    azv:"Aqu?? hay algunas palabras de ejemplo para que entiendas como usar esta herramienta.",
                    lkogvxam:"Tambi??n, Aqu?? se dejar?? un texto para que saques palabras y las uses en la herramienta. ",
                    lkogvxam1:"Conversa",
                    gvxam1:"Hola hermanos hermanas. Yo me llamo Juan. Conversaremos de mi descanso de invierno (vacaciones). Yo fui al sur, por Gorbea.",
                    gvxam2:"Fui a estudiar en un koneltun*(internado de mapuzugun). Yo voy a temuco habitualmente, pero este a??o no fui, en el verano ir?? a ver a mi familia a temico.",
                    gvxam3:" Cuando estaba en Gorbea, hable con algunas personas, ell@s tambi??n estudian mapuzugun. Otras personas saben hablar mapuzugun.",
                    gvxam4:"Ahora yo se m??s mapuzugun, as?? que todav??a estoy feliz.",
                    pelan: "No encontr?? esta palabra, ponla denuevo.",
                    wirintukun:"Creo que est?? escrito en {{hemvla['wirintukun']}}.",
                    wvzalgeci:"As?? lo separ??:",
                    butkp:"Herramienta",
                    butcp:"Como usarla",
                    butgp:"Texto para usar aqu??"
                 }
    }




// define language reload onclick illiteration

function reloadPage() {
  setTimeout(function () {
    location.reload();
  }, 100);
}
