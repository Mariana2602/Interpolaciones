import random
import matplotlib.pyplot as plt

class InterpolacionLagrange:
    def __init__(self, puntos):
        self.puntos = puntos

    def lagrange(self, x):
        n = len(self.puntos)
        resultado = 0
        for i in range(n):
            x1, y1 = self.puntos[i]
            termino = y1
            for j in range(n):
                if i != j:
                    x2, _ = self.puntos[j]
                    termino *= (x - x2) / (x1 - x2)

            resultado += termino

        return resultado

dias = {"Lunes": 0, "Martes": 1, "Miércoles": 2, "Jueves": 3, "Viernes": 4, "Sábado": 5, "Domingo": 6}
numeroDia = {n: i for i, n in dias.items()}
temperaturas = [random.uniform(15, 30) for _ in range(7)]

puntos_interpolacion = [(dias["Miércoles"], temperaturas[dias["Miércoles"]]), (dias["Jueves"], temperaturas[dias["Jueves"]])]
interpolacion = InterpolacionLagrange(puntos_interpolacion)
interpolar = dias["Viernes"]
temp_interpolada = interpolacion.lagrange(interpolar)

print(f"Temperatura interpolada para {numeroDia[interpolar]} usando Lagrange: {temp_interpolada:.2f}°C")
plt.plot(list(numeroDia.keys()), temperaturas, marker='o', color='b', linestyle='-', label="Temperatura diaria")
plt.scatter(interpolar, temp_interpolada, color='r', label=f"Interpolación ({numeroDia[interpolar]})")

plt.xlabel("Día de la semana")
plt.ylabel("Temperatura (°C)")
plt.title("Temperaturas Diarias en una Semana y su Interpolación de Lagrange")
plt.grid(True)
plt.legend()
plt.show()