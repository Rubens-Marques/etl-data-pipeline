import pandas as pd


class DataCleaner:
    def __init__(
        self,
        drop_duplicates: bool = True,
        dropna_threshold: float = 0.5,
        strip_strings: bool = True,
    ):
        self.drop_duplicates = drop_duplicates
        self.dropna_threshold = dropna_threshold
        self.strip_strings = strip_strings

    def transform(self, df: pd.DataFrame) -> pd.DataFrame:
        result = df.copy()
        if self.drop_duplicates:
            result = result.drop_duplicates()
        threshold = int(len(result) * self.dropna_threshold)
        result = result.dropna(thresh=threshold, axis=1)
        if self.strip_strings:
            str_cols = result.select_dtypes(include="object").columns
            result[str_cols] = result[str_cols].apply(lambda col: col.str.strip())
        return result.reset_index(drop=True)
