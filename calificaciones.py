from promedio import promedio_semestre
#Definir colores para usarlos en print(f"")
RED = "\033[31m" 
GREEN = "\033[32m"  
YELLOW = "\033[33m"
BLUE = "\033[34m"
CYAN = "\033[36m" 
RESET = "\033[0m"
ORANGE = "\033[38;5;214m"
blue_to_green = [
"\033[38;2;0;0;255m", #COLOR_1   N Azul
"\033[38;2;0;21;234m", #COLOR_2 o
"\033[38;2;0;42;213m", #COLOR_3 s
"\033[38;2;0;64;191m", #COLOR_4 
"\033[38;2;0;85;170m", # COLOR_5  v
"\033[38;2;0;106;148m", #COLOR_6  e
"\033[38;2;0;128;127m", #COLOR_7  m
"\033[38;2;0;149;106m", #COLOR_8  o
"\033[38;2;0;170;85m", #COLOR_9   s
"\033[38;2;0;191;64m", #COLOR_10  !
"\033[38;2;0;213;42m", #COLOR_11   !
"\033[38;2;0;234;21m", #COLOR_12  !
"\033[0m"] #COLOR_13 - RESET  !Verde
import os
import pathlib
import sys
import time
ruta = r"C:\Users\nekom\OneDrive\Documentos\Universidad\programacion"
#r"" colocar r al inicio de un string hace que se ignore el parametro de reserva del '\' que tiene python y lo toma como caracter
def conversor_ruta(ruta): #Un metodo simplemente para convertir las rutas con '\' a '/' para mejor manejo de localizaciones
  cadena = ""
  for letra in range(int(len(ruta))):
    if (ruta[letra] == "\\"):
      cadena = cadena + "/"
      continue
    cadena = cadena + ruta[letra]
  return cadena
ruta = conversor_ruta(ruta)

sys.path.append(ruta) #Agregar la carpeta que colocamos en ruta para importar archivos
from proging import calificaciones


def main():
  global seguir
  global continuar
  global seguir_continuar
  seguir_continuar = True
  continuar = True
  seguir = True
  while continuar == True:
    menu() #Preferi colocar el metodo menu para mayor claridad y legibilidad del codigo
    
def menu():
    textos = [f"{CYAN}Menu principal:{RESET}",f"{YELLOW}1. Obtener el promedio de tres evaluaciones.",
                f"2. Obtener la minima calificacion del tercer parcial para acreditar.",f"3. Verificar estatus de materia NA's del alumno.",
                f"4. Verificar estatus de faltas del alumno.{RESET}",f"{RED}5. Finalizar programa.{RESET}"]
    os.system("cls") #Limpiar la consola cada vez que accedemos al menu
    for lineas in textos: #Iteracion en el arreglo o lista de 'textos'
      print(lineas) #Imprimir cada una de las lineas
      time.sleep(0.1) #Agregar una pequeña animacion al menu
    opcion= int(input(f"{GREEN}Digite la opcion deseada: {RESET}"))

    match(opcion):
        case 1: 
          time.sleep(0.2)
          global seguir
          seguir = True
          while(seguir == True):
            promedio_semestre()
            seguir_continuar = (input(f"¿Desea continuar? {GREEN}s{RESET}/{RED}n{RESET} "))                    
            if (seguir_continuar == "s" or seguir_continuar == "si" or seguir_continuar == "SI" or seguir_continuar == "Si" or seguir_continuar=="S"):
              seguir = True
            if (seguir_continuar == "n" or seguir_continuar == "no" or seguir_continuar == "NO" or seguir_continuar == "No" or seguir_continuar=="N"):
              seguir=False
        case 2:
          time.sleep(0.2)
          minima_calificacion(cal=minima_calificacion)
        case 3:
          time.sleep(0.2)
          seguir = True
          while(seguir == True):
            calificaciones()
            seguir_continuar = (input(f"¿Desea continuar? {GREEN}s{RESET}/{RED}n{RESET} "))                    
            if (seguir_continuar == "s" or seguir_continuar == "si" or seguir_continuar == "SI" or seguir_continuar == "Si" or seguir_continuar=="S"):
              seguir = True
            if (seguir_continuar == "n" or seguir_continuar == "no" or seguir_continuar == "NO" or seguir_continuar == "No" or seguir_continuar=="N"):
              seguir = False 
        case 4:
            time.sleep(0.2)
            faltas_alumno()
        case 5:
          despedida = "Nos vemos!!! "
          time.sleep(0.2)
          global continuar 
          continuar = False
          time.sleep(1)
          print(f"{CYAN}Finalizando el programa.{RESET}")
          time.sleep(1) 
          print(f"{CYAN}Gracias por usar el servicio de Klassen y Flores equipo NekoWorks{RESET}")
          time.sleep(1)
          os.system("cls")
          for i in range(len(despedida)):
            time.sleep(0.3)
            print(f"{blue_to_green[i]}{despedida[i]}", end = "", flush=True)
          time.sleep(3)
          os.system("cls")
        case _:  
          print("Opción no válida")

