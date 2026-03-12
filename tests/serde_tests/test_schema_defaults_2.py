from jsoncompact.serde import Deserializer, Serializer


def test_default_schema_1(serializer: Serializer, deserializer: Deserializer) -> None:
    schema = {"properties": {"string": {"default": "default", "type": "string"}}, "type": "object"}
    test_var = {}
    s1, s2 = serializer.serialize(test_var, schema)
    deserialized = deserializer.deserialize(s1, s2, schema)
    assert deserialized == test_var


def test_default_schema_2(serializer: Serializer, deserializer: Deserializer) -> None:
    schema = {"properties": {"string": {"default": "default", "type": "string"}}, "type": "object"}
    test_var = {"string": "test"}
    s1, s2 = serializer.serialize(test_var, schema)
    deserialized = deserializer.deserialize(s1, s2, schema)
    assert deserialized == test_var


def test_default_schema_3(serializer: Serializer, deserializer: Deserializer) -> None:
    schema = {"properties": {"string": {"default": "default", "type": "string"}}, "type": "object"}
    test_var = {"string": "default"}
    s1, s2 = serializer.serialize(test_var, schema)
    deserialized = deserializer.deserialize(s1, s2, schema)
    assert deserialized == test_var


def test_default_schema_4(serializer: Serializer, deserializer: Deserializer) -> None:
    schema = {
        "properties": {"var": {"default": [], "items": {"type": "string"}, "type": "array"}},
        "type": "object",
    }
    test_var = {}
    s1, s2 = serializer.serialize(test_var, schema)
    deserialized = deserializer.deserialize(s1, s2, schema)
    assert deserialized == test_var


def test_default_schema_5(serializer: Serializer, deserializer: Deserializer) -> None:
    schema = {
        "properties": {"var": {"default": [], "items": {"type": "string"}, "type": "array"}},
        "type": "object",
    }
    test_var = {"var": []}
    s1, s2 = serializer.serialize(test_var, schema)
    deserialized = deserializer.deserialize(s1, s2, schema)
    assert deserialized == test_var


def test_default_schema_6(serializer: Serializer, deserializer: Deserializer) -> None:
    schema = {
        "properties": {"var": {"default": [], "items": {"type": "string"}, "type": "array"}},
        "type": "object",
    }
    test_var = {"var": ["test", "test2"]}
    s1, s2 = serializer.serialize(test_var, schema)
    deserialized = deserializer.deserialize(s1, s2, schema)
    assert deserialized == test_var


def test_default_schema_7(serializer: Serializer, deserializer: Deserializer) -> None:
    schema = {
        "properties": {
            "var": {"additionalProperties": {"type": "string"}, "default": {}, "type": "object"}
        },
        "type": "object",
    }
    test_var = {}
    s1, s2 = serializer.serialize(test_var, schema)
    deserialized = deserializer.deserialize(s1, s2, schema)
    assert deserialized == test_var


def test_default_schema_8(serializer: Serializer, deserializer: Deserializer) -> None:
    schema = {
        "properties": {
            "var": {"additionalProperties": {"type": "string"}, "default": {}, "type": "object"}
        },
        "type": "object",
    }
    test_var = {"var": {}}
    s1, s2 = serializer.serialize(test_var, schema)
    deserialized = deserializer.deserialize(s1, s2, schema)
    assert deserialized == test_var


def test_default_schema_9(serializer: Serializer, deserializer: Deserializer) -> None:
    schema = {
        "properties": {
            "var": {"additionalProperties": {"type": "string"}, "default": {}, "type": "object"}
        },
        "type": "object",
    }
    test_var = {"var": {"test": "test"}}
    s1, s2 = serializer.serialize(test_var, schema)
    deserialized = deserializer.deserialize(s1, s2, schema)
    assert deserialized == test_var
