from pathlib import Path
import pandas as pd


class CSVLoader:
    def __init__(self, output_path: str, mode: str = "overwrite"):
        self.output_path = Path(output_path)
        self.mode = mode

    def load(self, df: pd.DataFrame) -> int:
        self.output_path.parent.mkdir(parents=True, exist_ok=True)
        if self.mode == "append" and self.output_path.exists():
            df.to_csv(self.output_path, mode="a", header=False, index=False)
        else:
            df.to_csv(self.output_path, index=False)
        return len(df)
