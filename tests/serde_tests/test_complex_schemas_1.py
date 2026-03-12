from jsoncompact.serde import Deserializer, Serializer

SCHEMA = {
    "$defs": {
        "TestModel1": {
            "properties": {"string": {"type": "string"}},
            "required": ["string"],
            "type": "object",
        }
    },
    "properties": {
        "var": {"items": {"$ref": "#/$defs/TestModel1"}, "type": "array"}
    },
    "required": ["var"],
    "type": "object",
}


def test_serde_array_schema_1(serializer: Serializer, deserializer: Deserializer) -> None:
    test_var = {"var": []}
    s1, s2 = serializer.serialize(test_var, SCHEMA)
    deserialized = deserializer.deserialize(s1, s2, SCHEMA)
    assert deserialized == test_var


def test_serde_array_schema_2(serializer: Serializer, deserializer: Deserializer) -> None:
    test_var = {"var": [{"string": ""}]}
    s1, s2 = serializer.serialize(test_var, SCHEMA)
    deserialized = deserializer.deserialize(s1, s2, SCHEMA)
    assert deserialized == test_var


def test_serde_array_schema_3(serializer: Serializer, deserializer: Deserializer) -> None:
    test_var = {"var": [{"string": "aaab"}, {"string": "aaab"}]}
    s1, s2 = serializer.serialize(test_var, SCHEMA)
    deserialized = deserializer.deserialize(s1, s2, SCHEMA)
    assert deserialized == test_var
