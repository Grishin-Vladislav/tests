import json

import pytest

from src.first import *


def load_fixtures(path: str):
    with open(path) as f:
        data = json.load(f)
    return data


@pytest.mark.parametrize('data', load_fixtures('fixtures/full_names.json'))
def test_get_unique_names(data):
    full_names = data['data']
    expected = data['unique']
    result = get_unique_names(full_names)
    assert result == expected


@pytest.mark.parametrize('data', load_fixtures('fixtures/full_names.json'))
def test_get_top_3_names(data):
    full_names = data['data']
    expected = data['top3']
    result = get_top_3_names(full_names)
    assert result == expected
    assert len(result) == 3


@pytest.mark.parametrize('data', load_fixtures('fixtures/courses.json'))
def test_get_max_min_duration_courses(data):
    courses = data["courses"]
    durations = data["durations"]
    expected = data["expected"]
    result = get_max_min_duration_courses(courses, durations)
    assert result == expected
