import random, os, sys

print("")
print( """                         XOXOXOXOXOXOXOXOX
                              TA-TE-TI 
                         XOXOXOXOXOXOXOXOX """)
print("")
c=input("XXXOOOXXX Ingrese cualquier letra para jugar:")
lugares=["1","2","3","4","5","6","7","8","9"]
def imprimir ():
   print(f"""                       
                         XOXOXOXOXOXOXOXOX
                              TA-TE-TI 
                         XOXOXOXOXOXOXOXOX 
         
                - - - - - - - - - - - - - - - - - - - - 
                        
                           |           |
                           |           |
                     {lugares[0]}     |     {lugares[1]}     |     {lugares[2]}
                ___________|___________|___________
                           |           |
                           |           |
                     {lugares[3]}     |     {lugares[4]}     |     {lugares[5]}
                           |           |
                ___________|___________|___________
                           |           |
                           |           |
                     {lugares[6]}     |     {lugares[7]}     |     {lugares[8]}
                           |           |
                                 
                - - - - - - - - - - - - - - - - - - - - 
          
          """)



mov=0
j=True
while j!=False:
 
  def puntos():

   for i in range(0,9,3):
    if lugares[i]== lugares[i+1] and lugares[i+1]==lugares[i+2]:
      os.system("cls")
      if lugares[i]=="X":
        imprimir()
        print("GANASTE")
      elif lugares[i]=="O":
        imprimir()
        print("PERDISTE")
      sys.exit()
     

  for i in range(0,3):
    if lugares[i]== lugares[i+3] and lugares[i+3]==lugares[i+6]:
     os.system("cls")
     if lugares[i]=="X":
       imprimir()
       print("GANASTE")
     elif lugares[i]=="O":
       imprimir()
       print("PERDISTE")
     sys.exit()

  for i in range(0,2,2):
    if lugares[i]== lugares[i+4] and lugares[i+4]==lugares[i+8]:
     os.system("cls")
     if lugares[i]=="X":
       imprimir()
       print("GANASTE")
     elif lugares[i]=="O":
       imprimir()
       print("PERDISTE")
     sys.exit()

    if lugares[i-3]== lugares[i-5] and lugares[i-5]==lugares[i-7]:
     os.system("cls")
     if lugares[i-3]=="X":
       imprimir()
       print("GANASTE")
     elif lugares[i-3]=="O":
       imprimir()
       print("PERDISTE")
     sys.exit()

    


  os.system("cls")
  imprimir()
  jug=input("Ingresa tu movimiento: ")

  z=True

  if not (jug.isalpha()) and jug.isdigit:
   jug=int(jug)

  elif (jug.isalpha()):
   while z!=False:
    jug=input("Incorrecto, vuelva a ingresar una opción: ")
    if (jug.isdigit()):
      jug=int(jug)
      if jug<1 or jug>9:
        z=True
      elif jug>0 and jug<10:
        z=False

  while jug<1 or jug>9:
    jug=input("Incorrecto, vuelva a ingresar su movimiento: ")
    if not (jug.isalpha()) and jug.isdigit:
      jug=int(jug) 
    elif (jug.isalpha()):
      jug=2

  jug=str(jug)

  ff=lugares.index(jug)
  if ff>=0: 
    lugares.pop(ff)
    lugares.insert(ff,"X")
  puntos()
  
  mov+=1
  if mov==5:
    print("EMPATE")
    j=False
    break
     


  maq=random.randrange(1,9)
  maq=str(maq)
  while lugares.count(maq)==0:
    maq=random.randrange(1,9)
    maq=str(maq)
   
  vv=lugares.index(maq)
  if vv>=0: 
    lugares.pop(vv)
    lugares.insert(vv,"O")

  puntos()
puntos()
   


 
