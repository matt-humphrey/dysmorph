from functools import partial

import polars as pl
from polars import DataFrame

__all__ = [
    "DATA_TRANSFORMS",
]


def sort_by_id(df: DataFrame) -> DataFrame:
    return df.sort(by="ID")


def replace_missing_values(df: DataFrame) -> DataFrame:
    """Replace values for each given column that..."""
    return df.with_columns(
        pl.col(r"^.*$").replace({-99: None}),
    )


def apply_rounding(df: DataFrame) -> DataFrame:
    """Apply rounding to numeric columns"""
    return df.with_columns(
        pl.col(r"^.*$").round(1),
    )


def recast_types(df: DataFrame) -> DataFrame:
    """Recast column types as new type"""
    return df.with_columns(
        pl.col(r"^.*$").cast(pl.Int64),
    )


initial_transforms = [replace_missing_values]
final_transforms = [apply_rounding, recast_types, sort_by_id]

dataset_transforms = {
    "G200": [],
    "G201": [],
    "G202": [],
    "G203": [],
    "G105": [],
    "G205": [],
    "G108": [],
    "G208": [],
    "G210": [],
    "G114": [],
    "G214": [],
    "G117": [],
    "G217": [],
    "G220": [],
    "G222": [],
    "G227": [],
    "G228": [],
    "G126": [],
    "G0G1": [],
}

DATA_TRANSFORMS = {
    dset: initial_transforms + transforms + final_transforms
    for dset, transforms in dataset_transforms.items()
}
