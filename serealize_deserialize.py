import json

def serialize(data: dict) -> bytes:
  return json.dumps(data).encode('utf-8')

def deserialize(data: bytes) -> dict:
    return json.loads(data.decode('utf-8'))