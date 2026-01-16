from jsoncompact.serde import Deserializer, Serializer


def test_serde_array_schema_1(serializer: Serializer, deserializer: Deserializer) -> None:
    schema = {"type": "array"}
    test_var = []
    s1, s2 = serializer.serialize(test_var, schema)
    assert s2 == []
    assert s1 == b"\x00"
    deserialized = deserializer.deserialize(s1, s2, schema)
    assert deserialized == test_var


def test_serde_array_schema_2(serializer: Serializer, deserializer: Deserializer) -> None:
    schema = {"type": "array"}
    test_var = [1, 2, "3", None, True]
    s1, s2 = serializer.serialize(test_var, schema)
    assert s2 == [5, 1, 2, "3", None, True]
    assert s1 == b"\x80"
    deserialized = deserializer.deserialize(s1, s2, schema)
    assert deserialized == test_var


def test_serde_array_schema_3(serializer: Serializer, deserializer: Deserializer) -> None:
    schema = {"type": "array"}
    test_var = [1, 2, "3", {}, True]
    s1, s2 = serializer.serialize(test_var, schema)
    assert s2 == [5, 1, 2, "3", {}, True]
    assert s1 == b"\x80"
    deserialized = deserializer.deserialize(s1, s2, schema)
    assert deserialized == test_var


def test_serde_array_schema_4(serializer: Serializer, deserializer: Deserializer) -> None:
    schema = {"type": "array"}
    test_var = [1, 2, [3, 50, "5"], True]
    s1, s2 = serializer.serialize(test_var, schema)
    assert s2 == [4, 1, 2, [3, 50, "5"], True]
    assert s1 == b"\x80"
    deserialized = deserializer.deserialize(s1, s2, schema)
    assert deserialized == test_var


def test_serde_array_schema_5(serializer: Serializer, deserializer: Deserializer) -> None:
    schema = {"type": "array", "items": {"type": "array", "items": "number"}}
    test_var = [[1, 2], [3, 4]]
    s1, s2 = serializer.serialize(test_var, schema)
    assert s2 == [2, 2, 1, 2, 2, 3, 4]
    assert s1 == b"\xe0"
    deserialized = deserializer.deserialize(s1, s2, schema)
    assert deserialized == test_var
