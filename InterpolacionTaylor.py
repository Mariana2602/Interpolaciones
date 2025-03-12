import random
import matplotlib.pyplot as plt

class InterpolacionTaylor:
    def __init__(self, funcion, dia_semana, orden=2):
        self.funcion = funcion
        self.dia_semana = dia_semana
        self.orden = orden

    def derivada(self, f, x, h=1e-5):
        return (f(x + h) - f(x)) / h

    def taylor(self, x):
        valor = self.funcion(self.dia_semana)
        derivada1 = self.derivada(self.funcion, self.dia_semana)
        resultado = valor + derivada1 * (x - self.dia_semana)
        
        if self.orden > 1:
            derivada2 = self.derivada(lambda x: self.derivada(self.funcion, x), self.dia_semana)
            resultado += (derivada2 / 2) * (x - self.dia_semana)**2
            
        return resultado

dias = {"Lunes": 0, "Martes": 1, "Miércoles": 2, "Jueves": 3, "Viernes": 4, "Sábado": 5, "Domingo": 6}
numeroDia = {n: i for i, n in dias.items()}
temperaturas = [random.uniform(15, 30) for _ in range(7)]

def funcion_temperatura(dia):
    if dia < 0 or dia >= len(temperaturas) - 1:
        raise ValueError("Día fuera de rango")

    dia_inf = int(dia)       
    dia_sup = dia_inf + 1   
    peso = dia - dia_inf
    return temperaturas[dia_inf] * (1 - peso) + temperaturas[dia_sup] * peso

expansion = dias["Miércoles"]
interpolar = dias["Viernes"]
interpolacion = InterpolacionTaylor(funcion_temperatura, expansion)
temp_interpolacion = interpolacion.taylor(interpolar)
print(f"Temperatura interpolada para {numeroDia[interpolar]} usando Taylor: {temp_interpolacion:.2f}°C")

plt.plot(list(numeroDia.keys()), temperaturas, marker='o', color='b', linestyle='-', label="Temperatura diaria")
plt.scatter(numeroDia[interpolar], temp_interpolacion, color='r', label=f"Interpolación ({numeroDia[interpolar]})")

plt.xlabel("Día de la semana")
plt.ylabel("Temperatura (°C)")
plt.title("Temperaturas Diarias en una Semana y su Interpolación de Taylor")
plt.grid(True)
plt.legend()
plt.show()