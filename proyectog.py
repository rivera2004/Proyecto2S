import matplotlib.pyplot as plt
# =========================
# 1. ENTRADA Y VALIDACIÓN
# =========================
while True:
    try:
        print("""
        Proyecto Integrador - Grupo 02
        Sistema de Asistencia y Puntualidad
        Programación en Python
        Carrera de Ciencia de Datos e Inteligencia Artificial
        Asignatura: Fundamentos de Programación
        January 6, 2026
        INTEGRANTES:Marcos Rivera,Marcos Cabrera, Katherin Torres, Nahomy Carreño
        """)
        Pmin = float(input("Ingrese el porcentaje mínimo de asistencia (0-100): "))
        if 0 < Pmin <= 100:
            break
        else:
            print("Valor inválido.")
    except:
        print("Ingrese un número válido.")

while True:
    try:
        Amax = float(input("Ingrese el atraso máximo permitido (minutos): "))
        if Amax > 0:
            break
        else:
            print("Valor inválido.")
    except:
        print("Ingrese un número válido.")

# =========================
# 2. MATRICES BASE (8x7)
# =========================
asistencia = [
    [1,1,1,1,1,1,1],
    [1,1,0,1,1,1,1],
    [1,0,0,1,1,1,0],
    [1,1,1,1,1,0,1],
    [0,1,1,1,0,1,1],
    [1,1,1,0,1,1,1],
    [1,1,1,1,1,1,0],
    [1,0,1,1,1,1,1]
]

atrasos = [
    [0,5,3,0,2,1,0],
    [2,0,0,4,6,0,3],
    [0,0,0,8,12,5,0],
    [1,3,2,0,0,0,4],
    [0,6,0,7,0,2,1],
    [0,0,5,0,9,0,2],
    [3,2,1,4,0,0,0],
    [0,0,6,2,1,3,4]
]

n_estudiantes = 8
n_dias = 7

# =========================
# 3. FUNCIONES OBLIGATORIAS
# =========================
def resumen_estudiante(lista_asistencia, lista_atrasos):
    total_asistencias = 0
    total_atrasos = 0
    dias_presentes = 0
    for a, t in zip(lista_asistencia, lista_atrasos):
        if t < 0:
            continue   # atraso inválido
        if a == 1:
            total_asistencias += 1
            total_atrasos += t
            dias_presentes += 1
    porcentaje = (total_asistencias / len(lista_asistencia)) * 100
    promedio_atraso = total_atrasos / dias_presentes if dias_presentes > 0 else 0
    return (
        total_asistencias,    
        porcentaje,            
        total_atrasos,        
        promedio_atraso       
    )

def porcentaje_asistencia(lista_asistencia):
    return sum(lista_asistencia) / len(lista_asistencia) * 100

def atraso_promedio(lista_asistencia, lista_atrasos):
    suma = 0
    contador = 0
    for a, t in zip(lista_asistencia, lista_atrasos):
        if t < 0:
            continue
        if a == 1:
            suma += t
            contador += 1
    return suma / contador if contador > 0 else 0

def clasificar_estudiante(porc, atraso_prom, pmin, amax):
    if porc < pmin:
        return "Crítico"
    elif porc >= pmin and atraso_prom > amax:
        return "En riesgo"
    else:
        return "Regular"

def resumen_dia(asistencia, atrasos, dia, amax):
    asistentes = 0
    suma_atrasos = 0
    for i in range(len(asistencia)):
        if atrasos[i][dia] < 0:
            continue
        if asistencia[i][dia] == 1:
            asistentes += 1
            suma_atrasos += atrasos[i][dia]
            if atrasos[i][dia] > 3 * amax:
                print("Alerta: atraso extremo detectado")
                break
    porcentaje_dia = (asistentes / len(asistencia)) * 100
    atraso_promedio_dia = suma_atrasos / asistentes if asistentes > 0 else 0
    return (
        asistentes,            
        porcentaje_dia,       
        atraso_promedio_dia    
    )

