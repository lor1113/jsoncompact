from jsoncompact.serde import Deserializer, Serializer


def test_default_schema_1(serializer: Serializer, deserializer: Deserializer) -> None:
    schema = {"default": "default", "type": "string"}
    test_var = ""
    s1, s2 = serializer.serialize(test_var, schema)
    deserialized = deserializer.deserialize(s1, s2, schema)
    assert deserialized == test_var


def test_default_schema_2(serializer: Serializer, deserializer: Deserializer) -> None:
    schema = {"default": "default", "type": "string"}
    test_var = "default"
    s1, s2 = serializer.serialize(test_var, schema)
    deserialized = deserializer.deserialize(s1, s2, schema)
    assert deserialized == test_var


def test_default_schema_3(serializer: Serializer, deserializer: Deserializer) -> None:
    schema = {"default": 1, "type": "integer"}
    test_var = 0
    s1, s2 = serializer.serialize(test_var, schema)
    deserialized = deserializer.deserialize(s1, s2, schema)
    assert deserialized == test_var


def test_default_schema_4(serializer: Serializer, deserializer: Deserializer) -> None:
    schema = {"default": 1, "type": "integer"}
    test_var = 1
    s1, s2 = serializer.serialize(test_var, schema)
    deserialized = deserializer.deserialize(s1, s2, schema)
    assert deserialized == test_var


def test_default_schema_5(serializer: Serializer, deserializer: Deserializer) -> None:
    schema = {"default": True, "type": "boolean"}
    test_var = False
    s1, s2 = serializer.serialize(test_var, schema)
    deserialized = deserializer.deserialize(s1, s2, schema)
    assert deserialized == test_var


def test_default_schema_6(serializer: Serializer, deserializer: Deserializer) -> None:
    schema = {"default": True, "type": "boolean"}
    test_var = True
    s1, s2 = serializer.serialize(test_var, schema)
    deserialized = deserializer.deserialize(s1, s2, schema)
    assert deserialized == test_var
