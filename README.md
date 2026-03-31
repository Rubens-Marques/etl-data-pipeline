# etl-data-pipeline

> Template ETL Python — extrai de múltiplas fontes, transforma com Pandas e carrega em destino configurável.

![Python](https://img.shields.io/badge/Python-3.11+-3776AB?style=flat&logo=python)
![Pandas](https://img.shields.io/badge/Pandas-2.2-150458?style=flat&logo=pandas)
![License](https://img.shields.io/badge/License-MIT-green?style=flat)

## Sobre

Template modular para pipelines ETL. Troque os componentes conforme a necessidade — qualquer extractor, transformer ou loader funciona com qualquer outro via interface comum.

**Problema resolvido:** Cada pipeline de dados começa do zero. Este template fornece a estrutura, os componentes básicos e o padrão para que novos pipelines sejam criados em minutos.

## Arquitetura

```
[Extractor]  →  [Transformer]  →  [Loader]
CSV / API        Pandas              CSV
                 DataCleaner
```

## Componentes

| Componente | Opções |
|-----------|--------|
| Extractors | `CSVExtractor`, `APIExtractor` |
| Transformers | `DataCleaner` (deduplicação, nulos, normalização) |
| Loaders | `CSVLoader` (overwrite / append) |

## Instalação

```bash
git clone https://github.com/Rubens-Marques/etl-data-pipeline
cd etl-data-pipeline
python -m venv venv && source venv/bin/activate
pip install -r requirements.txt
```

## Como usar

```python
from src.etl.extractors.csv_extractor import CSVExtractor
from src.etl.transformers.cleaner import DataCleaner
from src.etl.loaders.csv_loader import CSVLoader
from src.etl.pipeline.runner import PipelineRunner

runner = PipelineRunner(
    name="vendas-diarias",
    extractor=CSVExtractor("dados/vendas.csv"),
    transformer=DataCleaner(drop_duplicates=True),
    loader=CSVLoader("output/vendas_limpo.csv"),
)
result = runner.run()
print(result)
# {'status': 'success', 'rows_extracted': 1500, 'rows_loaded': 1487, 'duration_seconds': 0.42}
```

## Testes

```bash
pytest tests/ -v
```

## Licença

MIT © Rubens Marques
