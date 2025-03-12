import random
import matplotlib.pyplot as plt

class InterpolacionHermite:
    def __init__(self, puntos, derivadas):
        self.puntos = puntos  
        self.derivadas = derivadas  

    def hermite(self, x):
        n = len(self.puntos)
        resultado = 0
        for i in range(n):
            x1, y1 = self.puntos[i]
            h = 1
            Li_deriv = 0
            for j in range(n):
                if i != j:
                    x2, _ = self.puntos[j]
                    h *= (x - x2) / (x1 - x2)
                    
            for j in range(n):
                if i != j:
                    x2, _ = self.puntos[j]
                    Li_deriv += 1 / (x1 - x2)

            resultado += (1 - 2 * (x - x1) * Li_deriv) * (h**2) * y1
            resultado += (x - x1) * (h**2) * self.derivadas[i][1]

        return resultado

dias = {"Lunes": 0, "Martes": 1, "Miércoles": 2, "Jueves": 3, "Viernes": 4, "Sábado": 5, "Domingo": 6}
numeroDia = {v: k for k, v in dias.items()}
temperaturas = [random.uniform(15, 30) for _ in range(7)]

derivadas = []
for i in range(len(temperaturas)):
    if 0 < i < len(temperaturas) - 1:
        derivada_aprox = (temperaturas[i + 1] - temperaturas[i - 1]) / 2  
    elif i == 0:
        derivada_aprox = (temperaturas[i + 1] - temperaturas[i])  
    else:
        derivada_aprox = (temperaturas[i] - temperaturas[i - 1])  
    derivadas.append((i, derivada_aprox))

puntos = [(dias["Miércoles"], temperaturas[dias["Miércoles"]]), (dias["Jueves"], temperaturas[dias["Jueves"]])]
derivadas_interpolacion = [derivadas[dias["Miércoles"]], derivadas[dias["Jueves"]]]
interpolacion = InterpolacionHermite(puntos, derivadas_interpolacion)

interpolar = dias["Viernes"]
temp_interpolada = interpolacion.hermite(interpolar)
print(f"Temperatura interpolada para {numeroDia[interpolar]} usando Hermite: {temp_interpolada:.2f}°C")

plt.plot(list(numeroDia.keys()), temperaturas, marker='o', color='b', linestyle='-', label="Temperatura diaria")
plt.scatter(interpolar, temp_interpolada, color='r', label=f"Interpolación ({numeroDia[interpolar]})")

plt.xlabel("Día de la semana")
plt.ylabel("Temperatura (°C)")
plt.title("Temperaturas diarias en una semana y su interpolación")
plt.grid(True)
plt.legend()
plt.show()
