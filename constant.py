BOOTSTRAP_SERVERS: str = 'localhost:9092'
FLIGHT_BOOKING_TOPIC: str = 'flight-booking'

PAYMENT_GROUP_ID: str = 'payment-group'
TICKET_GROUP_ID: str = 'ticket-group'
INSPECTOR_GROUP_ID: str = 'inspect-group'

NUM_BOOKINGS: int = 5
PRODUCER_DELAY_SECONDS: float = 5

FLIGHTS: list[str] = ['FLIGHT-001', 'FLIGHT-002', 'FLIGHT-003', 'FLIGHT-004']
PASSENGERS: list[str] = ['USER_01', 'USER_02', 'USER_03', 'USER_04', 'USER_05']
SEAT_ROWS: int = 30
SEAT_COLS: list[str] = ['A', 'B', 'C', 'D', 'E', 'F']
PRICE_MIN: int = 500
PRICE_MAX: int = 2000