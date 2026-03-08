import pytest
from pytest import FixtureRequest

from src.jsoncompact.serde import Deserializer, Serializer

SETTINGS = ((True, True), (False, True), (True, False), (False, False))


@pytest.fixture(params=SETTINGS)
def serde_settings(request: FixtureRequest) -> tuple[bool, bool]:
    return (request.param[0], request.param[1])


@pytest.fixture()
def serializer(serde_settings: tuple[bool, bool]) -> Serializer:
    serializer = Serializer()
    serializer.COMPACT_ITERABLES = serde_settings[0]
    serializer.COMPACT_MAPPINGS = serde_settings[1]
    return serializer


@pytest.fixture()
def deserializer(serde_settings: tuple[bool, bool]) -> Deserializer:
    deserializer = Deserializer()
    deserializer.COMPACT_ITERABLES = serde_settings[0]
    deserializer.COMPACT_MAPPINGS = serde_settings[1]
    return deserializer
