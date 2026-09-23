import pytest

from src.processing import filter_by_state, sort_by_date


@pytest.mark.parametrize(
    "data_fixture,status,expected",
    [
        (
            "test1",
            "EXECUTED",
            [
                {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
                {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
            ],
        ),
        (
            "test1",
            "CANCELED",
            [
                {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
                {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
            ],
        ),
        (
            "test2",
            "HELP",
            [],
        ),
    ],
)
def test_filter_by_state_parametrized(request, data_fixture, status, expected):
    old = request.getfixturevalue(data_fixture)
    assert filter_by_state(old, status=status) == expected


@pytest.mark.parametrize(
    "data_fixture,is_value,expected",
    [
        (
            "test1",
            False,
            [
                {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
                {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
                {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
                {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
            ],
        ),
        (
            "test1",
            True,
            [
                {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
                {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
                {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
                {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
            ],
        ),
    ],
)
def test_sort_by_date(request, data_fixture, is_value, expected):
    data = request.getfixturevalue(data_fixture)
    assert sort_by_date(data, is_value) == expected


@pytest.mark.parametrize(
    "old_list, new_list",
    [
        (
            [
                {"id": 1, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
                {"id": 2, "state": "CANCELED", "date": "2018-06-30T02:08:58.425572"},
                {"id": 3, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
            ],
            [
                {"id": 3, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
                {"id": 1, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
                {"id": 2, "state": "CANCELED", "date": "2018-06-30T02:08:58.425572"},
            ],
        )
    ],
)
def test_sort_by_date_2(old_list, new_list):
    assert sort_by_date(old_list) == new_list
