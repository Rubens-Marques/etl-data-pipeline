import pytest
import pandas as pd
from src.etl.extractors.csv_extractor import CSVExtractor
from src.etl.transformers.cleaner import DataCleaner
from src.etl.loaders.csv_loader import CSVLoader
from src.etl.pipeline.runner import PipelineRunner


@pytest.fixture
def sample_csv(tmp_path):
    path = tmp_path / "input.csv"
    df = pd.DataFrame({
        "nome": ["Alice ", " Bob", "Alice "],
        "valor": [100, 200, 100],
    })
    df.to_csv(path, index=False)
    return str(path)


def test_pipeline_runs_end_to_end(sample_csv, tmp_path):
    output_path = str(tmp_path / "output.csv")
    runner = PipelineRunner(
        name="test-pipeline",
        extractor=CSVExtractor(sample_csv),
        transformer=DataCleaner(drop_duplicates=True, strip_strings=True),
        loader=CSVLoader(output_path),
    )
    result = runner.run()
    assert result["status"] == "success"
    assert result["rows_extracted"] == 3

    df_out = pd.read_csv(output_path)
    assert len(df_out) == 2
    assert df_out.iloc[0]["nome"] == "Alice"
