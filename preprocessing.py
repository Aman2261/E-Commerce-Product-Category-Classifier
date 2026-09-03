import re


def normalize_text(text, keep_numbers=True):
    """
    Clean product title/description before passing it to TF-IDF.

    Parameters
    ----------
    text : str
        Raw product title or description.

    keep_numbers : bool
        If True, preserve alphanumeric product specifications
        such as 4K, 128GB, 15W, etc.

    Returns
    -------
    str
        Cleaned text.
    """

    # Convert to string and lowercase
    text = str(text).lower()

    # Expand common contractions
    contractions = {
        "can't": "cannot",
        "won't": "will not",
        "don't": "do not",
        "doesn't": "does not",
        "isn't": "is not",
        "aren't": "are not",
        "wasn't": "was not",
        "weren't": "were not",
        "it's": "it is",
        "that's": "that is",
    }

    for contraction, replacement in contractions.items():
        text = text.replace(contraction, replacement)

    # Remove URLs
    text = re.sub(r"https?://\S+|www\.\S+", " ", text)

    # Remove social-media handles
    text = re.sub(r"@\w+", " ", text)

    # Keep numbers/alphanumeric specifications if requested
    if keep_numbers:
        text = re.sub(r"[^a-z0-9\s]", " ", text)
    else:
        text = re.sub(r"[^a-z\s]", " ", text)

    # Remove extra whitespace
    text = re.sub(r"\s+", " ", text).strip()

    return text