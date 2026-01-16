from jsoncompact.serde import Deserializer, Serializer


def test_serde_none_schema(serializer: Serializer, deserializer: Deserializer) -> None:
    schema = None
    test_var = [1, 2, "3", None, True]
    s1, s2 = serializer.serialize(test_var, schema)
    assert len(s2) == 1
    assert s2[0] == test_var
    assert len(s1) == 0
    deserialized = deserializer.deserialize(s1, s2, schema)
    assert deserialized == test_var


def test_serde_true_schema(serializer: Serializer, deserializer: Deserializer) -> None:
    schema = True
    test_var = [1, 2, "3", None, True]
    s1, s2 = serializer.serialize(test_var, schema)
    assert len(s2) == 1
    assert s2[0] == test_var
    assert len(s1) == 0
    deserialized = deserializer.deserialize(s1, s2, schema)
    assert deserialized == test_var


# NOTE: In theory a false schema matches nothing and always fails - but again, the purpose of
# this library is not to validate data to the schema. The library will package this identical
# to a "true" schema.
def test_serde_false_schema(serializer: Serializer, deserializer: Deserializer) -> None:
    schema = False
    test_var = [1, 2, "3", None, True]
    s1, s2 = serializer.serialize(test_var, schema)
    assert len(s2) == 1
    assert s2[0] == test_var
    assert len(s1) == 0
    deserialized = deserializer.deserialize(s1, s2, schema)
    assert deserialized == test_var


def test_serde_string_schema_1(serializer: Serializer, deserializer: Deserializer) -> None:
    schema = {"type": "string"}
    test_var = ""
    s1, s2 = serializer.serialize(test_var, schema)
    assert len(s2) == 1
    assert s2[0] == test_var
    assert len(s1) == 0
    deserialized = deserializer.deserialize(s1, s2, schema)
    assert deserialized == test_var


def test_serde_string_schema_2(serializer: Serializer, deserializer: Deserializer) -> None:
    schema = {"type": "string"}
    test_var = "aaabbb"
    s1, s2 = serializer.serialize(test_var, schema)
    assert len(s2) == 1
    assert s2[0] == test_var
    assert len(s1) == 0
    deserialized = deserializer.deserialize(s1, s2, schema)
    assert deserialized == test_var


def test_serde_null_schema(serializer: Serializer, deserializer: Deserializer) -> None:
    schema = {"type": "null"}
    test_var = None
    s1, s2 = serializer.serialize(test_var, schema)
    assert len(s2) == 1
    assert s2[0] == test_var
    assert len(s1) == 0
    deserialized = deserializer.deserialize(s1, s2, schema)
    assert deserialized == test_var


def test_serde_boolean_schema_1(serializer: Serializer, deserializer: Deserializer) -> None:
    schema = {"type": "boolean"}
    test_var = True
    s1, s2 = serializer.serialize(test_var, schema)
    assert len(s2) == 1
    assert s2[0] == test_var
    assert len(s1) == 0
    deserialized = deserializer.deserialize(s1, s2, schema)
    assert deserialized == test_var


def test_serde_boolean_schema_2(serializer: Serializer, deserializer: Deserializer) -> None:
    schema = {"type": "boolean"}
    test_var = False
    s1, s2 = serializer.serialize(test_var, schema)
    assert len(s2) == 1
    assert s2[0] == test_var
    assert len(s1) == 0
    deserialized = deserializer.deserialize(s1, s2, schema)
    assert deserialized == test_var


def test_serde_integer_schema_1(serializer: Serializer, deserializer: Deserializer) -> None:
    schema = {"type": "integer"}
    test_var = 0
    s1, s2 = serializer.serialize(test_var, schema)
    assert len(s2) == 1
    assert s2[0] == test_var
    assert len(s1) == 0
    deserialized = deserializer.deserialize(s1, s2, schema)
    assert deserialized == test_var


def test_serde_integer_schema_2(serializer: Serializer, deserializer: Deserializer) -> None:
    schema = {"type": "integer"}
    test_var = 999
    s1, s2 = serializer.serialize(test_var, schema)
    assert len(s2) == 1
    assert s2[0] == test_var
    assert len(s1) == 0
    deserialized = deserializer.deserialize(s1, s2, schema)
    assert deserialized == test_var


def test_serde_number_schema_1(serializer: Serializer, deserializer: Deserializer) -> None:
    schema = {"type": "number"}
    test_var = 0
    s1, s2 = serializer.serialize(test_var, schema)
    assert len(s2) == 1
    assert s2[0] == test_var
    assert len(s1) == 0
    deserialized = deserializer.deserialize(s1, s2, schema)
    assert deserialized == test_var


def test_serde_number_schema_2(serializer: Serializer, deserializer: Deserializer) -> None:
    schema = {"type": "number"}
    test_var = 400
    s1, s2 = serializer.serialize(test_var, schema)
    assert len(s2) == 1
    assert s2[0] == test_var
    assert len(s1) == 0
    deserialized = deserializer.deserialize(s1, s2, schema)
    assert deserialized == test_var


def test_serde_number_schema_3(serializer: Serializer, deserializer: Deserializer) -> None:
    schema = {"type": "number"}
    test_var = 432.56
    s1, s2 = serializer.serialize(test_var, schema)
    assert len(s2) == 1
    assert s2[0] == test_var
    assert len(s1) == 0
    deserialized = deserializer.deserialize(s1, s2, schema)
    assert deserialized == test_var
