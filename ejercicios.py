# Ejercicio 1
class baseEmpleado:
    def __init__(self, nombre: str, salario: float, departamento: str):
        self.nombre = nombre
        self.salario = salario
        self.departamento = departamento

class Empleado(baseEmpleado):
    def __init__(self, nombre: str, salario: float, departamento: str):
        super().__init__(nombre, salario, departamento)

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
Simon = Gerente("Simón", 10000000, "Ventas", ["Mateo", "Laura"])
melina = Empleado("Melina", 4000000, "Atención al cliente")
print(mateo.trabajar())
print(Simon.trabajar())
print(melina.trabajar())


# Ejercicio 2 
class FiguraGeometrica:
    def calcularArea(self) -> float:
        pass  
class Triangulo(FiguraGeometrica):
    def __init__(self, base: float, altura: float):
        self.base = base
        self.altura = altura

    def calcularArea(self) -> float:
        return (self.base * self.altura) / 2

class Cuadrado(FiguraGeometrica):
    def __init__(self, lado: float):
        self.lado = lado

    def calcularArea(self) -> float:
        return self.lado * self.lado

cuadradito = Cuadrado(4)
triangulito = Triangulo(3, 6)
print("Área del cuadrado:", cuadradito.calcularArea())
print("Área del triángulo:", triangulito.calcularArea())


# Ejercicio 3 
class Electrodomestico:
    def __init__(self, marca: str, modelo: str, consumoEnergetico: float):
        self.marca = marca
        self.modelo = modelo
        self.consumoEnergetico = consumoEnergetico
        
    def encender(self) -> str:
        return f"El electrodoméstico {self.marca} {self.modelo} está encendido y consume {self.consumoEnergetico} kw."

class Lavadora(Electrodomestico):
    def __init__(self, marca: str, modelo: str, consumoEnergetico: float, capacidad: float):
        super().__init__(marca, modelo, consumoEnergetico)
        self.capacidad = capacidad
    
    def encender(self) -> str:
        return f"La lavadora {self.marca} {self.modelo} con capacidad de {self.capacidad} kg está encendida y consume {self.consumoEnergetico} kw."
    
    def iniciarCicloDeLavado(self) -> str:
        return "La lavadora ha iniciado un ciclo de lavado."

class Refrigerador(Electrodomestico):
    def __init__(self, marca: str, modelo: str, consumoEnergetico: float, tieneCongelador: bool):
        super().__init__(marca, modelo, consumoEnergetico)
        self.tieneCongelador = tieneCongelador    
    def encender(self) -> str:
        tipo = "con congelador" if self.tieneCongelador else "sin congelador"
        return f"El refrigerador {self.marca} {self.modelo} {tipo} está encendido y consume {self.consumoEnergetico} kw."    
    def regularTemperatura(self) -> str:
        return "El refrigerador está regulando la temperatura."

lavadora1 = Lavadora("LG", "Turbo", 1.5, 10)
refrigerador1 = Refrigerador("Samsung", "Cool", 0.9, True)
print(lavadora1.encender())
print(lavadora1.iniciarCicloDeLavado())
print(refrigerador1.encender())
print(refrigerador1.regularTemperatura())


# Ejercicio 4
class Usuario:
    def __init__(self, nombre: str, contraseña: str):
        self.nombre = nombre
        self.contraseña = contraseña
    
    def iniciarSesion(self, nombre: str, contraseña: str) -> str:
        if self.nombre == nombre and self.contraseña == contraseña:
            return f" Bienvenido {self.nombre}, sesión iniciada correctamente."
        else:
            return " Credenciales incorrectas."

class Administrador(Usuario):
    def __init__(self, nombre: str, contraseña: str, gestionUsuarios: str):
        super().__init__(nombre, contraseña)
        self.gestionUsuarios = gestionUsuarios

    def gestionarUsuarios(self) -> str:
        return f" El administrador {self.nombre} está gestionando usuarios: {self.gestionUsuarios}"

class Cliente(Usuario):
    def __init__(self, nombre: str, contraseña: str, realizarCompras: str):
        super().__init__(nombre, contraseña)
        self.realizarCompras = realizarCompras

    def realizarCompra(self) -> str:
        return f" El cliente {self.nombre} está realizando una compra: {self.realizarCompras}"

admin = Administrador("Carlos", "1234", "Agregar y eliminar usuarios")
cliente1 = Cliente("Ana", "abcd", "Laptop y celular")
print(admin.iniciarSesion("Carlos", "1234"))  
print(admin.gestionarUsuarios())

print(cliente1.iniciarSesion("Ana", "abcd"))  
print(cliente1.realizarCompra())

print(cliente1.iniciarSesion("Ana", "12345"))
