import marimo

__generated_with = "0.15.0"
app = marimo.App(width="medium")


@app.cell
def _():
    import banksia as bk
    import marimo as mo
    import polars as pl
    from typing import Any
    import re
    return Any, bk, mo, pl, re


@app.cell
def _():
    from dysmorph import read_all_datasets
    from dysmorph.config import DATASETS, RAW_DATA

    return DATASETS, read_all_datasets


@app.cell
def _(DATASETS, read_all_datasets):
    df, meta = read_all_datasets(DATASETS)
    return df, meta


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""## G126""")
    return


@app.cell
def _(df, pl):
    df.select("ID", pl.col("^G126_.*$")).filter(~pl.all_horizontal(pl.exclude("ID").is_null()))
    return


@app.cell
def _(meta, pl):
    meta.filter(pl.col("Variable").str.starts_with("G126"))
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ## G200

    Different enough that it makes more sense to just keep separate and not harmonise.
    """
    )
    return


@app.cell
def _(df, pl):
    df.select("ID", pl.col("^G200_.*$")).filter(~pl.all_horizontal(pl.exclude("ID").is_null()))
    return


@app.cell
def _(meta, pl):
    meta.filter(pl.col("Variable").str.starts_with("G200"))
    return


@app.cell
def _(mo):
    mo.md(r"""## G201""")
    return


@app.cell
def _(df, pl):
    df.select("ID", pl.col("^G201_.*$")).filter(~pl.all_horizontal(pl.exclude("ID").is_null()))
    return


@app.cell
def _(meta, pl):
    meta.filter(pl.col("Variable").str.starts_with("G201"))
    return


@app.cell
def _(mo):
    mo.md(r"""## G202""")
    return


@app.cell
def _(df, pl):
    df.select("ID", pl.col("^G202_.*$")).filter(~pl.all_horizontal(pl.exclude("ID").is_null()))
    return


@app.cell
def _(meta, pl):
    meta.filter(pl.col("Variable").str.starts_with("G202"))
    return


@app.cell
def _(mo):
    mo.md(r"""## G203""")
    return


@app.cell
def _(df, pl):
    df.select("ID", pl.col("^G203_.*$")).filter(~pl.all_horizontal(pl.exclude("ID").is_null()))
    return


@app.cell
def _(meta, pl):
    meta.filter(pl.col("Variable").str.starts_with("G203"))
    return


@app.cell
def _(mo):
    mo.md(r"""## G205""")
    return


@app.cell
def _(df, pl):
    df.select("ID", pl.col("^G205_.*$")).filter(~pl.all_horizontal(pl.exclude("ID").is_null()))
    return


@app.cell
def _(meta, pl):
    meta.filter(pl.col("Variable").str.starts_with("G205"))
    return


@app.cell
def _(mo):
    mo.md(r"""## G208""")
    return


@app.cell
def _(df, pl):
    df.select("ID", pl.col("^G208_DM.*$")).filter(~pl.all_horizontal(pl.exclude("ID").is_null()))
    return


@app.cell
def _(meta, pl):
    meta.filter(pl.col("Variable").str.starts_with("G208_DM"))
    return


@app.cell
def _(mo):
    mo.md(r"""## Troubleshooting G205""")
    return


@app.cell
def _(df, pl):
    df5 = df.select("ID", pl.col("^G205.*$")).filter(~pl.all_horizontal(pl.exclude("ID").is_null()))
    df5
    return (df5,)


@app.cell
def _(pl):
    def split_and_convert_columns(df: pl.DataFrame, columns: list[str]) -> pl.Expr:
        """
        Combine splitting and letter-to-number conversion in one step.

        This splits letters into columns AND converts them to numbers (A=1, B=2, etc.)
        """
        expressions = []

        for col in columns:
            max_length = df.select(pl.col(col).str.len_chars().max()).item()

            # Create alphabet mapping for conversion
            letter_to_num = {chr(ord('A') + i): i + 1 for i in range(26)}

            for i in range(max_length):
                suffix = chr(ord('A') + i)
                new_col = f"{col}{suffix}"

                expr = (pl.when(pl.col(col).str.len_chars() > i)
                        .then(
                            pl.col(col)
                            .str.slice(i, 1)
                            .map_elements(
                                lambda x: letter_to_num.get(x) if x in letter_to_num else None,
                                return_dtype=pl.Int64
                            )
                        )
                        .otherwise(None)
                        .alias(new_col))

                expressions.append(expr)

        return df.with_columns(expressions)
    return (split_and_convert_columns,)


