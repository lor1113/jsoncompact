from itertools import product

import pytest
from pytest import FixtureRequest

from src.jsoncompact.serde import Deserializer, Serializer

SETTINGS = list(product([True, False], repeat=3))


@pytest.fixture(params=SETTINGS)
def serde_settings(request: FixtureRequest) -> tuple[bool, bool, bool]:
    return (request.param[0], request.param[1], request.param[2])


@pytest.fixture()
def serializer(serde_settings: tuple[bool, bool, bool]) -> Serializer:
    serializer = Serializer()
    serializer.COMPACT_ITERABLES = serde_settings[0]
    serializer.COMPACT_MAPPINGS = serde_settings[1]
    serializer.USE_DEFAULTS = serde_settings[2]
    return serializer


@pytest.fixture()
def deserializer(serde_settings: tuple[bool, bool, bool]) -> Deserializer:
    deserializer = Deserializer()
    deserializer.COMPACT_ITERABLES = serde_settings[0]
    deserializer.COMPACT_MAPPINGS = serde_settings[1]
    deserializer.USE_DEFAULTS = serde_settings[2]
    return deserializer
