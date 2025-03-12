import random
import matplotlib.pyplot as plt

class InterpolacionPolinomica:
    def __init__(self, puntos):
        self.puntos = sorted(puntos)

    def interpolar(self, x):
        for i in range(len(self.puntos) - 1):
            x1, y1 = self.puntos[i]
            x2, y2 = self.puntos[i + 1]
            if x1 <= x <= x2:
                return y1 + (y2 - y1) * (x - x1) / (x2 - x1)

        raise ValueError("El valor de x está fuera del rango de interpolación.")

dias = {"Lunes": 0, "Martes": 1, "Miércoles": 2, "Jueves": 3, "Viernes": 4, "Sábado": 5, "Domingo": 6}
numeroDia = {n: i for i, n in dias.items()}
temperaturas = [random.uniform(15, 30) for _ in range(7)]
puntos = [(dias[dia], temp) for dia, temp in zip(dias.keys(), temperaturas)]
interpolacion = InterpolacionPolinomica(puntos)
interpolar = dias["Viernes"]
temp_interpolada = interpolacion.interpolar(interpolar)

print(f"Temperatura interpolada para {numeroDia[interpolar]} usando Polinomios por Trozos: {temp_interpolada:.2f}°C")

plt.plot(list(numeroDia.keys()), temperaturas, marker='o', color='b', linestyle='-', label="Temperatura diaria")
plt.scatter(interpolar, temp_interpolada, color='r', label=f"Interpolación ({numeroDia[interpolar]})")
plt.xlabel("Día de la semana")
plt.ylabel("Temperatura (°C)")
plt.title("Temperaturas Diarias en una Semana y su Interpolación Polinómica por Trozos")
plt.grid(True)
plt.legend()
plt.show()
