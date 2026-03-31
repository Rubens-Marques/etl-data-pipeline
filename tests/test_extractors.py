import pytest
import pandas as pd
from src.etl.extractors.csv_extractor import CSVExtractor
from src.etl.extractors.api_extractor import APIExtractor
from unittest.mock import patch, MagicMock


@pytest.fixture
def sample_csv(tmp_path):
    path = tmp_path / "test.csv"
    df = pd.DataFrame({"nome": ["Alice", "Bob"], "valor": [100, 200]})
    df.to_csv(path, index=False)
    return str(path)


def test_csv_extractor_returns_dataframe(sample_csv):
    extractor = CSVExtractor(sample_csv)
    df = extractor.extract()
    assert isinstance(df, pd.DataFrame)
    assert len(df) == 2
    assert list(df.columns) == ["nome", "valor"]


def test_csv_extractor_file_not_found():
    extractor = CSVExtractor("/tmp/arquivo_nao_existe_xyz.csv")
    with pytest.raises(FileNotFoundError):
        extractor.extract()


def test_api_extractor_returns_dataframe():
    mock_response = MagicMock()
    mock_response.json.return_value = [
        {"id": 1, "name": "Item A"},
        {"id": 2, "name": "Item B"},
    ]
    mock_response.raise_for_status = MagicMock()
    with patch("requests.get", return_value=mock_response):
        extractor = APIExtractor("https://api.exemplo.com/data")
        df = extractor.extract()
    assert isinstance(df, pd.DataFrame)
    assert len(df) == 2
