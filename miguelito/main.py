from typing import Union
from fastapi import FastAPI
from model import Ticket
from controller import TicketController
from functions import add_queue

app = FastAPI()

ticketTypes = {
    "dudas": TicketController(),
    "asesor": TicketController(),
    "caja": TicketController(),
    "otros": TicketController()
}

# Endpoint para crear un turno
@app.post("/ticketCreate")
def crear_turno(turno: Ticket):
    add_queue(turno, ticketTypes)
    return {"mensaje": "Turno creado correctamente", "datos_turno": turno}

# Endpoint para obtener el siguiente turno
@app.get("/ticketNext")
def obtener_siguiente_turno(tipo: str):
    if tipo not in ticketTypes:
        return {"mensaje": "Tipo de turno no válido", "datos_turno": None}
    
    ticket = ticketTypes[tipo].dequeue()
    if ticket is None:
        return {"mensaje": "No hay turnos en espera", "datos_turno": None}
    
    return {"mensaje": "El siguiente turno es", "datos_turno": ticket}

# Endpoint para listar los turnos en cola por el tipo de turno
@app.get("/ticketList")
def listar_turnos_cola(tipo: str):
    if tipo not in ticketTypes:
        return {"mensaje": "Tipo de turno no válido", "datos_turnos": []}
    
    tickets = ticketTypes[tipo].get_all_tickets()
    return {"mensaje": "Lista de turnos en cola", "datos_turnos": tickets}

# Otros endpoints existentes
@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}
