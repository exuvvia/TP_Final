import random,pickle, sys, os
ruta=("C:/Users/exuvv/codes/TP Final Python/Generador_TicketsFINAL.py")
guardar=("DBTickets")
os.path.isfile(ruta)
x=True
listatickets=[]
os.system("cls")
with open(guardar, "rb") as f:
  listatickets = pickle.load(f)

while x!=False:
 print(" ")
 print("Bievenido/a al sistema de tickets")
 print(" ")
 print(""" 1-Generar un nuevo ticket
 2-Leer un ticket
 3-Salir""")
 print(" ")
 usu=input("Ingrese una opción para continuar: ")

 z=True 

 if not (usu.isalpha()) and usu.isdigit:
   usu=int(usu)

 elif (usu.isalpha()):
   while z!=False:
    usu=input("Incorrecto, vuelva a ingresar una opción: ")
    if (usu.isdigit()):
      usu=int(usu)
      if usu<1 or usu>4:
        z=True
      elif usu>0 and usu<4:
        z=False

 while usu<1 or usu>3:
   bb=input("Incorrecto, vuelva a ingresar opción:")
   if not (bb.isalpha()) and bb.isdigit:
     bb=int(bb)
     usu=bb
 
 while usu==1:
     print("")
     print("Ingrese los datos para generar un nuevo Ticket")
     print("")
     s=len(listatickets)
     for i in range (s,s+1):
       listatickets.append({})
       listatickets[i]["nombre"]=input("Ingrese nombre: ")
       listatickets[i]['sector']=input("Ingrese sector: ")
       listatickets[i]['asunto']=input("Ingrese asunto: ")
       listatickets[i]['problema']=input("Ingrese el problema: ")
       listatickets[i]['numticket']=random.randrange(1000,9999)
       
       print("")
       print(f""" 
       ********************************************************************      
       | =================================================================
       |                 Se generó su Nro de Ticket: {listatickets[i]['numticket']}   
       | =================================================================
       | Nombre: {listatickets[i]['nombre']}                              
       | Sector: {listatickets[i]['sector']}                              
       | Asunto: {listatickets[i]['asunto']}                              
       |                                                                  
       | Problema: {listatickets[i]['problema']}                          
       |                                                                  
       |            POR FAVOR RECUERDE SU NÚMERO DE TICKET                
       ********************************************************************
       """)
       
     print(" ")
     j=True
     while j!=False:
      var=input("¿Desea generar otro ticket? S/N: ")
      if not (var.isdigit()) and var.isalpha:
       varmin=var.lower()
       if varmin=="s":
         usu=1
         j=False
       elif varmin=="n":
         usu=0
         os.system("cls")
         j=False
       else:
        print("Incorrecto, ingrese S / N")
      else:
        print("Incorrecto, ingrese S / N")
        
     

 g=len(listatickets)

 while usu==2:
   print(" ")
   numticket1=int(input("Ingrese su número de ticket: "))
   for i in range (g):
    if numticket1 == listatickets[i]['numticket']:
      vv=i
      print(f""" 
        ********************************************************************      
       | =================================================================
       |                         Nro de Ticket: {listatickets[i]['numticket']}   
       | =================================================================
       | Nombre: {listatickets[i]['nombre']}                              
       | Sector: {listatickets[i]['sector']}                              
       | Asunto: {listatickets[i]['asunto']}                              
       |                                                                  
       | Problema: {listatickets[i]['problema']}                          
       |                                                                                 
       ********************************************************************
       """)
   k=True
   while k!=False:
    var1=input("¿Desea ver otro ticket? S/N: ")
    if not (var1.isdigit()) and var1.isalpha:
      varmin1=var1.lower()
      if varmin1=="s":
        usu=2
        k=False
      elif varmin1=="n":
        usu=0
        os.system("cls")
        k=False
      else:
        print("Incorrecto, ingrese S / N")
    else:
     print("Incorrecto, ingrese S / N")

 
 while usu==3: 
   print(" ")
   q=True
   while q!=False:
    var2=input("¿Desea salir? S/N: ")
    if not (var2.isdigit()) and var2.isalpha:
      varmin2=var2.lower()
      if varmin2=="s":
        with open(guardar, "wb") as f:
         pickle.dump(listatickets, f)
        sys.exit("Has salido.")
      elif varmin2=="n":
        usu=0
        os.system("cls")
        q=False
      else:
        print("Incorrecto, ingrese S / N")
    else:
     print("Incorrecto, ingrese S / N")
   
     
     