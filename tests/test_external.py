from unittest.mock import Mock, patch

import pytest

from src.external_api import get_convert_to_rub


@patch("src.external_api.os.getenv")
@patch("src.external_api.requests.get")
def test_get_convert_to_rub_1(mock_get, mock_getenv):
    mock_getenv.return_value = "fake_api"
    fake_response = Mock()
    fake_response.raise_for_status = Mock()
    fake_response.json.return_value = {"result": 123.45}
    mock_get.return_value = fake_response
    assert get_convert_to_rub("USD", 10) == 123.45
    mock_get.assert_called_once()


def test_get_convert_to_rub_2():
    with patch("src.external_api.os.getenv") as mock_getenv:
        mock_getenv.return_value = None
        with pytest.raises(RuntimeError):
            get_convert_to_rub("USD", 10)
