
# Import utility functions for loading and cleaning Project Gutenberg data
from tt_gutenberg.utils import load_authors, load_languages, load_metadata, clean_aliases


def list_authors(by_languages=True, alias=True):
    """
    Returns a list of author aliases sorted by the number of unique language translations.
    Loads author, language, and metadata tables, merges them, and counts translations per alias.
    """
    # Load and clean the authors table (ensures aliases are standardized)
    authors = clean_aliases(load_authors())
    # Load the languages table (contains language info for each book)
    langs   = load_languages()
    # Load the metadata table (contains book and author IDs)
    meta    = load_metadata()

    # Merge metadata with authors and languages to associate books, authors, and languages
    merged = (
        meta
        .merge(authors, on="gutenberg_author_id", how="left")
        .merge(langs,  on="gutenberg_id",        how="left")
    )

    # Check if the expected language column exists after merging
    if "language_y" not in merged.columns:
        print("Column 'language_y' not found in merged DataFrame. Please check merge keys and DataFrame contents.")
        return []

    # Group by alias and count the number of unique languages (translations) for each alias
    counts = (
        merged.groupby("alias")["language_y"]
              .nunique()
              .sort_values(ascending=False)
    )
    # Return the list of aliases sorted by translation count
    return list(counts.index)