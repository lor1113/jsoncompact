import json

from jsoncompact.serde import Deserializer, Serializer
from jsoncompact.types import JsonSchema, PyJsonType


def serialize(value: PyJsonType, schema: JsonSchema) -> tuple[bytes, list]:
    serializer = Serializer()
    return serializer.serialize(value, schema)


def deserialize(field_list: bytes, data_list: list, schema: JsonSchema) -> PyJsonType:
    serializer = Deserializer()
    return serializer.deserialize(field_list, data_list, schema)


def serialize_json(value: PyJsonType, schema: JsonSchema) -> str:
    field_list, data_list = serialize(value, schema)
    return json.dumps([field_list, data_list])


def deserialize_json(json_data: str, schema: JsonSchema) -> PyJsonType:
    field_list, data_list = json.loads(json_data)
    return deserialize(field_list, data_list, schema)
