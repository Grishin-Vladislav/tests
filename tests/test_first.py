import json

import pytest

from src.first import *


def get_full_names():
    with open('fixtures/full_names.json') as f:
        data = json.load(f)
    return data


@pytest.mark.parametrize('full_names', get_full_names())
def test_get_unique_names(full_names):
    data = full_names['data']
    expected = full_names['unique']
    result = get_unique_names(data)
    assert result == expected


@pytest.mark.parametrize('full_names', get_full_names())
def test_get_top_3_names(full_names):
    data = full_names['data']
    expected = full_names['top3']
    result = get_top_3_names(data)
    assert result == expected
    assert len(result) == 3