@app.cell
def _(df5, pl, split_and_convert_columns):
    cols = [col for col in df5.columns if "DM" in col]
    (
        df5
        .with_columns(pl.col(r"^G205_DM\d+$").replace({"-99": None, "8888": None, "9999": None, "": None}))
        .pipe(split_and_convert_columns, cols)
    )
    return


@app.cell
def _(mo):
    mo.md(
        r"""
    ## Compare metadata between G205 and G201-G203

    - Note the differences for each variable
    - Strip out the field values like "A and Z"
    """
    )
    return


@app.cell
def _():
    letters_to_numbers = {chr(ord('A') + i): i + 1 for i in range(26)}
    return (letters_to_numbers,)


@app.cell
def _(Any, re):
    def compare_dicts(d1: dict[Any, str], d2: dict[Any, str], 
        ignore_case: bool = True,
        ignore_whitespace: bool = True,
        ignore_punctuation: bool = True,
    ) -> dict[Any, tuple[str, str]]:
        """
        Compare dictionaries with configurable text normalization.

        Args:
            d1, d2: Dictionaries to compare
            ignore_case: Ignore case differences
            ignore_whitespace: Normalize whitespace
            ignore_punctuation: Remove punctuation
        """
        def normalize_text(text: str) -> str:
            result = text

            if ignore_case:
                result = result.lower()

            if ignore_punctuation:
                # Remove punctuation but keep spaces
                result = re.sub(r'[^\w\s]', '', result)

            if ignore_whitespace:
                # Normalize whitespace
                result = re.sub(r'\s+', '', result.strip())

            return result

        s1 = set(d1.keys())
        s2 = set(d2.keys())
        common_keys = s1 & s2
        print("Different keys: ", s1.difference(s2), s2.difference(s1))

        return {
            key: (d1[key], d2[key])
            for key in common_keys
            if normalize_text(d1[key]) != normalize_text(d2[key])
        }
    return (compare_dicts,)


@app.cell
def _(meta, pl):
    g205_meta_dict = meta.filter(pl.col("Variable").str.starts_with("G205_DM")).to_dict(as_series=False)
    g205_meta = dict(zip(g205_meta_dict["basename"], g205_meta_dict["Field Values"]))
    return (g205_meta,)


@app.cell
def _(meta, pl):
    g201_meta_dict = meta.filter(pl.col("Variable").str.contains(r"G201_DM\d+A")).with_columns(basename=pl.col("basename").str.replace("A", "")).to_dict(as_series=False)
    g201_meta = dict(zip(g201_meta_dict["basename"], g201_meta_dict["Field Values"]))
    return (g201_meta,)


@app.cell
def _():
    from rich import print as rprint
    return (rprint,)


@app.cell
def _(bk, compare_dicts, g201_meta, g205_meta, letters_to_numbers, rprint):
    for var in g205_meta:
        print(var)
        g201_m = {k: v for k, v in bk.str_to_field_values(g201_meta[var]).items() if k > 0}
        g205_m = {letters_to_numbers.get(k): v[4:] for k, v in bk.str_to_field_values(g205_meta[var]).items() if isinstance(k, str) and len(k) == 1}
        rprint(compare_dicts(g201_m, g205_m))
    return


@app.cell
def _(meta, pl):
    meta.filter(pl.col("Variable").str.contains("DM19(A|$)"))
    return


@app.cell
def _(mo):
    mo.md(
        r"""
    DM2: 14->15; 26 = Tympanosclerosis vs Other  
    DM10: 14->15  
    DM13: 15->16
    """
    )
    return


@app.cell
def _():
    return


if __name__ == "__main__":
    app.run()
