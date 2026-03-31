import requests
import pandas as pd


class APIExtractor:
    def __init__(self, url: str, params: dict | None = None, headers: dict | None = None):
        self.url = url
        self.params = params or {}
        self.headers = headers or {}

    def extract(self) -> pd.DataFrame:
        response = requests.get(self.url, params=self.params, headers=self.headers, timeout=30)
        response.raise_for_status()
        data = response.json()
        if isinstance(data, list):
            return pd.DataFrame(data)
        if isinstance(data, dict):
            for key, value in data.items():
                if isinstance(value, list):
                    return pd.DataFrame(value)
        raise ValueError(f"Formato de resposta não suportado: {type(data)}")
