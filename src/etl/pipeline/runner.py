import logging
from datetime import datetime

logger = logging.getLogger(__name__)


class PipelineRunner:
    def __init__(self, name: str, extractor, transformer, loader):
        self.name = name
        self.extractor = extractor
        self.transformer = transformer
        self.loader = loader

    def run(self) -> dict:
        started_at = datetime.now()
        logger.info(f"[{self.name}] Iniciando pipeline")
        try:
            df_raw = self.extractor.extract()
            logger.info(f"[{self.name}] Extraídas {len(df_raw)} linhas")
            df_clean = self.transformer.transform(df_raw)
            logger.info(f"[{self.name}] Transformadas: {len(df_raw)} → {len(df_clean)} linhas")
            rows_loaded = self.loader.load(df_clean)
            logger.info(f"[{self.name}] Carregadas {rows_loaded} linhas")
            duration = (datetime.now() - started_at).total_seconds()
            return {
                "status": "success",
                "pipeline": self.name,
                "rows_extracted": len(df_raw),
                "rows_loaded": rows_loaded,
                "duration_seconds": round(duration, 2),
            }
        except Exception as e:
            logger.error(f"[{self.name}] Erro: {e}")
            return {"status": "error", "pipeline": self.name, "error": str(e)}