def clasificar_curso(prom_curso):
    if prom_curso >= 90:
        return "Curso estable"
    elif prom_curso >= 80:
        return "Curso en observación"
    else:
        return "Curso crítico"

# =========================
# 4. PROCESAMIENTO E IMPRESIÓN 
# =========================
def imprimir_reporte_general(porcs, atrasos_prom, estados, estado_curso, pmin, amax):
    total_estudiantes = len(porcs)
    promedio_asistencia_grupal = sum(porcs) / total_estudiantes
    promedio_atraso_grupal = sum(atrasos_prom) / total_estudiantes
    
    criticos = estados.count("Crítico")
    en_riesgo = estados.count("En riesgo")
    regulares = estados.count("Regular")

    print("\n==================================================")
    print("      REPORTE DE ASISTENCIA Y PUNTUALIDAD")
    print("==================================================")
    print(f"Configuración: Asistencia Mín: {pmin}% | Atraso Máx: {amax} min")
    print("--------------------------------------------------")
    print("RESUMEN DEL CURSO:")
    print(f"- Estado General: {estado_curso.upper()}")
    print(f"- Promedio Asistencia Grupal: {promedio_asistencia_grupal:.2f}%")
    print(f"- Promedio Atraso Grupal: {promedio_atraso_grupal:.2f} min")
    print(f"- Distribución: {regulares} Regulares, {en_riesgo} En Riesgo, {criticos} Críticos")
    print("--------------------------------------------------")
    print("DETALLE POR ESTUDIANTE:")
    for i in range(total_estudiantes):
        print(f"[Estudiante {i+1:02d}] Asistencia: {porcs[i]:>6.2f}% | Atraso Prom: {atrasos_prom[i]:>5.2f} min | Estado: {estados[i]}")
    print("==================================================")

def imprimir_detalle_por_dia(asistencia, atrasos, n_dias, amax):
    print("\n" + "="*30)
    print("DETALLE POR DÍA (CLASIFICACIÓN)")
    print("="*30)
    for d in range(n_dias):
        asistentes, porc_dia, prom_atr_dia = resumen_dia(asistencia, atrasos, d, amax)
        print(f"Día {d+1}: {asistentes} presentes | {porc_dia:.2f}% asistencia | Atraso prom: {prom_atr_dia:.2f} min")

# =========================
# 4. PROCESAMIENTO
# =========================
porcentajes = []
atrasos_prom = []
estados = []

for i in range(n_estudiantes):
    p = porcentaje_asistencia(asistencia[i])
    a = atraso_promedio(asistencia[i], atrasos[i])
    e = clasificar_estudiante(p, a, Pmin, Amax)
    porcentajes.append(p)
    atrasos_prom.append(a)
    estados.append(e)

prom_curso = sum(porcentajes) / n_estudiantes
estado_curso = clasificar_curso(prom_curso)

# =========================
# 5. REPORTE
# =========================
imprimir_reporte_general(porcentajes, atrasos_prom, estados, estado_curso, Pmin, Amax)

imprimir_detalle_por_dia(asistencia, atrasos, n_dias, Amax)

# =========================
# 6. VISUALIZACIONES
# =========================

# Gráfico de barras: asistencia por estudiante
plt.figure()
plt.bar(range(1, 9), porcentajes)
plt.axhline(Pmin)
plt.xlabel("Estudiante")
plt.ylabel("Asistencia (%)")
plt.title("Porcentaje de asistencia por estudiante")
plt.grid(True)
plt.show()

# Gráfico de línea: asistencia diaria
porc_dias = []
for d in range(n_dias):
    resultado = resumen_dia(asistencia, atrasos, d, Amax)
    if resultado:
        porc_dias.append(resultado[1])
plt.figure()
plt.plot(range(1, 8), porc_dias, marker='o')
plt.axhline(80)
plt.xlabel("Día")
plt.ylabel("Asistencia diaria (%)")
plt.title("Asistencia diaria del curso")
plt.grid(True)
plt.show()
