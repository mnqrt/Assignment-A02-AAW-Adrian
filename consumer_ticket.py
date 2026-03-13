from kafka import KafkaConsumer
from serealize_deserialize import deserialize

import constant

def create_consumer() -> KafkaConsumer:
  return KafkaConsumer(
    constant.FLIGHT_BOOKING_TOPIC,
    bootstrap_servers=constant.BOOTSTRAP_SERVERS,
    group_id=constant.TICKET_GROUP_ID,
    auto_offset_reset='earliest',
    value_deserializer=deserialize
  )


def issue_ticket(booking: dict) -> None:
  print(f'[Ticket Service] Generating ticket    --> {booking["booking_id"]} | {booking["passenger"]} | Flight {booking["flight"]} | Seat {booking["seat"]}')
  print(f'[Ticket Service] Ticket ISSUED         --> {booking["booking_id"]}')


def main() -> None:
  consumer = create_consumer()
  print('[Ticket Service] Waiting for bookings...')
  for message in consumer:
    issue_ticket(message.value)
    consumer.commit()


if __name__ == '__main__':
  main()