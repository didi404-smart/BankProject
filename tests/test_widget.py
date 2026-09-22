import pytest

from src.widget import get_date, mask_account_card


@pytest.mark.parametrize(
    "card, mask_card",
    [
        ("Visa Platinum 7000792289606361", "Visa Platinum 7000 79** **** 6361"),
        ("Счет 73654108430135874305", "Счет **4305"),
        ("", ""),
        (" ", ""),
        ("Visa Platinum 74658745", ""),
        ("Счет 54785487", ""),
        ("Visa Classic 6831982476737658", ""),
        ("Maestro 1596837868705199", "Maestro 1596 83** **** 5199")
    ],
)
def test_mask_account_card(card, mask_card):
    assert mask_account_card(card) == mask_card


@pytest.mark.parametrize(
    "data, new_data",
    [
        ("2024-03-11T02:26:18.671407", "11.03.2024"),
        (" ", ""),
        ("", ""),
        ("hgjfhkjfjghjghrtuurhehfytu", ""),
        ("2020.03.11T02:26:18.671407", ""),
        ("47547398574759348759847595", "")
    ],
)
def test_get_date(data, new_data):
    assert get_date(data) == new_data
