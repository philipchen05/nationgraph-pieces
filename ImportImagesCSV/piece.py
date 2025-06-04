import pandas as pd
from pathlib import Path
from domino.base_piece import BasePiece
from .models import InputModel, SecretsModel, OutputModel

class ImportImagesCSV(BasePiece):
    def piece_function(self, input_data: InputModel, secrets_data: SecretsModel):
        # 1) Domino hands you a Path to the uploaded CSV:
        csv_path: Path = input_data.in_csv

        # 2) Read it with pandas:
        df = pd.read_csv(csv_path)
        print(f"Read CSV with {df.shape[0]} rows and {df.shape[1]} columns.")
        print(f"Columns: {list(df.columns)}")

        # 3) (Optional) Write a new CSV to results_path for downstream Pieces:
        out_dir = Path(self.results_path)
        out_dir.mkdir(parents=True, exist_ok=True)
        cleaned_csv = out_dir / "cleaned.csv"
        df.to_csv(cleaned_csv, index=False)

        # 4) Return whatever you want in your OutputModel:
        return OutputModel(
            row_count=len(df),
            column_names=list(df.columns),
            out_file_path=cleaned_csv
        )
