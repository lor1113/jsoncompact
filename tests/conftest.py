import pytest

from src.jsoncompact.serde import Deserializer, Serializer


@pytest.fixture
def serializer() -> Serializer:
    return Serializer()


@pytest.fixture
def deserializer() -> Deserializer:
    return Deserializer()
