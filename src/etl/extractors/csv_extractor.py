from pathlib import Path
import pandas as pd


class CSVExtractor:
    def __init__(self, file_path: str, **read_kwargs):
        self.file_path = Path(file_path)
        self.read_kwargs = read_kwargs

    def extract(self) -> pd.DataFrame:
        if not self.file_path.exists():
            raise FileNotFoundError(f"Arquivo não encontrado: {self.file_path}")
        return pd.read_csv(self.file_path, **self.read_kwargs)
