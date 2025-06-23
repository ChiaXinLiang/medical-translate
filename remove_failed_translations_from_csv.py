#!/usr/bin/env python3
import pandas as pd
import sys

def append_count_then_filter(input_path, output_path, substring="Translation Failed"):
    """
    1. Reads the CSV at input_path into a DataFrame (all columns as strings).
    2. Counts how many times `substring` appears in each column.
    3. Appends a one‐row summary (with those per‐column counts) to the bottom of the DataFrame.
    4. Drops every row (from the combined DataFrame) where ANY column contains `substring`.
    5. Writes the result to output_path (no index column).
    """
    # 1) Load the CSV with every column as a string
    df = pd.read_csv(input_path, dtype=str, keep_default_na=False)

    # 2) Compute per-column counts of the substring
    counts = {
        col: int(df[col].str.contains(substring, regex=False).sum())
        for col in df.columns
    }

    # 3) Build a 1-row DataFrame containing those counts
    summary_row = pd.DataFrame([counts])

    # 4) Append the summary row to the DataFrame
    df_with_summary = pd.concat([df, summary_row], ignore_index=True)

    # 5) Build a boolean mask: True if ANY column in that row contains the substring
    mask_any = df_with_summary.apply(
        lambda row: row.str.contains(substring, regex=False).any(), axis=1
    )

    # 6) Drop all rows where mask_any is True
    result_df = df_with_summary[~mask_any].copy()

    # 7) Write the filtered DataFrame to CSV (no index)
    result_df.to_csv(output_path, index=False)
    print(f"Output written to {output_path}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print(f"Usage: {sys.argv[0]} <input.csv> <output.csv>")
        sys.exit(1)

    input_csv = sys.argv[1]
    output_csv = sys.argv[2]
    append_count_then_filter(input_csv, output_csv)
