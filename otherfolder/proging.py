def calificaciones():
  nas = int(input("Ingresa las calificaciones no aprobatorias tienes (NA's):\n"))
  semestre = int(input("Ingresa el semestre que cursas:\n"))
  match (semestre):
    case semestre if semestre <= 5:
        if(nas <= 8):
          print("Aun no estas en riesgo de baja definitiva")
        else:
          print("Ya estas dado de baja definitiva \U0001F480")
    case (8):
        if(nas <= 10):
            print("Aun no estas en riesgo de baja definitiva")
        else:
            print("Ya estas dado de baja definitiva \U0001F480")
    case (7 | 6):
        if(nas <= 11):
            print("Aun no estas en riesgo de baja definitiva")
        else:
            print("Ya estas dado de baja definitiva \U0001F480 (como weai vai a tener mas de 11 calificaciones sin aprobar??? \U0001F480 \U0001F480 \U0001F480 \U0001F480 \U0001F480 \U0001F480)")
    case _:
      if(nas < 9):
        print("No hay riesgo de baja definitiva")