class persona:
    altura: float
    def __init__(self, nombre: str, edad: int):
        self.nombre = nombre 
        self.edad = edad

    def saludar (self) -> str: 
        return f"hola, mi nombre es {self.nombre} y tengo {self.edad} años"

    def esMayor(self):
        return self.edad >= 18

    def __str__(self) -> str:
        return f"Nombre: {self.nombre}, Edad: {self.edad}"

class Estudiante(persona):
    __promedio: float 
    def __init__(self, nombre: str, edad: int, carrera: str):
        super().__init__(nombre, edad)
        self.carrera = carrera

    def estudiar(self) -> str:
        return f"El estudiante {self.nombre} está estudiando {self.carrera}."

    def __str__(self) -> str:
        return f"Nombre: {self.nombre}, Edad: {self.edad}, Carrera: {self.carrera}"
   
    def getPromedio(self) -> float:
        return self.__promedio
    def setPromedio(self, promedio: float):
        self.__promedio = promedio

simon = persona("Simon", 22) 
melina = Estudiante("Melina", 20, "Ingeniería")
print(simon.saludar())
print(melina.saludar())
simon.altura = 1.75
print(simon)
melina.setPromedio(8.5)
print(melina.getPromedio())