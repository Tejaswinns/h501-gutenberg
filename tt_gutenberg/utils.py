
# Import pandas for data manipulation and pathlib for file path handling
import pandas as pd
from pathlib import Path

# Set the path to the data directory (one level above this file)
DATA = Path(__file__).resolve().parents[1] / "data"


# Load the authors table from CSV
def load_authors():
    return pd.read_csv(DATA / "gutenberg_authors.csv")


# Load the languages table from CSV
def load_languages():
    return pd.read_csv(DATA / "gutenberg_languages.csv")


# Load the metadata table from CSV
def load_metadata():
    return pd.read_csv(DATA / "gutenberg_metadata.csv")


# Clean the aliases column in the authors DataFrame
# - Removes rows with missing aliases
# - Strips leading/trailing whitespace from alias values
def clean_aliases(df):
    # Keep only rows with a non-empty alias and strip whitespace
    df = df[df["alias"].notna()]
    df["alias"] = df["alias"].str.strip()
    return df