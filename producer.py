from kafka import KafkaProducer
from dataclasses import dataclass, asdict
from serealize_deserialize import serialize
import json
import time
import random
import constant

@dataclass
class Booking:
  booking_id: str
  passenger: str
  flight: str
  seat: str
  price: int

  def to_dict(self) -> dict:
    return asdict(self)

  def __repr__(self) -> str:
    return f'Booking({self.booking_id}, {self.passenger}, {self.flight}, seat {self.seat}, ${self.price})'

def create_producer() -> KafkaProducer:
    return KafkaProducer(
        bootstrap_servers=constant.BOOTSTRAP_SERVERS,
        value_serializer=serialize
    )

def generate_random_booking() -> Booking:
  return Booking(
    booking_id=f'BK-{random.randint(0,99999):05d}',
    passenger=random.choice(constant.PASSENGERS),
    flight=random.choice(constant.FLIGHTS),
    seat=f'{random.randint(1, constant.SEAT_ROWS)}{random.choice(constant.SEAT_COLS)}',
    price=random.randint(constant.PRICE_MIN, constant.PRICE_MAX)
  )

def main() -> None:
  producer = create_producer()

  for i in range(constant.NUM_BOOKINGS):
    booking = generate_random_booking()
    producer.send(constant.FLIGHT_BOOKING_TOPIC, value=booking.to_dict())
    print(f'[Booking Service] Sent: {booking}')
    time.sleep(constant.PRODUCER_DELAY_SECONDS)

  producer.flush()
  print('[Booking Service] All bookings sent.')

if __name__ == '__main__':
  main()