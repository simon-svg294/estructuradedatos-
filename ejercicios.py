class baseEmpleado:
    def __init__(self, nombre: str, salario: float, departamento: str):
        self.nombre = nombre
        self.salario = salario
        self.departamento = departamento

    def trabajar(self) -> str:
        return f"El empleado {self.nombre} está trabajando en el departamento de {self.departamento}."

class Gerente(baseEmpleado):
    def __init__(self, nombre: str, salario: float, departamento: str, equipo: list):
        super().__init__(nombre, salario, departamento)
        self.equipo = equipo

    def trabajar(self) -> str:
        return f"El gerente {self.nombre} está gestionando el equipo: {self.equipo}. y su sueldo mensual es de {self.salario}"
class desarrollador(baseEmpleado):
    def __init__(self, nombre: str, salario: float, departamento: str, lenguaje: str):
        super().__init__(nombre, salario, departamento)
        self.lenguaje = lenguaje

    def trabajar(self) -> str:
        return f"El desarrollador {self.nombre} está programando en {self.lenguaje}. y el sueldo mensual es de {self.salario}"
    

mateo = desarrollador("Mateo", 6000000, "Desarrollo", "Python")
Simon = Gerente("Simón", 10000000, "Ventas", ["Mateo", "Melina"])
print(mateo.trabajar())
print(Simon.trabajar())