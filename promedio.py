RED = "\033[31m" 
GREEN = "\033[32m"  
YELLOW = "\033[33m"
BLUE = "\033[34m"
CYAN = "\033[36m" 
RESET = "\033[0m"
ORANGE = "\033[38;5;214m"
def promedio_semestre():
    calificacion = [0,0,0]; multiplicador = [0.3,0.3,0.4]
    calificacion_temporal = -1; promedio = 0
    texto = ["primer","segundo","tercer"]
    for i in range(0,3):
        calificacion_temporal = float(input(f"Ingrese la calififcacion del {texto[i]} parcial: \n"))
        while calificacion_temporal > 10 or calificacion_temporal <0:
            calificacion_temporal = float(input(f"{RED}Ingrese una calificacion valida: \n{RESET}"))
        calificacion[i] = calificacion_temporal
        promedio += calificacion[i] * multiplicador [i]
        promedio = round(promedio,2)
    match(promedio):
        case promedio if promedio <7:
            print(f"{RED}El promedio del alumno es de {RESET}{promedio}")
        case promedio if promedio >=7 and promedio <=8:
            print(f"{ORANGE}El promedio del alumno es de {RESET}{promedio}")
        case promedio if promedio <9.9 and promedio>8:
            print(f"{GREEN}El promedio del alumno es de{RESET} {promedio}")
        case 10:
            print(f"{CYAN}El promedio del alumno es de {RESET}{promedio}{GREEN} perfecto.{RESET}")
