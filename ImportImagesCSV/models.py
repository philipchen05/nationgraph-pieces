from pydantic import BaseModel
from pathlib import Path

class InputModel(BaseModel):
    in_csv: Path

class SecretsModel(BaseModel):
    SECRET_VAR: str

class OutputModel(BaseModel):
    row_count: int
    column_names: list[str]
    out_file_path: Path
