import pytest

from src.masks import get_mask_account, get_mask_card_number


@pytest.mark.parametrize(
    "card_number, mask_card",
    [
        ("7000792289606361", "7000 79** **** 6361"),
        ("gh20792289606361", ""),
        ("3423792289605623", "3423 79** **** 5623"),
        ("", ""),
        (" ", ""),
        ("2341253758363749473463", ""),
        ("hfgdtersdgersfuet", ""),
    ],
)
def test_get_mask(card_number, mask_card):
    assert get_mask_card_number(card_number) == mask_card


@pytest.mark.parametrize(
    "account, mask_account",
    [
        ("73654108430135874305", "**4305"),
        ("43523675891036453624", "**3624"),
        (" ", ""),
        ("", ""),
        ("fgrtsdarwetdgfhyters", ""),
        ("67464874583", ""),
        ("ad654108430135874305", ""),
    ],
)
def test_mask_account(account, mask_account):
    assert get_mask_account(account) == mask_account
