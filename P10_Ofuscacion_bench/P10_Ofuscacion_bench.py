# -*- coding: utf-8 -*- 
#Hora=28, si h>30, 3% mas por h extra
import time, statistics

tiempos=[]
repetir=True
while repetir:
    print "------------------------------------"
    horas=input("Horas trabajadas> ")

    t0 = time.time()
    if(horas<=30):
        pago=horas*28
     
        print "Pago total= $"+`pago`
    else:
        pago=horas*28
        extras=horas-30
        pago=pago+(extras*28*0.03)
        print "Horas extras: "+`extras`
        print "Pago h. extras= $"+`(extras*28*1.03)`
        print "Pago total= $"+`pago`
    tiempo=time.time() - t0
    tiempos.append(tiempo)

    media=statistics.mean(tiempos)
    moda=statistics.mode(tiempos)
    mediana=statistics.median(tiempos)
    def_est_pob=statistics.pvariance(tiempos)
    desv_est_mue=statistics.pstdev(tiempos)

    print "************************"
    print ("Tiempos registrados: "+str(tiempos))
    print ("Media de tiempos: "+str(media))
    print ("Moda de tiempos: "+str(moda))
    print ("Mediana de tiempos: "+str(mediana))
    print ("Definicion estandar de la poblacion de tiempos: "+str(def_est_pob))
    print ("Desviacion estandar de la muestra de tiempos: "+str(desv_est_mue))
    print "************************"
    decision=str(raw_input("Desea repetir (s,n)> "))
    if decision=="s":
        repetir=True
    elif decision=="n":

        repetir=False


archivo = open("datos.txt", "a") 
archivo.write("-----------------------------------------"+'\n')
archivo.write("Hora "+str(time.strftime("%I:%M:%S"))+'\n')
archivo.write("Tiempos registrados: "+str(tiempos)+'\n')


archivo.write ("Media de tiempos: "+str(media)+'\n')
archivo.write ("Moda de tiempos: "+str(moda)+'\n')
archivo.write ("Mediana de tiempos: "+str(mediana)+'\n')
archivo.write ("Definicion estandar de la poblacion de tiempos: "+str(def_est_pob)+'\n')
archivo.write ("Desviacion estandar de la muestra de tiempos: "+str(desv_est_mue)+'\n')

archivo.close() 


'''
# -*- coding: utf-8 -*-
#Hora=28, si h>30, 3% mas por h extra
if 64 - 64: i11iIiiIii
while True :
 print "------------------------------------"
 OO0o = input ( "Horas trabajadas> " )
 if ( OO0o <= 30 ) :
  Oo0Ooo = OO0o * 28
  if 85 - 85: OOO0O0O0ooooo % IIii1I . II1 - O00ooooo00
  print "Pago total= $" + ` Oo0Ooo `
 else :
  Oo0Ooo = OO0o * 28
  I1IiiI = OO0o - 30
  Oo0Ooo = Oo0Ooo + ( I1IiiI * 28 * 0.03 )
  print "Horas extras: " + ` I1IiiI `
  print "Pago h. extras= $" + ` ( I1IiiI * 28 * 1.03 ) `
  print "Pago total= $" + ` Oo0Ooo `
  if 27 - 27: iIiiiI1IiI1I1 * IIiIiII11i * IiIIi1I1Iiii - Ooo00oOo00o
  if 48 - 48: oO0o / OOooOOo / I11i / Ii1I
  if 48 - 48: iII111i % IiII + I1Ii111 / ooOoO0o * o00O0oo
  if 97 - 97: oO0o0ooO0 - IIII / OOooOOo - oO0o0ooO0
# dd678faae9ac167bc83abf78e5cb2f3f0688d3a3

'''
'''

PASOS para ofuscar:
git clone https://github.com/astrand/pyobfuscate.git
cd pyobfuscate/
python setup.py install

pyobfuscate example.py

'''


