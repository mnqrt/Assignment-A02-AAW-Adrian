from kafka import KafkaConsumer
from serealize_deserialize import deserialize

import constant

def create_consumer() -> KafkaConsumer:
  return KafkaConsumer(
    constant.FLIGHT_BOOKING_TOPIC,
    bootstrap_servers=constant.BOOTSTRAP_SERVERS,
    group_id=constant.PAYMENT_GROUP_ID,
    auto_offset_reset='earliest',
    value_deserializer=deserialize
  )

def process_payment(booking: dict) -> None:
  print(f'[Payment Service] Processing payment  --> {booking["booking_id"]} | {booking["passenger"]} | ${booking["price"]}')
  print(f'[Payment Service] Payment SUCCESS      --> {booking["booking_id"]}')


def main() -> None:
  consumer = create_consumer()
  print('[Payment Service] Waiting for bookings...')
  for message in consumer:
    process_payment(message.value)
    consumer.commit()

if __name__ == '__main__':
    main()