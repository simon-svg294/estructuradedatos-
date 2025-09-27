import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from model.ticket import Ticket
from controller.ticketController import TicketController
from functions.queueFunctions import add_queue

def print_queue_status(queue_controller):
    """Imprime el estado actual de una cola de tickets"""
    print("\nEstado actual de la cola:")
    if queue_controller.is_empty():
        print("  Cola vacía")
        return
    
    current = queue_controller.head
    position = 1
    while current:
        print(f"  {position}. {current.data.name} (Edad: {current.data.age}, Prioridad: {current.priority})")
        current = current.next
        position += 1

def main():
    print("=== SISTEMA DE TICKETS DEL BANCO DE MIGUELITO ===")
    
    # Crear controladores para cada tipo de cola
    ticket_types = {
        "dudas": TicketController(),
        "asesor": TicketController(),
        "caja": TicketController(),
        "otros": TicketController()
    }
    
    # Crear algunos tickets de ejemplo
    tickets = [
        Ticket(
            name="Juan Pérez", 
            type="dudas",
            identity="12345678",
            case_description="Consulta sobre estado de cuenta",
            age=65,  # Mayor de 60, debería tener prioridad automática
            priority_attention=False
        ),
        Ticket(
            name="María García", 
            type="caja",
            identity="87654321",
            case_description="Deposito de cheque",
            age=35,
            priority_attention=True  # Solicita prioridad explícitamente
        ),
        Ticket(
            name="Pedro López", 
            type="caja",
            identity="23456789",
            case_description="Retiro de efectivo",
            age=30,
            priority_attention=False
        ),
        Ticket(
            name="Ana Martínez", 
            type="asesor",
            identity="98765432",
            case_description="Información sobre préstamos",
            age=70,  # Mayor de 60, debería tener prioridad automática
            priority_attention=False
        ),
        Ticket(
            name="Carlos Rodríguez", 
            type="dudas",
            identity="34567890",
            case_description="Problema con tarjeta",
            age=25,
            priority_attention=False
        ),
        Ticket(
            name="Lucia Fernández", 
            type="caja",
            identity="56789012",
            case_description="Pago de servicios",
            age=62,  # Mayor de 60, debería tener prioridad automática
            priority_attention=False
        ),
    ]
    
    # Encolar todos los tickets
    print("\nEncolar tickets...")
    for ticket in tickets:
        print(f"Agregando: {ticket.name} ({ticket.type}, Edad: {ticket.age}, Prioridad solicitada: {ticket.priority_attention})")
        add_queue(ticket, ticket_types)
    
    # Mostrar el estado de cada cola
    for queue_type, controller in ticket_types.items():
        print(f"\n=== Cola de {queue_type.upper()} ===")
        print_queue_status(controller)
    
    # Demostrar extracción de tickets (ejemplo con la cola de caja)
    print("\n\n=== DEMOSTRACIÓN DE ATENCIÓN EN CAJA ===")
    caja_queue = ticket_types["caja"]
    
    print("\nLlamar al siguiente cliente:")
    next_ticket = caja_queue.dequeue()
    if next_ticket:
        print(f"Atendiendo a: {next_ticket.name} (Edad: {next_ticket.age}, Prioridad: {'Sí' if next_ticket.priority_attention or next_ticket.age > 60 else 'No'})")
    
    print("\nEstado de la cola después de atender:")
    print_queue_status(caja_queue)
    
    print("\nLlamar al siguiente cliente:")
    next_ticket = caja_queue.dequeue()
    if next_ticket:
        print(f"Atendiendo a: {next_ticket.name} (Edad: {next_ticket.age}, Prioridad: {'Sí' if next_ticket.priority_attention or next_ticket.age > 60 else 'No'})")
    
    print("\nEstado de la cola después de atender:")
    print_queue_status(caja_queue)
    

if __name__ == "__main__":
    main()