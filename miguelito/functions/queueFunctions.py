from model.ticket import Ticket
from controller.ticketController import TicketController

def add_queue(ticket: Ticket, ticketTypes: dict) -> None:
    """
    Add a ticket to the queue based on its type and priority
    """
    # Get the ticket type
    ticket_type = ticket.type.lower()
    
    # Check if ticket type exists, default to "otros" if not
    if ticket_type not in ticketTypes:
        ticket_type = "otros"
    
    # Asignar prioridad automáticamente a mayores de 50 años
    # incluso si no lo solicitan explícitamente
    priority = 1 if (ticket.priority_attention or ticket.age > 50) else 0
    
    # Add ticket to the appropriate queue
    ticketTypes[ticket_type].enqueue(ticket, priority)
    
    return None