def minima_calificacion(cal):
  global seguir
  seguir = True
  while(seguir == True):
    calificacion_1=float(input("Primer calificación: \n"))
    if calificacion_1<0 or calificacion_1>10:
      print("Calificación NO válida")
    else:
      calificacion_2=float(input("Segunda calificación: \n"))
    if calificacion_2<0 or calificacion_2>10:
      print("Calificación NO válida")
    else:
      calificacion_3=((7-((calificacion_1+calificacion_2)*0.3))/0.4)
      calificacion_3 = round(calificacion_3,3)
    if calificacion_3>10:
      print("En el 3er parcial debes obtener un: ",calificacion_3)
      print(f"{RED}Materia no aprobada, imposibilidad de promediar con 7: Se necesita de {RESET}", calificacion_3,f"{RED}; number out of range.{RESET}")  
    elif calificacion_3==10:
      print(f"{ORANGE}Es momento de obtener un AS para pasar: Calificacion necesaria -> ",calificacion_3,f"{RESET}")
    elif calificacion_3>9 and calificacion_3<9.9:
      print(f"{ORANGE}Aun hay esperanza para ti: Se precisa de un ->{RESET} ",calificacion_3)
    elif calificacion_3<=2.5:
      print(f"{CYAN}Muy buen trabajo haz hecho un AS en ambos parciales, con un ->{RESET} ",calificacion_3,f"{CYAN} puedes pasar. {RESET}{GREEN} Felicidades{RESET}")  
    else:
      print(f"{GREEN}Posibilidad de promediar: alta, se requiere de un ->:{RESET} ",calificacion_3)# 1F60A
    seguir_continuar = (input(f"¿Desea continuar? {GREEN}s{RESET}/{RED}n{RESET} "))                    
    if (seguir_continuar == "s" or seguir_continuar == "si" or seguir_continuar == "SI" or seguir_continuar == "Si" or seguir_continuar=="S"):
      seguir = True
    if (seguir_continuar == "n" or seguir_continuar == "no" or seguir_continuar == "NO" or seguir_continuar == "No" or seguir_continuar=="N"):
      seguir=False
  

def faltas_alumno():
  global seguir
  seguir = True

  verificacion = False
  while(seguir == True): 
    while(verificacion == False):
      ordinario = True
      no_ordinario = True
      faltas = int(input("Ingresa la cantidad de faltas en la materia: \n"))
      if(faltas<0):
        print(f"{ORANGE}No sea chistoso joven, como va a tener faltas negativas. Le debemos asistencias o que?{RESET}")
      else:
        verificacion=True
    verificacion = False
    while(verificacion == False):
      horas_semanas = int(input(f"Ingresar la cantidad de horas por semana de la materia: \n"))
      if(horas_semanas<1):
        print(f"{ORANGE}Apoco no va a clases?{RESET}")
      elif (horas_semanas>5):
        print(f"{ORANGE}Porque tienes tantas horas a la semana?{RESET}")
      else:
        verificacion=True
    verificacion = False
    total_horas = (horas_semanas * 16)

    if faltas > (total_horas * .80):
      ordinario = False
      print(f"{RED}No tienes derecho a presentar examen ordinario.{RESET}")
    if faltas > (total_horas * .60):
      no_ordinario = False
      print(f"{RED}No tienes derecho a presentar examen no ordinario.{RESET}")
    if(faltas >= total_horas):
      print(f"{RED}Oye, si no quieres ir a la escuela no es necesario pagar por el semestre y ocupar un lugar.{RESET}")
    if (ordinario == True and no_ordinario == True):
      print(F"{GREEN}Puedes realizar ambos examenes.{RESET}")
    elif(ordinario == False and no_ordinario == False):
      print(F"{RED}No puedes realizar ningun examen.{RESET}")
    
    seguir_continuar = (input(f"¿Desea continuar? {GREEN}s{RESET}/{RED}n{RESET} "))                    
    if (seguir_continuar == "s" or seguir_continuar == "si" or seguir_continuar == "SI" or seguir_continuar == "Si" or seguir_continuar=="S"):
      seguir = True
    if (seguir_continuar == "n" or seguir_continuar == "no" or seguir_continuar == "NO" or seguir_continuar == "No" or seguir_continuar=="N"):
      seguir=False

if __name__=="__main__":
  main()   

