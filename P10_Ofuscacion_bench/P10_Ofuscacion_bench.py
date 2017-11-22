# -*- coding: utf-8 -*- 
#Hora=28, si h>30, 3% mas por h extra
'''
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
#Hora=28, si h>30, 3% mas por h extra
import time , statistics
if 64 - 64: i11iIiiIii
OO0o = [ ]
Oo0Ooo = True
while Oo0Ooo :
 print "------------------------------------"
 O0O0OO0O0O0 = input ( "Horas trabajadas> " )
 if 5 - 5: iiI / ii1I
 ooO0OO000o = time . time ( )
 if ( O0O0OO0O0O0 <= 30 ) :
  ii11i = O0O0OO0O0O0 * 28
  if 66 - 66: iIiI * iIiiiI1IiI1I1 * o0OoOoOO00
  print "Pago total= $" + ` ii11i `
 else :
  ii11i = O0O0OO0O0O0 * 28
  I11i = O0O0OO0O0O0 - 30
  ii11i = ii11i + ( I11i * 28 * 0.03 )
  print "Horas extras: " + ` I11i `
  print "Pago h. extras= $" + ` ( I11i * 28 * 1.03 ) `
  print "Pago total= $" + ` ii11i `
 O0O = time . time ( ) - ooO0OO000o
 OO0o . append ( O0O )
 if 78 - 78: i11ii11iIi11i . oOoO0oo0OOOo + IiiI / Iii1ii1II11i
 iI111iI = statistics . mean ( OO0o )
 IiII = statistics . mode ( OO0o )
 iI1Ii11111iIi = statistics . median ( OO0o )
 i1i1II = statistics . pvariance ( OO0o )
 O0oo0OO0 = statistics . pstdev ( OO0o )
 if 6 - 6: oooO0oo0oOOOO - ooO0oo0oO0 - i111I * II1Ii1iI1i
 print "************************"
 print ( "Tiempos registrados: " + str ( OO0o ) )
 print ( "Media de tiempos: " + str ( iI111iI ) )
 print ( "Moda de tiempos: " + str ( IiII ) )
 print ( "Mediana de tiempos: " + str ( iI1Ii11111iIi ) )
 print ( "Definicion estandar de la poblacion de tiempos: " + str ( i1i1II ) )
 print ( "Desviacion estandar de la muestra de tiempos: " + str ( O0oo0OO0 ) )
 print "************************"
 iiI1iIiI = str ( raw_input ( "Desea repetir (s,n)> " ) )
 if iiI1iIiI == "s" :
  Oo0Ooo = True
 elif iiI1iIiI == "n" :
  if 91 - 91: i1 . IIii11I1 - i1111 - i1IIi11111i / I11i1i11i1I % Iiii
  Oo0Ooo = False
  if 87 - 87: i111I / Iiii + I11i1i11i1I - Iiii . Iiii / o0OoOoOO00
  if 11 - 11: i11ii11iIi11i % oooO0oo0oOOOO - oOoO0oo0OOOo
oo0O000OoO = open ( "datos.txt" , "a" )
oo0O000OoO . write ( "-----------------------------------------" + '\n' )
oo0O000OoO . write ( "Hora " + str ( time . strftime ( "%I:%M:%S" ) ) + '\n' )
oo0O000OoO . write ( "Tiempos registrados: " + str ( OO0o ) + '\n' )
if 34 - 34: i1 * i11ii11iIi11i
if 31 - 31: o0OoOoOO00 + IiiI . I11i1i11i1I
oo0O000OoO . write ( "Media de tiempos: " + str ( iI111iI ) + '\n' )
oo0O000OoO . write ( "Moda de tiempos: " + str ( IiII ) + '\n' )
oo0O000OoO . write ( "Mediana de tiempos: " + str ( iI1Ii11111iIi ) + '\n' )
oo0O000OoO . write ( "Definicion estandar de la poblacion de tiempos: " + str ( i1i1II ) + '\n' )
oo0O000OoO . write ( "Desviacion estandar de la muestra de tiempos: " + str ( O0oo0OO0 ) + '\n' )
if 68 - 68: i11ii11iIi11i - i11iIiiIii - IiiI / II1Ii1iI1i - IiiI + iIiiiI1IiI1I1
oo0O000OoO . close ( )
if 48 - 48: iIiI % oooO0oo0oOOOO . i11ii11iIi11i - IIii11I1 % iIiiiI1IiI1I1 % iIiI
if 3 - 3: i1111 + iiI
if 42 - 42: II1Ii1iI1i / iIiiiI1IiI1I1 + i11iIiiIii - IIii11I1
if 78 - 78: IiiI
# dd678faae9ac167bc83abf78e5cb2f3f0688d3a3


'''

PASOS para ofuscar:
git clone https://github.com/astrand/pyobfuscate.git
cd pyobfuscate/
python setup.py install

pyobfuscate example.py

'''


