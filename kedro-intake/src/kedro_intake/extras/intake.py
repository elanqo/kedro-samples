from __future__ import annotations
import intake
from kedro.io import DataCatalog
from intake.source.base import DataSourceBase
from kedro.io import AbstractDataSet
from typing import Any


class IntakeCatalog(DataCatalog):
    @classmethod
    def from_config(
        cls,
        catalog: dict[str, dict[str, Any]] | None,
        credentials: dict[str, dict[str, Any]] = None,
        load_versions: dict[str, str] = None,
        save_version: str = None,
    ) -> DataCatalog:
        data_sources = intake.open_catalog("/home/ensangalufu/code/ResponsibleAIML/kedro-samples/kedro-intake/conf/base/intake.yml")

        return cls(
            data_sets=data_sources,
            layers=None,
            dataset_patterns=None,
            load_versions=load_versions,
            save_version=save_version,
        )

class IntakeDataSet(AbstractDataSet, DataSourceBase):
    def __init__(
        self,
        data_source: DataSourceBase 
    ) -> None:
        self._data_source = data_source

    def _load(self) -> Any:
        return self._data_source.read()

    def _save(self, _: Any) -> None:
       pass

    def _exists(self) -> bool:
        pass

    def _describe(self) -> Any:
        pass
