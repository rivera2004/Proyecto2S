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

def resumen_dia(asistencia, atrasos, dia):
    asistentes = 0
    suma_atraso = 0
    for i in range(len(asistencia)):
        if asistencia[i][dia] == 1:
            asistentes += 1
            suma_atraso += atrasos[i][dia]
            if atrasos[i][dia] > 3 * Amax:
                print("Alerta: atraso extremo detectado")
                return None
    porc_dia = asistentes / len(asistencia) * 100
    atraso_prom_dia = suma_atraso / asistentes if asistentes > 0 else 0
    return asistentes, porc_dia, atraso_prom_dia

def clasificar_curso(prom_curso):
    if prom_curso >= 90:
        return "Curso estable"
    elif prom_curso >= 80:
        return "Curso en observación"
    else:
        return "Curso crítico"

def generar_reporte(porcs, atrasos_prom, estados, estado_curso, pmin, amax):
    reporte = "REPORTE DE ASISTENCIA Y PUNTUALIDAD\n"
    reporte += f"Pmin = {pmin}% | Amax = {amax} min\n\n"
    for i in range(len(porcs)):
        reporte += f"Estudiante {i+1}: Asistencia = {porcs[i]:.2f}% | "
        reporte += f"Atraso Prom = {atrasos_prom[i]:.2f} min | Estado = {estados[i]}\n"
    reporte += "\nEstado del curso: " + estado_curso
    return reporte

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
reporte = generar_reporte(porcentajes, atrasos_prom, estados, estado_curso, Pmin, Amax)
print("\n" + reporte)

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
    resultado = resumen_dia(asistencia, atrasos, d)
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
